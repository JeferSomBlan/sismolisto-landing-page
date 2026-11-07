# Alcance y trazabilidad de historias — Landing Page SismoListo

**Fuente normativa:** `UPC-PRE-202620-1ASI0385-Final-Project-Statement_V4.pdf`, pp. 16–19, 28.  
**Fuente del producto:** `upc-pre202620-1ASI0385-16734-sismolisto-report-tb1.pdf`, pp. 49–88 (HU y backlog), 92, 94–112 (arquitectura, UI, wireflows y mockups).  
**Alcance:** implementación web de demostración; no es el prototipo móvil Figma ni una aplicación desplegada con backend.

## Principio de control

No se incorpora una funcionalidad si no existe una HU, un flujo documentado o una decisión explícita de arquitectura en el TB1. Los controles de calidad (mensajes de error, etiquetas, accesibilidad, advertencia sobre datos ficticios) son necesarios para ejecutar de manera responsable las funciones aprobadas, y no se cuentan como HU adicionales.

## Historias cubiertas en la primera implementación

**Leyenda:** DEMO = comportamiento local comprobable, PARCIAL = solamente un subconjunto de los escenarios o una simulación sin infraestructura real, PENDIENTE = no implementado. Estos estados no equivalen a validación de usuarios ni cumplimiento docente.

| HU | Función / evidencia en el sitio | Estado | Relación |
|---|---|---|---|
| HU-001 | Título de portada, propuesta y CTA | DEMO | `#inicio` |
| HU-002 | Exposición del problema y enlace a solución | DEMO | `#problema` |
| HU-003 | Cuatro pasos del proceso | DEMO | `#como-funciona` |
| HU-004 | Tarjetas de capacidades y enlaces a experiencia | DEMO | `#funcionalidades` |
| HU-005 | Registro real de cuentas | PENDIENTE | Sin backend; no simular persistencia de credenciales |
| HU-006 | Autenticación real | PENDIENTE | Sin backend |
| HU-007 | Tres escenarios catalogados | DEMO | `#simulacros` |
| HU-008 | Beneficios filtrados por perfil | DEMO | `#beneficios` |
| HU-009 | Testimonios verificables | PENDIENTE | Requiere testimonios auténticos y permiso |
| HU-010 | Acceso a contacto | PARCIAL | Sin redes/correo del equipo verificados |
| HU-011 | Tres recursos con filtro | DEMO | `#recursos` |
| HU-012 | Perfiles objetivo | DEMO | `#segmentos` |
| HU-013 | Duplicado textual de HU-012 en el TB1; perfiles mostrados una sola vez | PARCIAL | No se duplica UI |
| HU-014 | Comparación comercial con competidores | PENDIENTE | No es prioritaria para core y requiere revisión de hechos |
| HU-015 | Compartir página (API nativa o copiar) | DEMO | `#contacto` |
| HU-016 | Diálogo informativo sobre privacidad de la demo | PARCIAL | No es una política legal definitiva |
| HU-017 | Navegación responsive con menú plegable | DEMO | Header + CSS |
| HU-018 | CTA principal lleva al área de práctica | PARCIAL | No hay registro/autenticación real |
| HU-019 | Identidad de SismoListo en encabezado | DEMO | `#inicio` |
| HU-020 | Pie de página con enlaces | DEMO | Footer |
| HU-021 | Formulario de consulta copiable, sin envío | PARCIAL | No se finge entrega de mensaje |
| HU-022 | Volver al inicio | DEMO | Footer |
| HU-023 | CTA para demostración interactiva | DEMO | `#simulacros` |
| HU-024 | Preguntas frecuentes expandibles | DEMO | `#preguntas` |
| HU-025 | CTA secundario a «Cómo funciona» | DEMO | Hero |
| HU-026 | Compartir recurso preventivo | DEMO | Recursos |
| HU-027 | Compatibilidad responsive en distintas anchuras | DEMO | CSS media queries |
| HU-028 | Menú de navegación entre secciones | DEMO | Header |
| HU-029 | Jerarquía semántica, foco visible, etiquetas y avisos de estado | PARCIAL | Requiere auditoría WCAG adicional |
| HU-030 | Botones de tiendas de apps o QR de descarga | PENDIENTE | No existen enlaces de app verificados; no crear enlaces ficticios |
| HU-031 | Selección/alta de espacio y evaluación guiada | DEMO | `app: evaluar` |
| HU-032 | Registro de riesgo con categoría, gravedad, descripción y foto local opcional | DEMO | `app: riesgos` |
| HU-033 | Zonas referenciales en mapa, mensaje sin evaluar | PARCIAL | No hay zonas validadas |
| HU-034 | Ruta y señalización de bloqueo ilustrativas | PARCIAL | No calcula rutas reales ni tiempos |
| HU-035 | Escenario de máximo 60 s con pausa y reinicio | DEMO | `app: practica` |
| HU-036 | Tres opciones por escenario y estado sin respuesta | DEMO | `app: practica` |
| HU-037 | Resultado, explicación y opción de repetir | DEMO | `app: practica` |
| HU-038 | Checklist, ítems y porcentaje | DEMO | `app: checklist` |
| HU-039 | Indicador agregado de avance local | PARCIAL | Métrica demo, sin sincronización con servidor |
| HU-040 | Historial local y filtro por tipo | DEMO | `app: progreso` |
| HU-041 | Contexto de estudiante/oficina y cambio de ambiente | PARCIAL | No hay cuenta o perfil remoto |
| HU-042 | Guardar evaluación pendiente | DEMO | `app: evaluar` |
| HU-043 | Recomendaciones según riesgo/resultado, marcadas «Hecho» | DEMO | `app: progreso` |
| HU-044 | Accesos directos a funciones core | DEMO | `app: inicio` |
| HU-045 | Mapa referencial con filtros, zoom y marcadores | PARCIAL | No es un plano georreferenciado |
| HU-046 | Editar y marcar como resuelto | DEMO | `app: riesgos` |
| HU-047 | Confirmación de eliminación y deshacer 5 s | DEMO | `app: riesgos` |
| HU-048 | Reanudar o descartar evaluación/simulacro | DEMO | `app: inicio` |
| HU-049 | Finalizar y mostrar resumen, incluso con pendientes confirmados | DEMO | `app: progreso` |
| HU-050 | Resumen general del progreso y pendientes | DEMO | `app: progreso` |

