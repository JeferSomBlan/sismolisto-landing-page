# Integración a VS Code / GitHub

1. Conserva una copia del repositorio y consulta `git status` antes de copiar.
2. `git switch develop && git pull origin develop`
3. `git switch -c feature/av2-hu-acceptance-fixes`
4. Copia los archivos del ZIP a la raíz del repositorio, sin borrar los documentos preexistentes `CONTRIBUTING.md`, `source-code-management.md` o el historial `.git`.
5. Abre `index.html` con Live Server o servidor local; desde el entorno de desarrollo: `python -m http.server 8000` y en el navegador `http://localhost:8000`.
6. Ejecuta `python tests/test_structure.py` y, tras instalar Playwright/Chromium, `python tests/test_ui.py`, `python tests/test_alternatives.py`, `python tests/test_acceptance_av2.py`, `python tests/test_visual_semantic.py`.
7. Comprueba manualmente en escritorio, tablet y móvil.
8. `git add . && git commit -m "fix(web): align core interactions with acceptance criteria"`
9. `git push -u origin feature/av2-hu-acceptance-fixes`; abre PR hacia `develop`; no se ha realizado automáticamente.
10. Las features para el segundo repositorio están en ZIP independiente y NO están ejecutadas.

No se ha realizado despliegue ni se ha afirmado que exista URL pública.
