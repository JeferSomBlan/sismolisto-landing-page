# Registro de comprobaciones locales — 7 de noviembre de 2026

**Alcance:** HTML, CSS y JavaScript originales ejecutados en Chromium con documento montado en memoria. El navegador de la evaluación bloqueó las navegaciones a direcciones `localhost` y `file://`. Por esa razón las pruebas no equivalen a funcionamiento comprobado desde URL pública. No se verificó despliegue ni ejecución en un equipo del usuario.

**Comprobaciones exitosas:** 18 de 18 escenarios automatizados ejecutados.

- Responsive: 1440×900, 768×900, 390×844, 320×780 sin desbordamiento horizontal detectado.
- HU-031: selección de ambiente, evaluación de tres pasos y alta alternativa de ambiente.
- HU-032: registro de riesgo sin fotografía.
- HU-034: cambio visual de ruta en escenario obstruido (ficticio).
- HU-035 a HU-037: micro-simulacro con respuesta y retroalimentación.
- HU-038: checklist con cálculo porcentual.
- HU-040: historial.
- Almacenamiento de estado entre remontajes de documento bajo shim localStorage.
- Menú responsive abierto/cerrado.
- HU-042/HU-048: guardar y continuar evaluación.
- HU-046: edición y resolución de riesgo.
- HU-047: confirmación de eliminación y acción «Deshacer».
- HU-035/HU-048: pausa y reanudación de micro-simulacro.
- HU-011: filtro de recursos.

**NO COMPROBADO:** pruebas en URL pública, navegadores de usuario, dispositivos físicos, lector de pantalla, contraste medido, tiempos agotados completos, foto grande, accesibilidad WCAG 2.2 AA y eficacia real de medidas de seguridad. La aceptación completa de cada HU requiere comprobación de sus escenarios de aceptación.
