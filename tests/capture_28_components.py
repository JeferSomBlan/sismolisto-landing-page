"""Screenshots from the mounted HTML/CSS/JS; assets resolved locally for visual evidence."""
import base64
from pathlib import Path
from playwright.sync_api import sync_playwright
from test_ui import mount,browser_args
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs/evidence/28_scenarios';OUT.mkdir(parents=True,exist_ok=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(**browser_args())
 page=b.new_page(viewport={'width':1440,'height':850});mount(page)
 page.locator('.hero-content .actions .btn-primary').click()
 page.locator('#account-dialog').screenshot(path=str(OUT/'componente-registro.png'))
 page.locator('#account-close').click()
 page.locator('#step-select').select_option('2');page.locator('#step-view').click()
 im=(ROOT/'assets/images/screenshots/paso-simulacro-tb1.webp').read_bytes()
 page.locator('#step-detail-image').evaluate('(img,data)=>{img.src=data}', 'data:image/webp;base64,'+base64.b64encode(im).decode())
 page.locator('#step-detail').screenshot(path=str(OUT/'componente-paso-con-referencia-tb1.png'))
 page.locator('#comparacion .comparison-table-wrap').screenshot(path=str(OUT/'componente-comparacion-desktop.png'))
 page.locator('#try-demo').click();page.locator('[data-action="answer-sim"]').nth(1).click()
 page.locator('#app-content').screenshot(path=str(OUT/'componente-simulacro-resultado.png'))
 page.close()
 mobile=b.new_page(viewport={'width':390,'height':844});mount(mobile)
 mobile.locator('#comparacion .comparison-cards').screenshot(path=str(OUT/'componente-comparacion-movil.png'))
 mobile.close();b.close()
print('Capturas de componentes renderizadas con Chromium aislado:', len(list(OUT.glob('componente-*.png'))))
