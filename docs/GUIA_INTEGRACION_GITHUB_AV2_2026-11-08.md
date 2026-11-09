# Integración segura con GitHub / VS Code

Repositorio: https://github.com/SismoListo/sismolisto-landing-page

**Importante:** el ZIP anterior auditado ya difiere de `develop` en `index.html` y `css/components/header.css`. No ejecutar copias destructivas ni sustituir todo el repositorio sin revisar los cambios.

1. Realiza una copia de seguridad de la carpeta actual del equipo.
2. Abre VS Code y clona el repositorio real:

```sh
git clone https://github.com/SismoListo/sismolisto-landing-page.git
cd sismolisto-landing-page
git switch develop
git pull --ff-only origin develop
git switch -c feature/hu-core-av2-20261108
```

3. Extrae el ZIP del proyecto auditado en **otra carpeta** y utiliza la vista Compare de VS Code o `git diff --no-index` para comparar archivos, empezando por `index.html`, `css/components/header.css`, `css/features/map.css`, `css/features/experience.css` y `js/app.js`. Conserva las mejoras de ambas versiones; el ZIP contiene mejoras de cabecera no fusionadas.
4. Copia únicamente los archivos revisados al clon, manteniendo intacto `.git` y preservando `CONTRIBUTING.md` del repositorio remoto.
5. Verifica `git status` y ejecuta las pruebas desde la raíz:

```sh
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python tests/test_ui.py
python tests/test_alternatives.py
python tests/test_acceptance_av2.py
python tests/test_core_extension.py
python tests/test_acceptance_extended.py
python tests/test_visual_semantic.py
```

6. Antes de enviar datos a GitHub, revisa que no existan credenciales ni archivos temporales. Luego:

```sh
git diff --stat
git add index.html css js tests docs README.md
git commit -m "feat(web): improve core flows and acceptance evidence"
git push -u origin feature/hu-core-av2-20261108
```

7. Abre Pull Request hacia `develop`, revisa cambios y checks. No realices merge a `main` hasta validar la versión.
8. Si se integra a `main`, espera el despliegue de GitHub Pages y prueba la URL pública a 1440/390 px, navegador y teclado. Documenta por separado el commit desplegado y las evidencias del apartado 5.1.4.

**Estado actual**: los pasos 2–8 no se han ejecutado desde esta sesión. La conexión de escritura de GitHub había respondido HTTP 403 en operaciones anteriores. No hay commit remoto ni PR nuevo atribuible a esta entrega.
