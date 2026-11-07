# Registro de correcciones y verificación — SismoListo Capítulo IV

## Correcciones realizadas

- Sustitución de la «S» creada en código por un recorte fiel de un **mockup existente**, en `assets/images/brand/` (no logo nuevo).
- Navegación del Landing Page alineada a las etiquetas/orden del wireframe 4.3.1; los enlaces funcionales conservan sus destinos.
- Tipografía web Poppins/Inter declarada mediante enlace remoto, con alternativas locales; no se distribuyen archivos fuente.
- Tokens visuales web y semánticos diferenciados para resolver divergencias entre 4.1.1 y 4.3.2.
- Fondo hero blanco, tarjetas menos ornamentales, radios de diseño y espaciados ajustados.
- Bloque de beneficios en tarjetas, sin añadir mensajes ni beneficios no documentados.
- Eliminación de aviso duplicado que antecedía al header; la advertencia de mapas y rutas ficticias **permanece junto a la demostración interactiva**.
- Menú móvil cierra con Escape y devuelve foco; enlace de navegación seleccionado comunica `aria-current`.
- Botones incorporan reglas de `focus-visible` y `disabled`; entradas disponen de retroalimentación `:user-invalid`.
- Conservación de `js/app.js` salvo control de navegación; funciones de evaluación, mapas, riesgos, simulacros y progreso intactas.

## Pruebas ejecutadas

- `tests/test_structure.py`: **PASS**; 19 archivos CSS, 1 JS y rutas locales comprobadas.
- `tests/test_ui.py`: **11 PASS** (4 anchuras 1440, 768, 390, 320; flujos de evaluación, riesgos, ruta simulada, micro-simulacro, checklist, historial, persistencia local).
- `tests/test_alternatives.py`: **7 PASS** (menú móvil, alta de espacio, guardar/reanudar, edición/resolución/eliminación de riesgo, pausa/reanudación, filtro).
- `tests/test_visual_semantic.py`: **13 PASS** (7 anchuras adicionales / sin overflow, logotipo real cargado, etiquetas y H1, menú Escape y estado activo, cuatro pares de contraste calculado).
- Total: **31 comprobaciones registradas**, contando mediciones por anchura y de interacción independientes; **no 31 historias de usuario verificadas**.

## Limitaciones metodológicas

- Pruebas en DOM montado en memoria con scripts reales; **no** prueba de sitio publicado, ni en hardware físico móvil.
- Se omite únicamente la descarga remota de Google Fonts en el harness aislado; la definición CSS está presente, pero la carga efectiva de Poppins depende de conectividad y del proveedor.
- Los contrastes reportados corresponden solo a cuatro pares de colores; no constituyen auditoría WCAG 2.2 AA completa.
- El logo recortado conserva la apariencia del mockup, pero la resolución de origen es baja y el vector oficial no está disponible.
- No se demostró que 30 HU core estén completamente implementadas y funcionales.
- El repositorio GitHub de SismoListo **no fue modificado** desde esta revisión. La integración, pull request, despliegue y URL pública permanecen pendientes.

## Evidencia a recopilar después de subir la versión

- Pull Request de `feature/landing-page-capiv` hacia `develop`, con commit `fix(ui): align landing page with chapter four style guide`.
- Enlace de publicación y captura de GitHub Pages (si se utiliza ese servicio).
- Capturas de las vistas a 1440, 1024, 768, 390 y 320 px desde URL real.
- Video recorriendo las funcionalidades core y alternativas que correspondan.
- Evidencia de evaluación heurística/validación real con usuarios, sin confundirla con pruebas automatizadas.
