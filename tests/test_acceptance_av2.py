"""Pruebas dirigidas a correcciones AV2: no certifican los 100 criterios del TB1.
Browser: Chromium aislado, documento HTML/CSS/JS real cargado en memoria;
no se interpreta como prueba de URL pública o de servidor.
"""
from test_ui import sync_playwright,mount,browser_args

checks=[]
def ok(name,cond):
    assert cond, f'FALLO: {name}'
    checks.append(name)

def evaluate(page):
    page.locator('[data-tab="evaluar"]').click()
    page.locator('#space-sample').select_option('aula')
    page.locator('#space-form button[type="submit"]').click()
    for idx in range(3):
        page.locator('#eval-form input[value="No"]').check()
        page.locator('#eval-form button[type="submit"]').click()

def add_block(page):
    page.locator('[data-tab="riesgos"]').click()
    page.locator('#risk-type').select_option('Ruta obstruida')
    page.locator('#risk-level').select_option('Crítico')
    page.locator('#risk-desc').fill('Pasillo bloqueado de ejemplo')
    page.locator('#risk-form button[type="submit"]').click()

with sync_playwright() as p:
    browser=p.chromium.launch(**browser_args())
    page=browser.new_page(viewport={'width':390,'height':844})
    errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
    mount(page)
    page.locator('[data-tab="progreso"]').click()
    ok('HU-050 S2 — estado inicial 0% y CTA',page.locator('#app-content').get_by_text('0 %',exact=True).count()>0 and page.locator('#app-content').get_by_role('button',name='Empieza tu primera evaluación').count()>0)
    page.locator('#app-content').get_by_role('button',name='Empieza tu primera evaluación').click()
    ok('HU-050 S2 — CTA abre evaluación',page.locator('#space-form').count()==1)
    evaluate(page)
    page.locator('[data-tab="progreso"]').click()
    ok('HU-050 S1 — resumen por categorías',all(x in page.locator('#app-content').inner_text() for x in ('Entorno','Simulacros','Checklist')))
    ok('HU-039 S1 — porcentaje recalculado al evaluar',int(page.locator('.mini-metric').first.inner_text().replace('%',''))>0)
    add_block(page)
    page.locator('[data-tab="zonas"]').click()
    ok('HU-034 S2 — marcador y alternativa de demostración',page.locator('.map-route.blocked').count()==1 and page.locator('.map-route.alternative').count()==1 and '3 minutos' in page.locator('#app-content').inner_text())
    page.locator('.map-marker.zone').click()
    ok('HU-045 S1 — detalle en diálogo accesible',page.locator('#map-detail-dialog').is_visible() and 'Columna B3' in page.locator('#map-detail-text').inner_text())
    page.locator('#map-detail-close').click()
    ok('HU-045 S1 — cerrar detalle retorna al mapa',not page.locator('#map-detail-dialog').is_visible() and page.locator('.map-shell').is_visible())
    page.locator('[data-tab="progreso"]').click()
    before=int(page.locator('.mini-metric').first.inner_text().replace('%',''))
    page.locator('[data-rec]').first.check()
    after=int(page.locator('.mini-metric').first.inner_text().replace('%',''))
    ok('HU-043 S2 — recomendación Hecho aumenta avance',after>before and 'Hecho' in page.locator('#app-content').inner_text())
    page.locator('[data-tab="riesgos"]').click()
    page.get_by_role('button',name='Eliminar').click()
    ok('HU-047 S1 — confirmación Cancelar/Eliminar',page.locator('#confirm-dialog').is_visible() and page.locator('#confirm-cancel').is_visible() and page.locator('#confirm-execute').inner_text()=='Eliminar')
    page.locator('#confirm-cancel').click()
    ok('HU-047 S1 — cancelar conserva registro', 'Pasillo bloqueado de ejemplo' in page.locator('#app-content').inner_text())
    page.get_by_role('button',name='Eliminar').click();page.locator('#confirm-execute').click()
    ok('HU-047 S2 — se permite Deshacer',page.get_by_role('button',name='Deshacer').count()>0)
    page.locator('[data-tab="progreso"]').click()
    page.get_by_role('button',name='Finalizar',exact=True).click()
    ok('HU-049 S2 — diálogo de pasos pendientes',page.locator('#session-pending-dialog').is_visible() and 'completar un micro-simulacro' in page.locator('#session-pending-list').inner_text())
    page.locator('#session-pending-finish').click()
    ok('HU-049 S1/S2 — resumen persistente en pantalla',page.locator('#session-summary').count()==1 and 'pasos pendientes' in page.locator('#session-summary').inner_text())
    ok('JS runtime — sin errores en pruebas dirigidas',not errors)
    browser.close()
for c in checks:print('PASS',c)
print('TOTAL',len(checks),'pruebas AV2 dirigidas satisfactorias')
