"""Pruebas dirigidas a HU-032/041/042/044/045/048 y regresión, navegador aislado.
No representan pruebas de 100 escenarios ni de despliegue GitHub Pages.
"""
from pathlib import Path
from test_ui import sync_playwright,mount,browser_args

PASS=[]
def check(name, condition):
    assert condition, 'FAIL: '+name
    PASS.append(name)
    print('PASS',name,flush=True)

with sync_playwright() as p:
    browser=p.chromium.launch(**browser_args())
    page=browser.new_page(viewport={'width':390,'height':844})
    page.set_default_timeout(5000)
    failures=[]
    page.on('pageerror',lambda e:failures.append(str(e)))
    mount(page)
    # HU-044 bottom navigation, only mobile; data is same as desktop section.
    check('HU-044 barra inferior visible móvil',page.locator('#mobile-app-nav').is_visible())
    page.locator('#mobile-app-nav [data-tab="progreso"]').click()
    check('HU-044 navegación a Perfil',page.locator('#profile-form').is_visible())
    check('HU-041 perfil configurable',page.locator('#profile-role').count()==1 and page.locator('#profile-space').count()==1)
    page.locator('#profile-role').select_option('oficina')
    page.locator('#profile-space').select_option('oficina')
    page.locator('#profile-form button[type=submit]').click()
    page.locator('#mobile-app-nav [data-tab="inicio"]').click()
    check('HU-041 contexto oficina actualizado', 'Trabajador de oficina' in page.locator('#app-content').inner_text() and 'Oficina B-12' in page.locator('#app-content').inner_text())
    # HU-031 / HU-042: evaluation, option back at first step offers save or discard.
    page.locator('#app-tabs [data-tab="evaluar"]').click()
    page.locator('#space-sample').select_option('oficina')
    page.locator('#space-form button[type=submit]').click()
    page.locator('#eval-form button[data-action="eval-back"]').click()
    check('HU-042 diálogo guardar antes de salir',page.locator('#leave-eval-dialog').is_visible() and page.locator('#leave-eval-save').is_visible() and page.locator('#leave-eval-discard').is_visible())
    page.locator('#leave-eval-cancel').click()
    check('HU-042 cancelar mantiene evaluación',page.locator('#eval-form').is_visible())
    page.locator('#eval-form input[value="No"]').check()
    page.locator('#eval-form button[type=submit]').click()
    page.locator('#eval-form button[data-action="eval-save"]').click()
    check('HU-048 reanudación indica porcentaje', '33 %' in page.locator('#app-content').inner_text() and 'Continúa donde te quedaste' in page.locator('#app-content').inner_text())
    # HU-041 changing context persists after current edit, available in Profile tab.
    page.locator('#mobile-app-nav [data-tab="progreso"]').click()
    page.locator('#profile-role').select_option('estudiante')
    page.locator('#profile-space').select_option('aula')
    page.locator('#profile-form button[type=submit]').click()
    check('HU-041 cambio de espacio',page.locator('#profile-space').input_value()=='aula')
    # HU-031 -> 032 -> 045 full example.
    page.locator('#app-tabs [data-tab="evaluar"]').click()
    # La evaluación anterior sigue pendiente del contexto anterior; descartarla con confirmación.
    page.locator('#eval-form button[data-action="eval-back"]').click()
    page.locator('#eval-form button[data-action="eval-back"]').click()
    page.locator('#leave-eval-discard').click()
    page.locator('#app-tabs [data-tab="evaluar"]').click()
    page.locator('#space-sample').select_option('aula')
    page.locator('#space-form button[type=submit]').click()
    for answer in ['No','No','Sí']:
        page.locator('#eval-form input[value="'+answer+'"]').check()
        page.locator('#eval-form button[type=submit]').click()
    check('HU-031 evaluación terminada tras cambio de espacio',page.locator('#app-content').get_by_text('Última evaluación guardada',exact=False).count()>0)
    page.locator('#mobile-app-nav [data-tab="riesgos"]').click()
    for description,typ,level in [('Obstrucción del aula de ejemplo','Ruta obstruida','Crítico'),('Vidrio de ejemplo','Vidrio','Precaución')]:
        page.locator('#risk-desc').fill(description)
        page.locator('#risk-type').select_option(typ)
        page.locator('#risk-level').select_option(level)
        page.locator('#risk-form button[type=submit]').click()
    page.locator('#mobile-app-nav [data-tab="zonas"]').click()
    check('HU-032 dos riesgos presentes en el mapa',page.locator('.map-marker.risk').count()==2)
    check('HU-034 se muestra alternativa ficticia cuando hay bloqueo',page.locator('.map-route.blocked').count()==1 and page.locator('.map-route.alternative').count()==1)
    initial=page.locator('.map-layout').evaluate("el=>getComputedStyle(el).getPropertyValue('--pan-x').trim()")
    page.get_by_role('button',name='Desplazar mapa a la derecha').click()
    after=page.locator('.map-layout').evaluate("el=>getComputedStyle(el).getPropertyValue('--pan-x').trim()")
    check('HU-045 desplazamiento controlado',initial=='0px' and after=='24px')
    page.get_by_role('button',name='Centrar').click()
    check('HU-045 centrar/restablecer plano',page.locator('.map-layout').evaluate("el=>getComputedStyle(el).getPropertyValue('--pan-x').trim()")== '0px')
    page.get_by_role('button',name='Ver riesgo 1: Vidrio').click()
    (Path(__file__).resolve().parents[1]/'docs/evidence').mkdir(parents=True,exist_ok=True)
    page.locator('.map-shell').screenshot(path=str(Path(__file__).resolve().parents[1]/'docs/evidence'/'revision-mapa-movil-390.png'))
    check('HU-045 detalle de segundo riesgo',page.locator('#map-detail-dialog').is_visible() and 'Vidrio de ejemplo' in page.locator('#map-detail-text').inner_text())
    page.locator('#map-detail-close').click()
    page.locator('#app-tabs [data-tab="checklist"]').click()
    page.locator('[data-check="mochila"]').check()
    check('HU-039 aviso tras actualizar checklist','Checklist actualizado' in page.locator('#toast').inner_text())
    check('Navegación/JS — sin excepciones',not failures)
    screenshot_dir=Path(__file__).resolve().parents[1]/'docs/evidence'
    page.locator('#mobile-app-nav [data-tab="inicio"]').click()
    page.screenshot(path=str(screenshot_dir/'revision-movil-390.png'),full_page=True)
    page.close()
    for width in [320,375,400,768,1024,1280,1440,1920]:
        page=browser.new_page(viewport={'width':width,'height':900})
        page.set_default_timeout(5000)
        mount(page)
        check(f'Responsive sin desbordamiento {width}px',page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
        if width==1440:
            page.screenshot(path=str(screenshot_dir/'revision-escritorio-1440.png'),full_page=True)
        page.close()
    browser.close()
print('TOTAL',len(PASS),'comprobaciones propias aprobadas')
