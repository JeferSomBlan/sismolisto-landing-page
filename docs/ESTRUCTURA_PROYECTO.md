# Organización modular — SismoListo Landing Page

## Fuente de verdad

- Requisitos y HU: informe TB1, pp. 49–88, y Final Project Statement V4, pp. 16–19 y 28.
- Mockups disponibles en el DOCX del TB1, pp. 99–102.
- **Pendiente:** URL del archivo Figma y acceso a sus nodos; en el DOCX examinado no se encontró hipervínculo de Figma. No se atribuye equivalencia visual píxel a píxel hasta compararlo con sus frames reales.

## Directorios

```text
sismolisto-landing-page/
├── index.html
├── css/
│   ├── base/
│   │   ├── tokens.css
│   │   ├── reset.css
│   │   ├── typography.css
│   │   ├── layout.css
│   │   ├── utilities.css
│   │   └── responsive.css
│   ├── components/
│   │   ├── header.css
│   │   ├── navbar.css
│   │   ├── footer.css
│   │   ├── buttons.css
│   │   ├── accessibility.css
│   │   ├── forms.css
│   │   └── feedback.css
│   ├── sections/
│   │   ├── hero.css
│   │   └── content.css
│   └── features/
│       ├── experience.css
│       ├── risks.css
│       ├── map.css
│       └── progress.css
├── js/
│   └── app.js
├── assets/
│   ├── images/
│   │   ├── brand/
│   │   ├── illustrations/
│   │   └── screenshots/
│   ├── icons/
│   └── fonts/
├── docs/
└── tests/
```

## Reglas de mantenimiento

1. Cada bloque de CSS reside en un módulo por función. No volver a crear un archivo único minificado.
2. `index.html` importa los módulos CSS en orden; `responsive.css` debe cargarse al final para conservar las media queries.
3. El JavaScript existente se mantiene en `js/app.js` para preservar la lógica de los escenarios y evitar una modificación funcional no solicitada.
4. Los cambios visuales se contrastarán con Figma en vistas desktop y móvil antes de afirmar fidelidad.
5. Cada imagen o icono requiere procedencia y relación con una HU, sección del mockup o componente del Design System.
6. Trabajar en `feature/*` y abrir Pull Request hacia `develop`; no sustituir directamente `main`.

## Cómo ejecutar en VS Code

Abrir la carpeta del proyecto y ejecutar en su terminal:

```bash
python -m http.server 8000
```

Abrir `http://localhost:8000` en un navegador. Si se publica con GitHub Pages, comprobar rutas relativas (`css/`, `js/`, `assets/`) en la URL final.

## Estado de la verificación visual

- Reestructuración CSS: **REALIZADA**.
- Comparación de regresión con la versión anterior: se debe ejecutar la prueba automatizada de captura y revisar el resultado.
- Inspección del Figma original: **NO COMPROBADA** por ausencia de URL verificable en el DOCX.
- Incorporación de imágenes originales del Figma: **PENDIENTE**.
