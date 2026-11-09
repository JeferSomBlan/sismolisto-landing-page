"""Pruebas de aceptación de simulaciones HU-021, HU-030, HU-034, HU-039, HU-041.
No existen Gmail, tiendas publicadas, backend de sincronización ni rutas reales.
"""
import json
from pathlib import Path
from playwright.sync_api import sync_playwright
from test_ui import mount, browser_args
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'/'evidence';OUT.mkdir(parents=True,exist_ok=True)
results=[]
def scenario(browser, hu, number, title, fn, width=1440):
    page=browser.new_page(viewport={'width':width,'height':900})
    page.set_default_timeout(5000)
    errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
    try:
        mount(page)
        fn(page)
        assert not errors,errors
        result='PASS';obs='Interacción simulada observada y coherente con el resultado esperado; sin servicios reales.'
    except Exception as e:
        result='FAIL';obs=type(e).__name__+': '+str(e)[:200]
    finally:
        page.close()
    results.append({'HU':hu,'Escenario':number,'Titulo':title,'Resultado':result,'Observacion':obs,'Plataforma':'HTML/CSS/JS Chromium aislado'})
    print(result,hu,number,title,obs[:85],flush=True)

def eval_space(page):
    page.locator('#app-tabs [data-tab="evaluar"]').click()
    page.locator('#space-sample').select_option('aula')
    page.locator('#space-form button[type=submit]').click()
    for x in range(3):
        page.locator('#eval-form input[type=radio]').first.check()
        page.locator('#eval-form button[type=submit]').click()

def contact_success(page):
    page.locator('#contact-name').fill('Demostración')
    page.locator('#contact-email').fill('test@example.org')
    page.locator('#contact-message').fill('Consulta de prueba de aceptación')
    page.locator('#contact-form button[type=submit]').click()
    feedback=page.locator('#contact-feedback').inner_text()
    assert 'Mensaje enviado. Te responderemos en un plazo de 48 horas' in feedback
    assert 'SIMULACIÓN' in feedback and 'no se envió' in feedback.lower()
    assert page.locator('#contact-email').input_value()==''
    store=json.loads(page.evaluate("localStorage.getItem('sismolisto_academic_demo_v1')"))
    assert len(store['sentMessages'])==1

def contact_invalid(page):
    page.locator('#contact-name').fill('Prueba')
    page.locator('#contact-email').fill('correo-no-valido')
    page.locator('#contact-message').fill('Prueba')
    page.locator('#contact-form button[type=submit]').click()
    assert page.locator('#contact-email').evaluate('(el)=>el.validity.valid') is False
    assert page.locator('#contact-email').evaluate('(el)=>el.classList.contains("is-invalid")') is True
    assert not page.evaluate("localStorage.getItem('sismolisto_academic_demo_v1')")

def download_mobile(page):
    page.locator('#download-open').click()
    assert page.locator('#download-dialog').is_visible()
    assert page.get_by_role('button',name='Google Play · demo').is_visible()
    assert page.get_by_role('button',name='App Store · demo').is_visible()
    page.get_by_role('button',name='Google Play · demo').click()
    assert 'no existe una aplicación publicada' in page.locator('#download-feedback').inner_text()
    page.screenshot(path=str(OUT/'hu030-mobile-stores.png'))

def download_desktop(page):
    page.locator('#download-open').click()
    assert page.locator('.download-desktop-qr img').is_visible()
    assert page.locator('.download-desktop-qr img').evaluate('(el)=>el.complete && el.naturalWidth>0')
    assert (ROOT/'assets/images/illustrations/qr-sismolisto-demo.png').stat().st_size>200
    assert 'no descarga una aplicación' in page.locator('.download-desktop-qr').inner_text()
    page.screenshot(path=str(OUT/'hu030-desktop-qr.png'))

def route_normal(page):
    eval_space(page)
    page.locator('#app-tabs [data-tab="zonas"]').click()
    page.get_by_role('button',name='Ver ruta de evacuación').click()
    output=page.locator('#demo-route-result').inner_text()
    assert '65 unidades simuladas' in output and 'Pasillo principal' in output
    assert 'No es una ruta real' in output
    page.screenshot(path=str(OUT/'hu034-ruta-ficticia.png'))

def route_blocked(page):
    eval_space(page)
    page.locator('#app-tabs [data-tab="riesgos"]').click()
    page.locator('#risk-type').select_option('Ruta obstruida')
    page.locator('#risk-level').select_option('Crítico')
    page.locator('#risk-desc').fill('Tramo B bloqueado en el grafo ficticio')
    page.locator('#risk-form button[type=submit]').click()
    page.locator('#app-tabs [data-tab="zonas"]').click()
    page.get_by_role('button',name='Ver ruta de evacuación').click()
    assert page.locator('.map-route.blocked').count()==1
    assert page.locator('.map-route.alternative').count()==1
    output=page.locator('#demo-route-result').inner_text()
    assert '90 unidades simuladas' in output and 'Corredor alternativo' in output

def sync_offline(page):
    page.context.set_offline(True)
    page.locator('#app-tabs [data-tab="checklist"]').click()
    page.locator('[data-check="mochila"]').check()
    st=json.loads(page.evaluate("localStorage.getItem('sismolisto_academic_demo_v1')"))
    assert st['syncPending'] is True
    page.context.set_offline(False)
    page.wait_for_function("JSON.parse(localStorage.getItem('sismolisto_academic_demo_v1')).syncPending === false")
    page.locator('#app-tabs [data-tab="progreso"]').click()
    assert 'Sincronización local simulada' in page.locator('#app-content').inner_text()
    st=json.loads(page.evaluate("localStorage.getItem('sismolisto_academic_demo_v1')"))
    assert st['syncHistory']

def profile_initial(page):
    page.locator('#app-tabs [data-tab="inicio"]').click()
    assert 'Primera visita' in page.locator('#app-content').inner_text()
    page.locator('#app-tabs [data-tab="progreso"]').click()
    assert 'Simulación de primera sesión' in page.locator('#profile-status').inner_text()
    page.locator('#profile-role').select_option('oficina')
    page.locator('#profile-space').select_option('oficina')
    page.locator('#profile-form button[type=submit]').click()
    assert 'Contexto configurado' in page.locator('#profile-status').inner_text()
    page.locator('#app-tabs [data-tab="inicio"]').click()
    assert 'Trabajador de oficina' in page.locator('#app-content').inner_text()

with sync_playwright() as p:
    browser=p.chromium.launch(**browser_args())
    for args in [
      ('HU-021',1,'Envío ficticio con mensaje y limpieza',contact_success,1440),
      ('HU-021',2,'Entrada inválida bloqueada',contact_invalid,1440),
      ('HU-030',1,'Tiendas de aplicaciones simuladas en móvil',download_mobile,390),
      ('HU-030',2,'QR demostrativo en escritorio',download_desktop,1440),
      ('HU-034',1,'Ruta más corta en grafo ficticio',route_normal,1440),
      ('HU-034',2,'Ruta alterna ficticia ante bloqueo',route_blocked,1440),
      ('HU-039',2,'Sincronización local simulada tras reconexión',sync_offline,1440),
      ('HU-041',1,'Configuración inicial de perfil simulado',profile_initial,1440),
    ]:
        scenario(browser,*args)
    browser.close()
(OUT.parent/'PRUEBAS_SIMULACION_HU021_030_034_039_041.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print('SUMMARY',json.dumps({'passed':sum(x['Resultado']=='PASS' for x in results),'failed':sum(x['Resultado']=='FAIL' for x in results)}),flush=True)
