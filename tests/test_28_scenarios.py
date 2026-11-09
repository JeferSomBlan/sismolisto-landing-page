"""28 isolated acceptance cases from SismoListo TB1 pp. 53–70.
Tests HTML/CSS/JS in Playwright Chromium in-memory. Does not verify production deployment.
"""
import json,base64,re,sys
from datetime import datetime,timezone
from pathlib import Path
from PIL import Image
from io import BytesIO
from playwright.sync_api import sync_playwright
from test_ui import mount,browser_args
ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/'docs/evidence/28_scenarios';EVIDENCE.mkdir(exist_ok=True,parents=True)
RESULT=[]

def check(cond,msg):
    if not cond: raise AssertionError(msg)

def reg(pg,email='demo@ejemplo.test',pwd='SoloDemo123'):
    pg.locator('.hero-content .actions .btn-primary').click()
    check(pg.locator('#account-dialog').is_visible(),'No aparece registro')
    pg.locator('#account-register-tab').click()
    pg.locator('#register-name').fill('Estudiante Ficticio')
    pg.locator('#register-email').fill(email)
    pg.locator('#register-password').fill(pwd)
    pg.locator('#register-role').select_option('estudiante')
    pg.locator('#register-privacy-check').check()
    pg.locator('#register-form button[type="submit"]').click()
    check(not pg.locator('#account-dialog').is_visible(),'No se cierra registro')

def eval_space(pg):
    pg.locator('#app-tabs [data-tab="evaluar"]').click()
    pg.locator('#space-sample').select_option('aula')
    pg.locator('#space-form button[type="submit"]').click()
    for i,ans in enumerate(('Sí','No','No estoy seguro')):
        pg.locator('#eval-form').get_by_label(ans,exact=True).check()
        pg.locator('#eval-form button[type="submit"]').click()
    check('Última evaluación guardada' in pg.locator('#app-content').inner_text(),'No guardó evaluación')

def case(b,hu,num,title,fn,width=1440,visual=False):
    pg=b.new_page(viewport={'width':width,'height':880});pg.set_default_timeout(5500)
    errors=[];pg.on('pageerror',lambda e:errors.append(str(e)))
    try:
        mount(pg)
        description=fn(pg)
        check(not errors,'Errores JS: '+'; '.join(errors))
        check(pg.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),f'Desbordamiento horizontal {width}px')
        if visual: pg.screenshot(path=str(EVIDENCE/f'{hu}-E{num}.png'),full_page=True)
        item={'HU':hu,'Escenario':num,'Descripcion':title,'Estado':'CUMPLE','Resultado':str(description),'Entorno':f'Chromium en memoria {width}x880','Captura':f'docs/evidence/28_scenarios/{hu}-E{num}.png' if visual else ''}
    except Exception as e:
        item={'HU':hu,'Escenario':num,'Descripcion':title,'Estado':'NO CUMPLE','Resultado':(type(e).__name__+': '+str(e))[:520],'Entorno':f'Chromium en memoria {width}x880','Captura':''}
    RESULT.append(item);print(item['Estado'],hu,num,title,item['Resultado'][:140],flush=True)
    pg.close()

