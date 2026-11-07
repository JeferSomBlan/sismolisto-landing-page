"""Auditoria sencilla de rutas CSS y recursos para GitHub Pages / VS Code."""
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='link' and attrs.get('rel')=='stylesheet' and attrs['href'].startswith('css/'):self.links.append(attrs['href'])
        if tag=='script' and attrs.get('src'):self.links.append(attrs['src'])

s=Links();s.feed((ROOT/'index.html').read_text(encoding='utf-8'))
assert len(s.links)==20,f'Esperado: 19 CSS + 1 JS; hay {len(s.links)}'
assert len(s.links)==len(set(s.links)),'Rutas de archivos duplicadas'
assert s.links[-2]=='css/base/responsive.css','Responsive CSS debe cargarse al final'
for ref in s.links:
    file=(ROOT/ref).resolve()
    assert file.is_relative_to(ROOT) and file.is_file(),f'Archivo no encontrado: {ref}'
assert (ROOT/'assets/images/brand/README.md').is_file()
print(f'Rutas OK: {len(s.links)-1} CSS y 1 JS; recursos y orden comprobados.')
