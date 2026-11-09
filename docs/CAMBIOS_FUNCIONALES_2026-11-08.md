# Registro de cambios auditados — SismoListo, 2026-11-08

**Origen:** ZIP auditado del capítulo IV; archivos base comparados parcialmente con `develop` mediante blobs Git. El ZIP no estaba fusionado previamente.

## Cambios de código
- `index.html`: navegación inferior móvil de la demostración (HU-044) y diálogo de confirmación para abandonar una evaluación (HU-042).
- `js/app.js`: perfil contextual (HU-041), guardar antes de salir (HU-042), varios marcadores locales para riesgos (HU-032), controles de desplazamiento del mapa (HU-045), feedback checklist (HU-039), porcentaje de evaluación pendiente (HU-048).
- `css/features/map.css`: transformaciones de plano y controles de desplazamiento. Sin mapas reales.
- `css/features/experience.css`: estilos adaptables de barra inferior de navegación móvil.
- `tests/`: se añaden suites `test_core_extension.py` y `test_acceptance_extended.py`; las suites antiguas fueron ajustadas para seleccionar la navegación específica sin ambigüedad.

## Evidencia
- `AUDITORIA_50_HU_CODIGO_2026-11-08.csv`: 50 HU; sin prioridad core docente aprobada.
- `AUDITORIA_100_ESCENARIOS_CODIGO_2026-11-08.csv`: 100 escenarios originales, 32 CUMPLE localmente, 8 NO CUMPLE y 60 NO COMPROBADO.
- `RESULTADOS_AUDITORIA_50_HU.json`: estadística reproducible y límites.
- `evidence/revision-escritorio-1440.png`, `revision-movil-390.png` y `revision-mapa-movil-390.png`: capturas de Chromium local aislado.

## Límites expresos
- La web nueva **no está desplegada**; no se ha modificado GitHub.
- `HU-021` no envía mensajes; `HU-030` no tiene destinos de descarga; `HU-034` carece de rutas/ETA reales; `HU-039` no sincroniza al recuperar red; `HU-041` no dispone de cuenta autenticada.
- La selección de 30 core requiere un acuerdo del equipo y comprobación de cada escenario.
- La marca reconstruida en CSS es temporal, pendiente del recurso maestro.
