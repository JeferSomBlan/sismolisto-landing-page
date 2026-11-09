# Integración controlada a GitHub — corrección de 28 escenarios

**No copies el ZIP entero directamente sobre una rama de equipo sin revisar diferencias.** El archivo ZIP utilizado como base contiene trabajo local todavía no coincidente con `develop`.

1. Conserva la carpeta original como respaldo.
2. En VS Code / GitHub Desktop abre el repositorio local actualizado, ejecuta `git fetch origin`, comprueba `git status` y `git switch develop && git pull origin develop` cuando no haya cambios sin guardar.
3. Crea `git switch -c feature/aceptacion-28-escenarios` desde `develop`.
4. Revisa en el paquete el listado `docs/ARCHIVOS_CAMBIADOS_28_2026-11-09.txt` y compara archivo por archivo con tu rama mediante `git diff --no-index` o la interfaz Compare. Si otra persona cambió un mismo archivo, integra cuidadosamente, sin reemplazar sus cambios.
5. Copia los cambios autorizados de `index.html`, `js/app.js`, `js/acceptance.js`, `css/features/acceptance.css`, favicon, imágenes TB1 extraídas, tests y docs. Mantén intactas las carpetas de otros miembros.
6. Ejecuta `python tests/test_28_scenarios.py`, `python tests/test_ui.py`, `python tests/test_alternatives.py`, `python tests/test_acceptance_av2.py`, `python tests/test_structure.py` y el resto de suites incluidas. Inspecciona las capturas de `docs/evidence/28_scenarios/`.
7. Ejecuta `git diff --check` y `git status`. No agregues archivos privados ni credenciales.
8. Confirma con `git add ...` (rutas revisadas), luego `git commit -m "feat(web): cover remaining academic acceptance scenarios"`.
9. Publica `git push -u origin feature/aceptacion-28-escenarios` y abre Pull Request hacia `develop` con alcance, pruebas, limitaciones y capturas.
10. Tras revisión y PR de `develop` a `main`, espera el proceso de GitHub Pages y verifica los flujos sobre `https://sismolisto.github.io/sismolisto-landing-page/`. Solo entonces actualiza 5.1.2 y 5.1.4 con evidencia de PR/commit/despliegue reales.

**Restricciones:** no forzar push, no modificar `main` directamente, no afirmar 30 HU core, no subir datos de prueba reales.
