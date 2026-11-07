"""Capturas locales de la versión bajo prueba; no corresponden al sitio desplegado."""
from test_ui import sync_playwright,mount,browser_args
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'/'evidence';OUT.mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(**browser_args())
 for w,h in [(1440,900),(768,960),(390,844)]:
  page=b.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
  mount(page)
  page.screenshot(path=str(OUT/f'landing-{w}-initial.png'),full_page=True)
  page.locator('[data-tab="progreso"]').click()
  page.screenshot(path=str(OUT/f'progreso-{w}.png'),full_page=False)
  page.close()
 b.close()
print('capturas',len(list(OUT.glob('*.png'))),str(OUT))
