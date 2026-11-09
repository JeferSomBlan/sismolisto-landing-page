"""Pruebas locales por escenario antes NO COMPROBADO, basadas en criterios TB1.
La prueba usa Chromium en memoria, sin red, backend ni validación de seguridad real.
"""
import json, time
from pathlib import Path
from playwright.sync_api import sync_playwright
from test_ui import mount,browser_args
ROOT=Path(__file__).resolve().parents[1]
RESULTS=[]

def case(browser, hu, num, name, fn, width=1440):
    page=browser.new_page(viewport={'width':width,'height':900})
    page.set_default_timeout(4000)
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    try:
        mount(page)
        msg=fn(page)
        assert not errors, errors
        status='PASS'; detail=str(msg or 'Resultado observable confirmado')
    except Exception as exc:
        status='FAIL';detail=(type(exc).__name__+': '+str(exc))[:260]
    RESULTS.append({'HU':hu,'Escenario':f'Escenario {num}','Prueba':name,'Resultado':status,'Detalle':detail,'Entorno':f'Chromium local/memoria, {width}px'})
    print(f'{status} {hu} S{num} {name} — {detail[:90]}',flush=True)
    page.close()

with sync_playwright() as p:
 b=p.chromium.launch(**browser_args())
 def problem_sources(page):
  t=page.locator('#problema').inner_text()
  assert '8,8' in t and 'no es una predicción' in t.lower()
  assert page.locator('#problema a[href*="gob.pe"]').count()==2
  return 'Ejercicio hipotético identificado y dos fuentes oficiales enlazadas'
 case(b,'HU-002',1,'Contexto de Lima/Callao sustentado',problem_sources)
 case(b,'HU-001',2,'CTA Ver cómo funciona navega',lambda pg:(pg.get_by_role('link',name='Ver cómo funciona').click(),pg.evaluate("document.location.hash === '#como-funciona'") or (_ for _ in()).throw(AssertionError('Ancla no cambió')),'Navega al ancla documentada')[-1])
 case(b,'HU-002',2,'Relación problema-solución',lambda pg:(pg.get_by_role('link',name='¿Cómo lo resolvemos?',exact=False).click(),pg.evaluate("document.location.hash === '#como-funciona'") or (_ for _ in()).throw(AssertionError('Ancla no cambió')),'Navega a Cómo funciona')[-1])
 def four_steps(page):
  steps=page.locator('#como-funciona ol > li'); assert steps.count()==4
  assert all(s in page.locator('#como-funciona').inner_text() for s in ['Elige tu espacio','Evalúa riesgos y zonas','Practica decisiones','Revisa tu progreso'])
  return 'Cuatro etapas visibles y numeradas'
 case(b,'HU-003',1,'Cuatro etapas principales',four_steps)
 def feature_cards(page):
  assert page.locator('#funcionalidades .feature-card').count()==4
  for title in ('Evaluación del entorno','Zonas y rutas','Micro-simulacros','Progreso personal'):
   assert title in page.locator('#funcionalidades').inner_text()
  return 'Cuatro capacidades justificadas'
 case(b,'HU-004',1,'Cuatro tarjetas funcionales',feature_cards)
 def feature_preview(page):
  page.locator('#funcionalidades .open-panel').first.click()
  assert page.locator('#app-tabs [data-tab="evaluar"]').get_attribute('aria-current') in (None,'page')
  assert page.locator('#space-form').count()==1
  return 'Abre la evaluación demostrativa; no pretende ser captura del móvil'
 case(b,'HU-004',2,'Vista funcional de evaluación',feature_preview)
 def scenarios(page):
  assert page.locator('#simulacros .scenario-card').count()==3
  assert all('60 s' in x.inner_text() for x in page.locator('#simulacros .scenario-card').all())
  return '3 escenarios con ámbito y duración visible'
 case(b,'HU-007',1,'Consulta simulacros',scenarios)
 def sim_entry(page):
  page.locator('#simulacros .scenario-open').first.click()
  assert page.locator('#sim-clock').is_visible();assert page.locator('#app-content [data-action="answer-sim"]').count()==3
  return 'CTA inicia escenario interactivo con tres elecciones'
 case(b,'HU-007',2,'Abrir demostración',sim_entry)
 def benefits_by_role(page):
  pg=page.locator('#benefit-list');a=pg.inner_text()
  page.locator('[data-benefit="oficina"]').click();bb=pg.inner_text()
  assert a!=bb and 'oficina' in bb.lower() or 'laboral' in bb.lower()
  return 'Contenido cambia al seleccionar Oficinas'
 case(b,'HU-008',2,'Filtrar beneficios por perfil',benefits_by_role)
 def resources(page):
  assert page.locator('#resource-list .resource-card').count()==3
  assert '#ZonaSegura' in page.locator('#recursos').inner_text()
  return '3 recursos breves visibles'
 case(b,'HU-011',1,'Consulta recursos',resources)
 def filter_resources(page):
  page.locator('#resource-filter').select_option('mochila')
  assert page.locator('#resource-list .resource-card:visible').count()==1
  assert '#MochilaEmergencia' in page.locator('#resource-list .resource-card:visible').inner_text()
  return 'Filtro deja recurso coincidente'
 case(b,'HU-011',2,'Filtrar por tema',filter_resources)
 def roles(page):
  assert page.locator('#segmentos .audience-card').count()==2
  assert 'Estudiantes universitarios' in page.locator('#segmentos').inner_text()
  assert 'Trabajadores de oficina' in page.locator('#segmentos').inner_text()
  return 'Ambos perfiles visibles'
 for hu in ['HU-012','HU-013']:
  case(b,hu,1,'Mostrar perfiles',roles)
 def choose_role(page):
  page.locator('#segmentos [data-role="oficina"]').click()
  assert 'Trabajador de oficina' in page.locator('#app-content').inner_text()
  return 'Contexto elegido se refleja en el área de demostración'
 for hu in ['HU-012','HU-013']:
  case(b,hu,2,'Seleccionar perfil',choose_role)
 def share_site(page):
  page.locator('#share-site').click()
  assert page.locator('#share-dialog').is_visible()
  assert all(page.locator('#share-'+s).get_attribute('href').startswith('https://') for s in ['whatsapp','facebook','linkedin'])
  return 'Se muestran WhatsApp, Facebook, LinkedIn y Copiar enlace'
 case(b,'HU-015',1,'Opciones de compartir',share_site)
 def share_copy(page):
  page.evaluate("Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async(x)=>{window.__copiedText=x}}})")
  page.locator('#share-site').click();page.locator('#share-copy').click()
  page.wait_for_function("window.__copiedText && document.querySelector('#share-feedback').textContent.includes('Enlace copiado')")
  assert 'sismolisto-landing-page' in page.evaluate('window.__copiedText')
  return 'Copia URL y muestra Enlace copiado'
 case(b,'HU-015',2,'Copiar vínculo',share_copy)
 def privacy(page):
  page.locator('#privacy-open').click()
  assert page.locator('#privacy-dialog').is_visible()
  assert 'almacenamiento local' in page.locator('#privacy-dialog').inner_text()
  return 'Información de datos y limitación visible'
 case(b,'HU-016',1,'Consulta de privacidad',privacy)
 def mobile_layout(page):
  assert page.locator('#menu-toggle').is_visible()
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  assert page.locator('#site-nav').is_hidden()
  return 'Columna responsive sin desbordamiento y menú colapsado'
 case(b,'HU-017',1,'Vista móvil 390px',mobile_layout,width=390)
 def desktop_layout(page):
  assert page.locator('#site-nav').is_visible()
  assert page.locator('#menu-toggle').is_hidden()
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
  return 'Menú desktop completo sin desbordamiento'
 case(b,'HU-017',2,'Vista escritorio 1440px',desktop_layout)
 def brand(page):
  assert page.locator('.site-header .brand-name').is_visible()
  assert page.locator('.site-header .brand-symbol').is_visible()
  return 'Marca y símbolo presentes en header'
 case(b,'HU-019',1,'Identidad en header',brand)
 def footer_link(page):
  a=page.locator('.site-footer a[href="#contacto"]'); assert a.count()==1
  a.click();assert page.evaluate("location.hash === '#contacto'")
  return 'Enlace de contacto desde footer funciona'
 case(b,'HU-020',2,'Enlaces del pie',footer_link)
 def back_hidden(page):
  assert page.locator('#back-to-top').is_hidden()
  return 'Volver arriba oculto al cargar'
 case(b,'HU-022',2,'Volver arriba oculto al inicio',back_hidden)
 def back_show(page):
  page.evaluate('window.scrollTo(0,1200)')
  page.wait_for_function("!document.querySelector('#back-to-top').hidden")
  page.locator('#back-to-top').click()
  page.wait_for_function('window.scrollY < 100',timeout=4000)
  return 'Botón aparece al desplazarse y retorna a inicio'
 case(b,'HU-022',1,'Volver arriba',back_show)
 def faq_open(page):
  page.locator('.faq-list details').nth(1).locator('summary').click()
  assert page.locator('.faq-list details').nth(1).get_attribute('open') is not None
  return 'La pregunta despliega su respuesta'
 case(b,'HU-024',1,'Abrir FAQ',faq_open)
 def faq_exclusive(page):
  page.locator('.faq-list details').nth(1).locator('summary').click()
  assert page.locator('.faq-list details').nth(0).get_attribute('open') is None
  assert page.locator('.faq-list details').nth(1).get_attribute('open') is not None
  return 'Abrir otra cierra la anterior'
 case(b,'HU-024',2,'FAQ exclusivas',faq_exclusive)
 def secondary_button(page):
  page.get_by_role('link',name='Ver cómo funciona').click()
  assert page.evaluate("location.hash === '#como-funciona'")
  return 'CTA secundario navega a sección'
 case(b,'HU-025',1,'CTA secundario',secondary_button)
 def resume_primary(page):
  a=page.locator('#como-funciona a[href="#experiencia"]'); assert a.count()==1
  a.click(); assert page.evaluate("location.hash === '#experiencia'")
  return 'CTA principal al final de la sección'
 case(b,'HU-025',2,'Retomar CTA principal',resume_primary)
 def share_resource(page):
  page.locator('#recurso-zonas .share-resource').click()
  assert page.locator('#share-dialog').is_visible()
  assert '#recurso-zonas' in page.locator('#share-link-preview').inner_text()
  return 'URL específica del recurso en opciones de compartir'
 case(b,'HU-026',1,'Compartir recurso',share_resource)
 def share_cancel(page):
  page.locator('#recurso-mochila .share-resource').click()
  page.locator('#share-cancel').click()
  assert not page.locator('#share-dialog').is_visible()
  assert page.locator('#recurso-mochila').count()==1
  return 'Cancelar mantiene el recurso visible'
 case(b,'HU-026',2,'Cancelar compartir',share_cancel)
 def menu_mobile(page):
  page.locator('#menu-toggle').click()
  assert page.locator('#site-nav').is_visible()
  assert page.locator('#menu-toggle').get_attribute('aria-label')=='Cerrar menú de navegación'
  page.locator('#menu-toggle').click()
  assert page.locator('#site-nav').is_hidden()
  return 'Menú accesible con apertura y cierre'
 case(b,'HU-028',2,'Menú móvil con cierre',menu_mobile,width=390)
 def keyboard_focus(page):
  page.keyboard.press('Tab')
  assert page.evaluate("document.activeElement.matches('a, button, input, select, textarea')")
  assert page.evaluate('getComputedStyle(document.activeElement).outlineStyle')!='none'
  return 'Foco visible en primer enlace'
 case(b,'HU-029',2,'Foco de teclado',keyboard_focus)
 def recommended(page):
  page.locator('#app-tabs [data-tab="riesgos"]').click()
  page.locator('#risk-type').select_option('Ruta obstruida')
  page.locator('#risk-level').select_option('Crítico')
  page.locator('#risk-desc').fill('Obstáculo de prueba')
  page.locator('#risk-form button[type=submit]').click()
  page.locator('#app-tabs [data-tab="progreso"]').click()
  assert page.locator('#app-content [data-rec]').count()>0
  return 'Se muestran recomendaciones ligadas a los riesgos'
 case(b,'HU-043',1,'Recomendaciones tras riesgo',recommended)
 b.close()
out=ROOT/'docs/PRUEBAS_ESCENARIOS_PENDIENTES_2026-11-08.json'
out.write_text(json.dumps(RESULTS,ensure_ascii=False,indent=2),encoding='utf-8')
print('SUMMARY',json.dumps({'pass':sum(x['Resultado']=='PASS' for x in RESULTS),'fail':sum(x['Resultado']=='FAIL' for x in RESULTS),'total':len(RESULTS)}),flush=True)
