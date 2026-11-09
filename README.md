# SismoListo — Landing Page, corrección AV2

Implementación académica de SismoListo en HTML5, CSS3 y JavaScript básico. Se conserva la organización CSS modular, los recursos y la referencia a la guía del capítulo IV del informe TB1.

## Probar localmente

```bash
python -m http.server 8000
```
Abre `http://localhost:8000` en un navegador. Para pruebas automatizadas se requiere `pip install -r requirements-dev.txt` y `python -m playwright install chromium`. En el entorno de ejecución de este paquete, las pruebas se han realizado con montaje en memoria debido a restricciones de navegación local; no equivalen a pruebas de despliegue.

## Documentación

- `docs/ALCANCE_FUNCIONAL_Y_BRECHAS.md`: qué está corregido y qué sigue sin demostrarse.
- `docs/MATRIZ_50_HU_AV2.csv`: clasificación y resultados por HU.
- `docs/MATRIZ_100_ESCENARIOS_AV2.csv`: 100 criterios originales y evidencia diferenciada.
- `docs/INSTRUCCIONES_VSCODE_GITHUB.md`: integración sin sobrescribir el historial.

**Advertencia**: mapas, zonas, rutas y tiempos del sitio son ejemplos de entrenamiento NO validados para emergencias reales. No existe backend, autentificación ni sincronización remota.


## Revisión de fidelidad visual (8 de noviembre de 2026)

Se ajustaron exclusivamente la cabecera, la legibilidad de la navegación y botones,
la representación de marca y la lectura del pie de página, conforme al capítulo IV.
La captura original del logotipo (70 × 22 px, fondo opaco) se **conserva** en
`assets/images/brand/logo-sismolisto-captura-tb1.png`. Para evitar una imagen ampliada
pixelada, la web presenta temporalmente un símbolo circular y el nombre de marca
reproducidos con CSS y texto editable. No se afirma equivalencia exacta con el logo vectorial
original: debe reemplazarse cuando el equipo aporte el recurso de alta resolución.

El código actualizado se entrega **sin publicar**; la URL de GitHub Pages mantiene
la versión anterior hasta que se integre, revise y despliegue una nueva versión.
Revisa `docs/AUDITORIA_VISUAL_2026-11-08.md` y `docs/INSTRUCCIONES_GITHUB_REVISION.md`.


## Actualización auditada — 8 de noviembre de 2026

Esta copia incorpora correcciones locales vinculadas con HU-032, HU-039, HU-041, HU-042, HU-044, HU-045 y HU-048, sin modificar las historias originales ni agregar un servicio backend. Los mapas son ficticios. No se ha subido esta revisión a GitHub Pages.

La versión base procede del ZIP `SismoListo_LandingPage_CapIV_Codigo_Auditado.zip`; **no es idéntica a `develop`**. Al cotejar los blobs Git, `index.html` y `css/components/header.css` ya eran distintos de sus equivalentes de la rama remota, mientras que `js/app.js` sí coincidía antes de las correcciones de esta iteración. Por tanto, se requiere inspeccionar los cambios antes de integrarlos.

### Pruebas locales

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

**Limitación:** estas suites montan HTML/CSS/JavaScript en memoria; no equivalen a una prueba del sitio desplegado ni a una certificación de las 30 HU core. Consulta `docs/RESULTADOS_AUDITORIA_50_HU.json` y el Excel anexo.

## Simulaciones de criterios de aceptación (8 de noviembre de 2026)

Con la aclaración académica de que se permiten flujos demostrativos en JavaScript, esta versión incorpora:

- **HU-021:** enviar una consulta de manera **simulada**, limpiar campos y mostrar confirmación sin afirmar que exista servicio de correo ni respuesta garantizada.
- **HU-030:** opciones ilustrativas de Google Play y App Store en móvil y QR a la propia página web en escritorio. No hay descarga real ni app publicada.
- **HU-034:** cálculo de la ruta mínima de un grafo ficticio y alternativa ante un bloqueo crítico. No son rutas de evacuación reales.
- **HU-039:** registrar una actividad sin conexión y procesar una cola de sincronización **solo local y simulada** al reconectar. No se envían datos a un servidor.
- **HU-041:** configuración inicial simulada de perfil y espacio habitual.

Para probar estas funcionalidades:

```bash
python tests/test_pending_scenarios.py
python tests/test_simulations.py
```

Las matrices actualizadas están en `docs/MATRIZ_100_ESCENARIOS_SIMULACIONES_2026-11-08.csv` y `docs/MATRIZ_50_HU_ESTADO_SIMULACIONES_2026-11-08.csv`.

**Resultado local orientativo**: 72 escenarios con evidencia local satisfactoria; 28 no comprobados; 32 HU con sus dos escenarios clasificados como cumplidos localmente. **No acredita las 30 HU core** por no haberse aprobado aún su selección desde el backlog. No equivale a una publicación en GitHub Pages ni a una auditoría WCAG completa.