## No confundir alcance total y mínimo de la guía

La guía V4, pp. 16–17 y 28, exige **al menos 30 HU core** funcionales en la versión final, seleccionadas de las mismas 50 HU del Product Backlog. En la clasificación actual de SismoListo, las HU-031 a HU-050 son las 20 más claramente operativas, con apoyo de HU-007, HU-023 y otras orientadas a interacción. Muchas HU-001 a HU-030 están relacionadas con lectura informativa, navegación o configuración, no con el núcleo funcional. Por ello, esta primera versión **no demuestra todavía 30 HU core completas**. No se deben reclasificar historias de marketing o de decoración como core para alcanzar el número. Se requiere una revisión autorizada del backlog y la matriz de aceptación antes de la sustentación final.

## Flujos y estados principales

1. **Evaluar entorno:** seleccionar ambiente o agregar → responder tres preguntas → avanzar/retroceder → guardar y salir → reanudar → finalizar → historial. Referencia: HU-031, HU-042, HU-048.
2. **Reportar riesgos:** categorizar → gravedad → descripción/foto opcional → guardar → visualizar → editar/resolver → confirmar eliminación → deshacer durante cinco segundos. Referencia: HU-032, HU-046, HU-047.
3. **Consultar mapa:** evaluado → ver zonas referenciales → filtros/zoom/marcadores → reporte crítico de ruta obstruida cambia tramo a rojo. Referencia: HU-033, HU-034, HU-045.
4. **Micro-simulacro:** elegir → iniciar cuenta de 60 s → seleccionar una de tres respuestas o agotar tiempo → feedback → repetir; alternativa de pausa y reanudación. Referencia: HU-007, HU-023, HU-035 a HU-037.
5. **Preparación:** checklist → marcar/agregar → avance local → historial filtrado → recomendaciones → finalizar resumen. Referencia: HU-038 a HU-043 y HU-049–050.

## Límites técnicos y de seguridad

- El encabezado emplea un recorte raster del logotipo presente en un mockup original del TB1; el recurso vectorial oficial no está disponible, por lo que la fidelidad de alta resolución sigue pendiente.

- Datos del navegador (`localStorage`), sin cuentas, API ni servidor.
- El formulario de contacto copia un borrador: **no envía mensajes**.
- Los escenarios y mapas son hipotéticos y **no sustituyen** rutas, zonas o protocolos reales validados por un profesional o institución.
- Un reporte de demostración **no notifica** a brigadistas ni SST.
- La tipografía visual del sitio sigue el estilo web del proyecto; Times New Roman de 12 pt corresponde al documento académico, no al producto web.
