# Protocolo de pruebas — Landing Page SismoListo

No confundir **pruebas automatizadas del comportamiento local** con entrevistas, evaluaciones heurísticas, validación de seguridad física o aceptación docente.

## Funcionalidad que debe revisarse

| Caso | HU | Procedimiento observable | Resultado esperado |
|---|---|---|---|
| T01 | HU-017, HU-028 | Reducir la pantalla a 390 px y abrir menú | Menú legible, enlaces accesibles, sin desbordamiento horizontal |
| T02 | HU-031 | Elegir aula demo, responder 3 pasos | Evaluación en historial y acceso a zonas |
| T03 | HU-031 | Seleccionar Agregar espacio | Nuevo ambiente disponible y evaluación continúa |
| T04 | HU-042, HU-048 | Guardar evaluación incompleta y volver | Tarjeta de continuación y estado preservado |
| T05 | HU-032 | Guardar riesgo sin foto | Registro visible con tipo, gravedad y descripción |
| T06 | HU-046 | Editar riesgo y marcar Resuelto | Valores y estado actualizados |
| T07 | HU-047 | Eliminar riesgo y elegir Deshacer antes de 5 s | Registro restaurado |
| T08 | HU-034, HU-045 | Marcar ruta obstruida crítica, abrir zonas | Trayecto ilustrativo cambia a rojo; aviso de simulación |
| T09 | HU-035–037 | Iniciar simulacro y elegir opción | Resultado con acierto/error, tiempo y retroalimentación |
| T10 | HU-035, HU-048 | Guardar simulacro y volver | Opción Continuar/Reiniciar |
| T11 | HU-038–040 | Marcar ítems de checklist | Porcentaje local e historial visibles |
| T12 | HU-043, HU-049 | Revisar recomendación y finalizar sesión | Mensaje de resultado y estado pendiente cuando corresponda |
| T13 | HU-011 | Filtrar recursos por tema | Tarjetas filtradas |
| T14 | HU-021 | Completar formulario de contacto | Borrador copiado o aviso; no afirmar envío |
| T15 | HU-029 | Navegar con teclado | Foco visible y etiquetas reconocibles |

## Responsabilidad de validación

- No registrar datos personales reales, contraseñas ni información confidencial de edificios.
- Comprobar al menos resoluciones 1440, 768 y 390 px, además de 320 px mínimo documentado en el TB1.
- Probar casos alternativos; un botón sin estado observable no demuestra cumplimiento funcional.
- No declarar «CUMPLE WCAG 2.2 AA» sin auditoría de contraste, teclado y tecnologías de asistencia.

## Evidencias

Guardar capturas y video después de ejecutar la versión que realmente se integrará y desplegará. El resultado de tests locales se incluye en un registro independiente con fecha y entorno de ejecución.
