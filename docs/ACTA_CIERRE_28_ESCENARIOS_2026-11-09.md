# SismoListo — acta de corrección de los 28 escenarios pendientes

Fecha: 9 de noviembre de 2026. Proyecto académico IHC y Tecnologías Móviles UPC, 2026-2.

## Fuente y alcance

- Enunciado: `UPC-PRE-202620-1ASI0385-Final-Project-Statement_V4.pdf`, pp. 16–18, 23.
- Criterios de aceptación: informe SismoListo TB1, pp. 52–77.
- Línea base de auditoría: `MATRIZ_100_ESCENARIOS_SIMULACIONES_2026-11-08.csv`: 72 CUMPLE locales y 28 NO COMPROBADO.
- Base técnica de trabajo: copia extraída de `SismoListo_AV2_Codigo_Simulaciones_Pendientes.zip`.
- Repositorio remoto: `https://github.com/SismoListo/sismolisto-landing-page`. Su rama `develop` consultada no incluye las modificaciones locales del ZIP.

## Intervenciones justificadas

| HU | Intervención | Alcance real |
|---|---|---|
| HU-003 | Selector de detalles e imágenes referenciales | Recortes de mockups TB1 pp. 106 y 113; no capturas nuevas de Figma |
| HU-005, HU-006 | Registro, validaciones y acceso ficticios | Cuenta local de demostración, sin autenticación remota; no ingresar credenciales reales |
| HU-008 | Beneficios didácticos concretos | Meta de 10 segundos no es medición ni resultado experimental |
| HU-009 | Carrusel de testimonios | Personajes explícitamente ficticios; no se atribuyen a entrevistados |
| HU-010 | Correo y redes de ejemplo | Dirección `.example` y enlaces a plataformas, no canales institucionales verificados |
| HU-014 | Comparación tabla/tarjetas | Tabla escritorio y tarjetas móvil, reutilizando tokens existentes |
| HU-016, HU-018 | Política y CTAs de acceso | Regreso al formulario sin pérdida de datos; CTA ofrece registro/login demo |
| HU-019, HU-020 | Favicon y contenido del footer | SVG de la misma marca simplificada; no reemplaza el logotipo original |
| HU-023 | CTA «Probar demo» y llamada a registro | Reutiliza micro-simulacro de salida bloqueada |
| HU-027 a HU-029 | Responsive, navegación y legibilidad | Nueve anchos; regla específica de 16 px del escenario TB1; cuatro contrastes de tokens comprobados |
| HU-032, HU-033, HU-036 | Nuevas pruebas del comportamiento existente | Riesgo con fotografía/marcador; zonas y vacío; simulacro y tiempo agotado |

## Resultados

- **28/28** escenarios antes NO COMPROBADO ejecutados ahora con resultado local satisfactorio; ver `RESULTADOS_28_ESCENARIOS_2026-11-09.json` y `tests/test_28_scenarios.py`.
- **72** escenarios previamente CUMPLE permanecen en la matriz como evidencia histórica; se ejecutaron suites de regresión, pero **no** se repitieron ahora 72 pruebas independientes, una por cada escenario.
- Las suites ejecutadas de regresión pasaron (11 principales, 7 alternativas, 14 dirigidas, 8 extendidas, 24 de ampliación core, 8 simulaciones, 33 de escenarios anteriores, 13 visuales/semánticas, 1 estructural). Algunas verificaciones se solapan.
- El recuento de 30 HU core **sigue NO COMPROBADO**: la selección y aprobación desde Product Backlog es un análisis distinto; HU-005 y HU-006 no cuentan automáticamente como core por figurar en estas pruebas.
- La navegación del Figma ajeno y la URL pública tras la corrección **no** se han comprobado ni modificado.

## Limitaciones metodológicas

Las pruebas se ejecutaron con Chromium, cargando HTML/CSS/JavaScript en un documento aislado en memoria. El navegador de este entorno bloquea `localhost`, por lo que no equivalen a pruebas en el sitio desplegado. El capturador de componentes resuelve imágenes locales mediante `data:` solo para la evidencia visual. La tipografía web remota se sustituye por fallbacks en estas pruebas.

El verificador de contraseñas ficticias **no es criptográfico**, carece de backend y se utiliza solo para demostrar navegación y validación. No introducir contraseñas reales. Las zonas/rutas son escenarios ficticios y no constituyen orientación real de evacuación.

Se midieron cuatro pares de contraste de tokens; las capturas y pruebas no permiten afirmar conformidad WCAG 2.2 AA integral.

## Archivos y trazabilidad

- `docs/MATRIZ_100_ESCENARIOS_ACTUALIZADA_2026-11-09.csv`
- `docs/MATRIZ_50_HU_ACTUALIZADA_2026-11-09.csv`
- `docs/RESULTADOS_28_ESCENARIOS_2026-11-09.json`
- `docs/RESULTADOS_REGRESION_2026-11-09.json`
- `tests/test_28_scenarios.py`
- `tests/capture_28_components.py`
- `docs/evidence/28_scenarios/`

Estado de GitHub: **NO ACTUALIZADO**. No se creó rama remota, commit, PR ni despliegue.
