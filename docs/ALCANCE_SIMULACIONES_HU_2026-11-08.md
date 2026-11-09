# Alcance de simulaciones funcionales — SismoListo (2026-11-08)

Fuente de requisitos: Final Project Statement V4 y 50 HU de TB1. Esta entrega no modifica el Figma ni el repositorio remoto.

- **HU-021**: formulario HTML validado, botón «Enviar», estado de éxito con texto esperado y aclaración visible de simulación; limpia los campos y guarda un registro en `localStorage`. No envía correos ni garantiza respuestas en 48 horas.
- **HU-030**: botones de demostración para Google Play / App Store en móvil, y QR local en escritorio. El QR abre el Landing Page web en `#descargar`; no existe APK, IPA ni publicación en tiendas.
- **HU-034**: Dijkstra sobre un grafo académico ficticio de cuatro nodos y pesos ilustrativos. Calcula la ruta mínima de ese grafo y, al registrar bloqueo crítico, usa ruta alterna. Los tiempos y trazados no son reales ni seguros para evacuación.
- **HU-039**: los cambios hechos sin conexión se guardan en el navegador; al detectar recuperación de conectividad, se limpia una cola *simulada* de sincronización local. No hay servidor ni sincronización entre dispositivos.
- **HU-041**: primer paso de configuración de perfil/espacio habitual en datos de ejemplo. No existe autenticación real.

## Resultados y límites

- La matriz local anterior tenía **32 CUMPLE, 8 NO CUMPLE y 60 NO COMPROBADO**.
- La nueva matriz registra **72 CUMPLE localmente y 28 NO COMPROBADO** después de ejecutar 33 pruebas por escenario anteriormente sin evidencia, ocho simulaciones y regresión. El conteo usa claves HU + número de escenario y evita duplicaciones.
- Hay **32 HU con los dos escenarios clasificados CUMPLE localmente**. Esto **no** demuestra 30 HU *core*; varias historias son informativas y la selección final exige backlog/priorización.
- No se ha actualizado GitHub Pages. Estas pruebas se ejecutaron en Chromium con HTML/CSS/JS cargados en memoria; tampoco equivalen a una auditoría WCAG completa.

## Integración Git

1. Clonar o actualizar la rama `develop` del repositorio de SismoListo.
2. Crear rama `feature/simulaciones-hu-av2`.
3. Comparar y copiar **solo los cambios autorizados** desde este paquete; evita sobrescribir archivos que tu equipo haya cambiado entretanto.
4. Ejecutar `python tests/test_structure.py`, `python tests/test_ui.py`, `python tests/test_alternatives.py`, `python tests/test_pending_scenarios.py` y `python tests/test_simulations.py`, además de las suites dirigidas.
5. Registrar `feat(web): simulate acceptance flows for HU-021 HU-030 HU-034 HU-039` y abrir PR hacia `develop`.
6. Tras revisar y fusionar a `main`, verificar la URL publicada y documentar la evidencia de despliegue.