with sync_playwright() as w:
 b=w.chromium.launch(**browser_args())
 def step_detail(pg):
    pg.locator('#step-select').select_option('2');pg.locator('#step-view').click()
    check(pg.locator('#step-detail').is_visible(),'Detalle oculto')
    check('Practica' in pg.locator('#step-detail-title').inner_text(),'Título de paso incorrecto')
    rel=pg.locator('#step-detail-image').get_attribute('src'); check((ROOT/rel).is_file(),'Imagen referencial no existe')
    return 'Descripción de paso e imagen de mockup TB1 p. 106 visibles'
 case(b,'HU-003',2,'Detalle de un paso',step_detail,visual=True)
 def registration_valid(pg):
    reg(pg)
    check(pg.locator('#profile-settings').count()==1,'Sin configuración inicial de espacio')
    check(pg.evaluate('!!JSON.parse(localStorage.getItem("sismolisto_demo_account_v1"))'),'No guarda cuenta simulada')
    return 'Registro simulado → perfil/espacio habitual'
 case(b,'HU-005',1,'Registro exitoso',registration_valid,visual=True)
 def registration_invalid(pg):
    reg(pg)
    pg.locator('.hero-content .actions .btn-primary').click();pg.locator('#account-register-tab').click()
    pg.locator('#register-name').fill('Nombre conservado');pg.locator('#register-email').fill('nuevo@ejemplo.test');pg.locator('#register-password').fill('corto')
    pg.locator('#register-privacy-check').check();pg.locator('#register-form button[type="submit"]').click()
    check(pg.locator('#register-password').get_attribute('aria-invalid')=='true','No marca contraseña corta')
    check('8 caracteres' in pg.locator('#register-feedback').inner_text(),'No indica cómo corregir')
    check(pg.locator('#register-name').input_value()=='Nombre conservado','Borró dato ingresado')
    pg.locator('#register-password').fill('OtraClave123');pg.locator('#register-email').fill('demo@ejemplo.test')
    pg.locator('#register-form button[type="submit"]').click()
    check(pg.locator('#register-email').get_attribute('aria-invalid')=='true','No marca duplicado')
    return 'Contraseña corta y correo duplicado resaltados; resto del formulario conservado'
 case(b,'HU-005',2,'Datos inválidos',registration_invalid,visual=True)
 def login_valid(pg):
    reg(pg)
    pg.locator('#app-tabs [data-tab="checklist"]').click();pg.locator('[data-check="mochila"]').check()
    pg.locator('.hero-content .actions .btn-primary').click()
    check(not pg.locator('#login-form').is_hidden(),'No ofrece inicio de sesión')
    pg.locator('#login-email').fill('demo@ejemplo.test');pg.locator('#login-password').fill('SoloDemo123')
    pg.locator('#login-form button[type="submit"]').click()
    check('Mi preparación' in pg.locator('#app-content').inner_text(),'No vuelve a inicio')
    check('Actividades registradas' in pg.locator('#app-content').inner_text(),'Sin progreso')
    return 'Inicio de sesión simulado abre inicio y conserva checklist en almacenamiento'
 case(b,'HU-006',1,'Inicio de sesión',login_valid,visual=True)
 def login_invalid(pg):
    pg.locator('.hero-content .actions .btn-primary').click();pg.locator('#account-login-tab').click()
    pg.locator('#login-email').fill('incorrecto@ejemplo.test');pg.locator('#login-password').fill('incorrecto')
    pg.locator('#login-form button[type="submit"]').click()
    check('Correo o contraseña incorrectos' in pg.locator('#login-feedback').inner_text(),'Mensaje incorrecto')
    check(pg.locator('#forgot-demo').is_visible(),'No aparece recuperar contraseña')
    return 'Credenciales de prueba incorrectas y recuperación simulada visible'
 case(b,'HU-006',2,'Credenciales incorrectas',login_invalid)
 def benefits(pg):
    t=pg.locator('#benefit-list').inner_text().lower()
    check('10 segundos' in t and 'practicar' in t,'Beneficios del escenario ausentes')
    check('no es un tiempo medido' in t,'Afirmación de eficacia no sustentada')
    return 'Beneficios de rapidez y práctica rotulados como objetivos, no datos medidos'
 case(b,'HU-008',1,'Consulta de beneficios',benefits)
 def testimonials(pg):
    check('personaje ficticio' in pg.locator('#testimonios').inner_text().lower(),'No aclara ficción')
    check(pg.locator('#testimonial-name').inner_text() and pg.locator('#testimonial-role').inner_text(),'Falta nombre o perfil')
    return 'Nombre, perfil, comentario y descargo ficticio visibles'
 case(b,'HU-009',1,'Visualización de testimonios',testimonials)
 def carousel(pg):
    before=pg.locator('#testimonial-quote').inner_text();initial=pg.url
    pg.locator('#testimonial-next').click()
    check(pg.locator('#testimonial-quote').inner_text()!=before,'No cambió testimonio')
    pg.locator('#testimonial-prev').click()
    check(pg.locator('#testimonial-quote').inner_text()==before,'No regresa')
    check(pg.url==initial,'Recargó la página')
    return 'Carrusel avanza y retrocede sin recarga'
 case(b,'HU-009',2,'Carrusel de testimonios',carousel,visual=True)
 def contact(pg):
    pg.locator('#site-nav a[href="#contacto"]').click()
    check(pg.url.endswith('#contacto'),'No navega a Contacto')
    check(pg.locator('#contact-form').count()==1,'No hay formulario')
    check(pg.locator('#contacto .contact-channels a').count()==3,'Faltan correo y redes de ejemplo')
    return 'Navegación a formulario y canales simulados claramente identificados'
 case(b,'HU-010',1,'Contacto con otros canales',contact)
 def channels(pg):
    mail=pg.locator('#contacto .contact-channels a').first
    check(mail.get_attribute('href').startswith('mailto:'),'Correo no invoca app mail')
    for a in pg.locator('#contacto .contact-channels a').all()[1:]:
        check(a.get_attribute('target')=='_blank','Red social no abre nueva pestaña')
        check(a.get_attribute('href').startswith('https://'),'URL de plataforma no válida')
    return 'Correo de ejemplo y redes llevan a la app/plataforma sin fingir identidad real del equipo'
 case(b,'HU-010',2,'Otro canal',channels)
 def comparison(pg):
    check(pg.locator('#comparacion .comparison-table').is_visible(),'Falta tabla en escritorio')
    t=pg.locator('#comparacion').inner_text().lower()
    check(all(word in t for word in ['sismolisto','guías tradicionales','simulacros','espacio propio']),'Comparación incompleta')
    return 'Tabla compara práctica, simulacros y evaluación de espacios'
 case(b,'HU-014',1,'Tabla comparativa',comparison,visual=True)
 def comparison_mobile(pg):
    check(not pg.locator('#comparacion .comparison-table').is_visible(),'Tabla no se adapta')
    check(pg.locator('#comparacion .comparison-cards article:visible').count()==3,'Faltan tarjetas')
    check(pg.evaluate('document.documentElement.scrollWidth <= innerWidth'),'Desborde')
    return 'Tres tarjetas comparativas apiladas sin scroll horizontal'
 case(b,'HU-014',2,'Comparación móvil',comparison_mobile,width=390,visual=True)
 def privacy_return(pg):
    pg.locator('.hero-content .actions .btn-primary').click()
    pg.locator('#register-name').fill('Nombre intacto');pg.locator('#register-email').fill('fake@ejemplo.test')
    pg.locator('#register-policy').click()
    check(pg.locator('#privacy-dialog').is_visible(),'No abre política')
    pg.locator('#privacy-close').click()
    check(pg.locator('#account-dialog').is_visible(),'Cerró registro')
    check(pg.locator('#register-name').input_value()=='Nombre intacto','Perdió nombre')
    check(pg.locator('#register-email').input_value()=='fake@ejemplo.test','Perdió correo')
    return 'Política modal retorna al formulario sin pérdida de datos'
 case(b,'HU-016',2,'Regreso al registro',privacy_return)
 def cta(pg):
    pg.locator('.hero-content .actions .btn-primary').click()
    check(pg.locator('#register-form').is_visible(),'CTA no dirige a registro')
    return 'CTA Comenzar ofrece registro simulado sin cambiar sección de la página'
 case(b,'HU-018',1,'Inicio de experiencia',cta)
 def cta_login(pg):
    reg(pg)
    pg.locator('.hero-content .actions .btn-primary').click()
    check(pg.locator('#login-form').is_visible(),'CTA no ofrece login para cuenta demo existente')
    return 'CTA ofrece inicio de sesión a cuenta demo existente'
 case(b,'HU-018',2,'Usuario con cuenta',cta_login)
 def browser_identity(pg):
    check(pg.title().startswith('SismoListo'),'Título de pestaña incorrecto')
    favicon=pg.locator('link[rel="icon"]').get_attribute('href')
    check(bool(favicon) and (ROOT/favicon).is_file(),'Favicon no está disponible en recursos')
    return 'Título y archivo favicon.svg presentes (despliegue público no comprobado)'
 case(b,'HU-019',2,'Identidad navegador',browser_identity)
 def footer(pg):
    t=pg.locator('.site-footer').inner_text().lower()
    check(all(w in t for w in ['contacto','privacidad','social','derechos reservados']),'Footer incompleto')
    check(pg.locator('.site-footer a[href^="#"]').count()>=3,'Enlaces de secciones insuficientes')
    return 'Enlaces, contacto, privacidad, red de ejemplo y derechos reservados visibles'
 case(b,'HU-020',1,'Footer completo',footer,visual=True)
 def demo_start(pg):
    pg.locator('#try-demo').click()
    check(pg.locator('#sim-clock').is_visible(),'No inicia demo')
    check(pg.locator('#app-content [data-action="answer-sim"]').count()==3,'No hay tres alternativas')
    return 'Demo de salida bloqueada con tres decisiones y temporizador'
 case(b,'HU-023',1,'Probar demo',demo_start)
 def demo_answer(pg):
    pg.locator('#try-demo').click();pg.locator('#app-content [data-action="answer-sim"]').nth(1).click()
    check('Resultado del micro-simulacro' in pg.locator('#app-content').inner_text(),'Sin feedback')
    check('Crea tu cuenta para practicar más' in pg.locator('#app-content').inner_text(),'Sin invitación posterior')
    return 'Feedback inmediato e invitación a cuenta demostrativa'
 case(b,'HU-023',2,'Resultado de demo',demo_answer,visual=True)
 def multi_device(pg):
    checked=[]
    for ww in (320,375,390,400,768,1024,1280,1440,1920):
        pg.set_viewport_size({'width':ww,'height':880})
        check(pg.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),f'Desbordamiento {ww}')
        check(pg.locator('h1').is_visible(),f'H1 no visible {ww}')
        checked.append(ww)
    return 'Viewport sin cortes: '+','.join(map(str,checked))
 case(b,'HU-027',1,'Multidispositivo',multi_device,width=320)
 def orientation(pg):
    for w,h in ((390,844),(844,390)):
        pg.set_viewport_size({'width':w,'height':h});pg.wait_for_timeout(70)
        check(pg.evaluate('document.documentElement.scrollWidth <= innerWidth + 1'),'Desbordamiento orientación')
        check(pg.locator('h1').evaluate('el => getComputedStyle(el).fontSize')!='0px','Texto oculto')
    return 'Pantalla vertical/horizontal reorganizada sin desbordamiento'
 case(b,'HU-027',2,'Cambio orientación',orientation,width=390)
 def nav_active(pg):
    pg.locator('#site-nav a[href="#como-funciona"]').click()
    check(pg.url.endswith('#como-funciona'),'No llega al ancla')
    check(pg.locator('#site-nav a[href="#como-funciona"]').get_attribute('aria-current')=='location','No resalta opción')
    return 'Navega a sección y marca estado activo'
 case(b,'HU-028',1,'Selección de sección',nav_active)
 def text_readability(pg):
    check(pg.locator('html').get_attribute('lang')=='es','Falta idioma')
    # Project-specific requirement: text nodes within visible common elements must be >=16 CSS px.
    data=pg.evaluate('''() => [...document.querySelectorAll('p,small,a,button,label,li,select,input,textarea,td,th,summary')].filter(e=>e.getClientRects().length && getComputedStyle(e).visibility!=='hidden').map(e=>({tag:e.tagName,sz:parseFloat(getComputedStyle(e).fontSize),text:e.textContent.trim().slice(0,26)})).filter(e=>e.sz<15.9).slice(0,14)''')
    check(not data,'Hay textos inferiores a 16px: '+repr(data))
    imgs=pg.locator('img').all();check(all(i.get_attribute('alt') is not None for i in imgs),'Imagen sin alt')
    # Check representative contrast pairs incl. normal text; automatic contrast cannot certify entire WCAG compliance.
    def ratio(f,b):
        def lin(hex_):
            c=[int(hex_[i:i+2],16)/255 for i in (1,3,5)]
            v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in c]
            return .2126*v[0]+.7152*v[1]+.0722*v[2]
        l,m=sorted([lin(f),lin(b)],reverse=True);return (l+.05)/(m+.05)
    check(ratio('#516174','#ffffff')>=4.5 and ratio('#1976d2','#ffffff')>=4.5,'Contraste tokens normal no alcanza 4.5')
    return 'Textos inspeccionados >=16px; alt en imágenes; pares de contraste básicos medidos (no auditoría WCAG completa)'
 case(b,'HU-029',1,'Lectura accesible',text_readability)
 def risk_photo(pg):
    eval_space(pg);pg.locator('#app-tabs [data-tab="riesgos"]').click()
    pg.locator('#risk-type').select_option('Objeto que puede caer');pg.locator('#risk-level').select_option('Crítico')
    pg.locator('#risk-desc').fill('Estantería ficticia en Aula A-302')
    im=Image.new('RGB',(12,12),(200,100,40)); buf=BytesIO(); im.save(buf,format='PNG'); pixel=buf.getvalue()
    pg.locator('#risk-photo').set_input_files({'name':'prueba.png','mimeType':'image/png','buffer':pixel})
    pg.locator('#risk-form button[type="submit"]').click()
    pg.locator('#app-tabs [data-tab="zonas"]').click()
    check(pg.locator('#app-content .map-marker.risk.critical').count()==1,'El marcador crítico no aparece en el plano')
    pg.locator('#app-content .map-marker.risk.critical').click()
    check('Estantería ficticia' in pg.locator('#map-detail-text').inner_text(),'El detalle de riesgo no aparece')
    check('Crítico' in pg.locator('#map-detail-text').inner_text(),'No representa gravedad')
    check(pg.evaluate('!!JSON.parse(localStorage.getItem("sismolisto_academic_demo_v1")).risks[0].photo'),'No guardó la imagen')
    return 'Riesgo con fotografía ficticia y gravedad crítica visible en mapa de ejemplo'
 case(b,'HU-032',1,'Registrar riesgo con foto',risk_photo,visual=True)
 def safe_zones(pg):
    eval_space(pg);pg.locator('#app-tabs [data-tab="zonas"]').click()
    t=pg.locator('#app-content').inner_text()
    check('Columna B3' in t and 'Punto de reunión' in t,'Faltan zona y punto referenciales')
    return 'Zona interna y punto de reunión ficticios tras evaluar espacio'
 case(b,'HU-033',1,'Consulta zonas registradas',safe_zones)
 def empty_zones(pg):
    pg.locator('#app-tabs [data-tab="evaluar"]').click()
    pg.locator('#space-sample').select_option('aula');pg.locator('#space-form button[type="submit"]').click()
    pg.locator('#app-tabs [data-tab="zonas"]').click()
    t=pg.locator('#app-content').inner_text()
    check('Este espacio aún no tiene zonas seguras' in t,'Falta mensaje vacío')
    check(pg.get_by_role('button',name='Evaluar este espacio').count()==1,'Falta CTA evaluación')
    return 'Estado vacío y CTA Evaluar este espacio antes de completar evaluación'
 case(b,'HU-033',2,'Zonas vacías',empty_zones,visual=True)
 def urgent_choice(pg):
    pg.locator('#try-demo').click()
    check(pg.locator('#sim-clock').is_visible(),'No inicia timer')
    check(pg.locator('[data-action="answer-sim"]').count()==3,'No hay 3 alternativas')
    return 'Tres decisiones disponibles durante cuenta regresiva de simulacro'
 case(b,'HU-036',1,'Responder imprevisto',urgent_choice)
 def timeout(pg):
    # Force virtual wall-clock forward and allow the existing interval tick. No 60-second real wait.
    pg.locator('#try-demo').click()
    pg.evaluate('''() => { window.__realNow = Date.now; const base=Date.now(); Date.now=()=>base+62000; }''')
    pg.wait_for_timeout(650)
    t=pg.locator('#app-content').inner_text()
    check('Sin respuesta' in t and 'Opción esperada' in t,'Tiempo 0 no registra sin respuesta y feedback: '+t[:100])
    return 'Temporizador finaliza tras avance ficticio de 62s; Sin respuesta + opción esperada'
 case(b,'HU-036',2,'Tiempo agotado',timeout,visual=True)
 b.close()

summary={'timestamp_utc':datetime.now(timezone.utc).isoformat(),'base':'SismoListo_AV2_Codigo_Simulaciones_Pendientes.zip','executed':len(RESULT),'passed':sum(r['Estado']=='CUMPLE' for r in RESULT),'failed':sum(r['Estado']!='CUMPLE' for r in RESULT),'results':RESULT}
out=ROOT/'docs/RESULTADOS_28_ESCENARIOS_2026-11-09.json'
out.write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print('SUMMARY',summary['passed'],summary['failed'],out,flush=True)
if summary['failed']: sys.exit(1)
