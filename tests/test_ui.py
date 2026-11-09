"""Local Playwright smoke tests. Uses in-memory document due sandbox URL restrictions."""
from pathlib import Path
import shutil
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
HTML=(ROOT/'index.html').read_text(encoding='utf-8')
# Playwright in-memory harness cannot fetch external Google Fonts; omit ONLY remote font stylesheet during tests.
import re as _re
HTML=_re.sub(r'<link href="https://fonts\.googleapis\.com/[^>]+>','',HTML)
CSS='\n'.join((ROOT/rel).read_text(encoding='utf-8') for rel in __import__('re').findall(r'href=\"(css/[^\"]+\.css)\"', HTML))
JS=(ROOT/'js/app.js').read_text(encoding='utf-8')+'\n'+(ROOT/'js/acceptance.js').read_text(encoding='utf-8')
import base64
logo=ROOT/'assets/images/brand/logo-sismolisto-captura-tb1.png'
HTML=HTML.replace('assets/images/brand/logo-sismolisto-captura-tb1.png', 'data:image/png;base64,'+base64.b64encode(logo.read_bytes()).decode())
qr=ROOT/'assets/images/illustrations/qr-sismolisto-demo.png'
HTML=HTML.replace('assets/images/illustrations/qr-sismolisto-demo.png','data:image/png;base64,'+base64.b64encode(qr.read_bytes()).decode())

def mount(page):
    # The evaluation environment blocks all browser navigation (including localhost/file URLs).
    # Test the exact HTML/CSS/JS through an in-memory document with localStorage shim.
    page.evaluate("""Object.defineProperty(window,'localStorage',{configurable:true,value:{
        __data:{},getItem(k){return this.__data[k]??null},setItem(k,v){this.__data[k]=String(v)},removeItem(k){delete this.__data[k]}
    }})""")
    page.set_content(HTML, wait_until="domcontentloaded", timeout=15000)
    page.add_style_tag(content=CSS)
    page.add_script_tag(content=JS)

def browser_args():
    exe=shutil.which('chromium') or shutil.which('google-chrome')
    return {'executable_path':exe,'headless':True,'args':['--no-sandbox']} if exe else {'headless':True}

def run():
    results=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(**browser_args())
        for width,height in [(1440,900),(768,900),(390,844),(320,780)]:
            page=browser.new_page(viewport={'width':width,'height':height})
            errors=[]
            page.on('pageerror',lambda exc:errors.append(str(exc)))
            mount(page)
            assert page.get_by_role('heading',name='Prepárate hoy. Actúa con más claridad.').count()==1
            assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),f'Horizontal overflow at {width}px'
            assert not errors,errors
            results.append(f'Responsive {width}x{height}: PASS')
            if width in (1440,390):
                out=ROOT.parent/'evidence'
                out.mkdir(exist_ok=True)
                page.screenshot(path=str(out/f'landing-{width}.png'),full_page=True)
            page.close()
        page=browser.new_page(viewport={'width':1440,'height':900})
        errors=[]
        page.on('pageerror',lambda exc:errors.append(str(exc)))
        mount(page)
        page.get_by_role('button',name='Evaluar espacio',exact=True).first.click()
        page.locator('#space-sample').select_option('aula')
        page.locator('#space-form').get_by_role('button',name='Iniciar evaluación').click()
        for answer in ['Sí','No','No estoy seguro']:
            page.locator('#eval-form').get_by_label(answer,exact=True).check()
            page.locator('#eval-form').get_by_role('button',name='Siguiente' if answer!='No estoy seguro' else 'Finalizar evaluación').click()
        assert 'Última evaluación guardada' in page.locator('#app-content').inner_text()
        results.append('HU-031 evaluación 3 pasos: PASS')
        page.locator('#app-tabs [data-tab="riesgos"]').click()
        page.locator('#risk-type').select_option('Ruta obstruida')
        page.locator('#risk-level').select_option('Crítico')
        page.locator('#risk-desc').fill('Obstáculo de demostración en pasillo')
        page.locator('#risk-form').get_by_role('button',name='Guardar riesgo').click()
        assert 'Obstáculo de demostración en pasillo' in page.locator('#app-content').inner_text()
        results.append('HU-032 riesgo sin fotografía: PASS')
        page.locator('#app-tabs [data-tab="zonas"]').click()
        assert 'Ruta principal bloqueada (simulación)' in page.locator('#app-content').inner_text()
        results.append('HU-034 ruta bloqueada simulada: PASS')
        page.locator('#app-tabs [data-tab="practica"]').click()
        page.locator('[data-scenario="blocked"]').last.click()
        assert '60 s' in page.locator('#sim-clock').inner_text()
        page.locator('[data-action="answer-sim"][data-choice="1"]').click()
        assert 'Resultado del micro-simulacro' in page.locator('#app-content').inner_text()
        results.append('HU-035–037 simulación/feedback: PASS')
        page.locator('#app-tabs [data-tab="checklist"]').click()
        page.locator('[data-check="mochila"]').check()
        assert '33 % completado' in page.locator('#app-content').inner_text()
        results.append('HU-038 checklist: PASS')
        page.locator('#app-tabs [data-tab="progreso"]').click()
        assert 'Simulacro' in page.locator('#app-content').inner_text()
        results.append('HU-040 historial: PASS')
        # Persistence is proved by retaining the in-memory localStorage shim while re-mounting.
        stored=page.evaluate('localStorage.__data')
        page.set_content(HTML, wait_until="domcontentloaded", timeout=15000)
        page.add_style_tag(content=CSS)
        page.add_script_tag(content=JS)
        page.locator('#app-tabs [data-tab="progreso"]').click()
        assert 'Simulacro' in page.locator('#app-content').inner_text()
        results.append('Persistencia local al recargar documento: PASS')
        assert not errors,errors
        out=ROOT.parent/'evidence';out.mkdir(exist_ok=True)
        page.screenshot(path=str(out/'landing-experience.png'),full_page=True)
        browser.close()
    print('\n'.join(results))
    print('TOTAL:',len(results),'PASS')

if __name__=='__main__': run()
