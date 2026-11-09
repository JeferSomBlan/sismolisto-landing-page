# Incorporación segura de la revisión UX/UI en GitHub

**No se ha modificado el repositorio remoto.** La integración de GitHub rechazó la creación de rama con 403.

1. En VS Code/GitHub Desktop actualiza y cambia a `develop` del repositorio `SismoListo/sismolisto-landing-page`.
2. Crea `feature/auditoria-visual-capitulo-iv` desde `develop`.
3. Haz copia de seguridad antes de copiar archivos. Sustituye únicamente los archivos del ZIP de revisión manteniendo otros commits del equipo. No copies sobre `main`.
4. Revisa `git status`, `git diff`, los cambios en HTML y CSS y los recursos preservados.
5. Ejecuta desde la raíz `python tests/test_structure.py`, `python tests/test_visual_semantic.py`, `python tests/test_ui.py`, `python tests/test_alternatives.py` y `python tests/test_acceptance_av2.py` (requieren Python y Playwright/Chromium).
6. Registra `git add .` y `git commit -m "fix(ui): improve landing header brand and readability"`.
7. Envía la rama: `git push -u origin feature/auditoria-visual-capitulo-iv`.
8. Abre PR a `develop`, solicita revisión, y fusiona después de comprobar el diff y las pruebas.
9. Solo tras validación del equipo, prepara la integración de `develop` a `main`; GitHub Pages se publica desde `main` y `/(root)`.
10. Comprueba URL pública, consola, carga real de imágenes y fuentes, y captura escritorio/tablet/móvil. Actualiza entonces el 5.1.4.

No crees releases ficticias ni declares cumplimiento de 30 HU core por estas pruebas de regresión.
