# Alcance funcional y brechas — SismoListo AV2

## Diferenciar los entregables
- La guía V4 requiere 50 HU representadas en wireframes, mockups y prototipo móvil principal; no hay acceso Figma editable para comprobarlas.
- Exige 30 HU core funcionales en el Landing Page; **no se certifica su cumplimiento**.
- Se identificaron **22 candidatas preliminares** (HU-007, HU-023 y HU-031 a HU-050). Esto **no** demuestra que sean 22 capacidades distintas ni que todas estén implementadas: algunas están superpuestas, incompletas o principalmente concebidas para móvil.
- Las restantes HU son en gran medida informativas, de marketing, navegación y configuraciones; no se deben sumar artificialmente al mínimo core.

## Defectos que se corrigen en el ZIP
| HU | Modificación | Alcance y limitación |
|---|---|---|
| HU-032/HU-046 | Marcadores de riesgo con colores de gravedad y estado verde al resolver | No hay georreferenciación real |
| HU-034 | Variante ficticia verde al bloquearse la ruta y tiempos expresamente ilustrativos | No calcula ruta real, no reemplaza planos institucionales |
| HU-037 | Resultado con aciertos y errores explícitos | Ejercicio basado en un único reactivo |
| HU-038 | Estado del checklist completado con color semántico | No es validación de seguridad |
| HU-039/HU-043 | Progreso tras completar actividades y recomendaciones con aviso | Persistencia local; **NO sincronización remota** |
| HU-040 | Historial ordenado por fecha, de más reciente a más antiguo | Depende de datos locales |
| HU-045 | Detalle del marcador en hoja inferior accesible | Plano no es mapa real |
| HU-047 | Modal con Cancelar/Eliminar; conserva Deshacer 5 segundos | Sin backend |
| HU-049 | Resumen visible y diálogo de pasos pendientes | Resultados demostrativos |
| HU-050 | Estado 0%, CTA y resumen por categorías | Indicador ilustrativo |

## Brechas expresas NO resueltas
- HU-021: formulario prepara/copia texto, pero no envía mensajes; no hay dirección ni servicio autorizado.
- HU-030: no existen enlaces verificables a tiendas ni app móvil publicada; no se inventaron URLs ni QR.
- HU-034: no hay rutas ni tiempos de evacuación reales validados; la representación es didáctica.
- HU-039: `localStorage` no equivale a sincronización posterior al restablecimiento de conexión.
- HU-041/HU-044: criterios de navegación y perfil corresponden a experiencia móvil; no se incorporaron pantallas nuevas de forma arbitraria a web.
- Cobertura total del prototipo móvil: NO COMPROBADO por falta de archivo Figma.
- Priorización docente de 30 HU core: PENDIENTE de revisión del equipo.

## Evidencia técnica
- Las pruebas Python usan Playwright/Chromium en memoria y un `localStorage` simulado; no equivalen a URL desplegada.
- El código conserva estilos específicos de 4.1.2 y 4.3.2 (Poppins/Inter y tokens CSS), sin rehacer header, marca o secciones.
