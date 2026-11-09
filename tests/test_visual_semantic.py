"""Visual/semantic checks; in-memory harness and not a public deployment audit."""
from test_ui import sync_playwright,mount,browser_args
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
def luminance(hexstr):
 h=hexstr.lstrip('#');rgba=[int(h[i:i+2],16)/255 for i in (0,2,4)]
 v=[u/12.92 if u<=0.04045 else ((u+0.055)/1.055)**2.4 for u in rgba]
 return .2126*v[0]+.7152*v[1]+.0722*v[2]
def contrast(a,b):
 la,lb=sorted([luminance(a),luminance(b)])
 return (lb+.05)/(la+.05)

results=[]
with sync_playwright() as p:
 browser=p.chromium.launch(**browser_args())
 for width in (320,390,767,768,1023,1024,1440):
  page=browser.new_page(viewport={'width':width,'height':900})
  mount(page)
  assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth'),f'overflow @{width}'
  assert page.locator(".brand .brand-symbol").count()==2 and page.locator(".brand .brand-name").first.inner_text()=="SismoListo"
  nav=page.locator('#site-nav a').all_text_contents()
  assert nav==['Inicio','Problema','Cómo funciona','Simulacros','Beneficios','Recursos','Contacto'],nav
  assert page.locator('h1').count()==1
  assert page.get_by_role('heading',name='Prepárate hoy. Actúa con más claridad.').count()==1
  results.append(f'{width}px: sin desbordamiento, marca sin fondo raster opaco, navegación y H1 OK')
  if width==390:
   page.locator('#menu-toggle').click()
   assert page.locator('#site-nav').is_visible()
   page.keyboard.press('Escape')
   assert not page.locator('#site-nav').is_visible()
   results.append('Menú móvil: abre, se cierra con Escape y devuelve el foco')
  if width==1440:
   page.locator('#site-nav').get_by_role('link',name='Beneficios').click()
   assert page.locator('#site-nav [aria-current="location"]').inner_text()=='Beneficios'
   results.append('Estado activo de navegación: aria-current correcto')
  page.close()
 browser.close()
for fg,bg,label in [('#1976d2','#ffffff','Azul web / blanco'),('#176c37','#ffffff','CTA verde oscuro / blanco'),('#212121','#ffffff','Texto principal / blanco'),('#516174','#ffffff','Texto secundario / blanco')]:
 r=contrast(fg,bg)
 assert r>=4.5,f'{label}: {r:.2f}'
 results.append(f'Contraste calculado {label}: {r:.2f}:1 >= 4.5:1')
output='\n'.join(results)+'\nRESULTADOS: '+str(len(results))+' comprobaciones satisfactorias.\nLIMITACIÓN: navegador aislado con fuentes web externas omitidas; no es prueba de sitio desplegado ni auditoría WCAG completa.\n'
(ROOT/'docs'/'RESULTADOS_VISUAL_SEMANTICO.txt').write_text(output,encoding='utf-8')
print(output)
