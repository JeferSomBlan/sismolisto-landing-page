# Auditoría visual y técnica — SismoListo (8 de noviembre de 2026)

## Fuentes y alcance

- TB1, capítulo IV (guía visual y mockups), especialmente páginas impresas 89–102.
- Final Project Statement V4, apartados 5.1.3 y 5.2 (guía oficial).
- Código `develop` de `SismoListo/sismolisto-landing-page`, cotejado por SHA Git contra el ZIP local.
- Capturas del sitio publicado proporcionadas en la conversación.
- Pruebas Chromium con HTML/CSS/JS reales montados en memoria: navegador sin acceso a URL local/pública ni Google Fonts externas.

**No se audita la publicación posterior a cambios**: no se ha actualizado `main`, `develop` ni Pages. El intento de crear una rama mediante el conector recibió 403.

## Matriz visual y funcional

| Elemento | Fuente | Antes | Problema | Corrección | Resultado |
|---|---|---|---|---|---|
| Cabecera y navegación | 4.1.2; 4.2.4; 4.3.2 | NO CUMPLE antes | 69 px de altura; enlaces 12,64 px en 1440; logotipo opaco | Altura ~85 px escritorio; enlaces 16 px; símbolo y texto CSS; menú colapsado <1151 px | COMPROBADO en navegador aislado |
| Identidad / logotipo | 4.1.1; 4.3.2 | NO CUMPLE antes | PNG original 70 × 22 px, opaco y ampliado | Original preservado; reconstrucción tipográfica limpia de presentación (NO es archivo de logo aprobado) | PARCIAL; recurso vectorial NO COMPROBADO |
| Hero | 4.2.1; 4.3.2 | CUMPLE estructural | H1, CTA y plano ilustrativo visibles | Contenido preservado; CTA alcanza mínimo 48 px; cuerpo legible | COMPROBADO local; exactitud Figma NO COMPROBADA |
| Problema / Cómo funciona | 4.2.1; 4.3.1 | CUMPLE estructural | Secciones y jerarquía existentes | Se mantienen; sin funciones nuevas | COMPROBADO estructural |
| Simulacros | 4.3.2; HU de entrenamiento | PARCIAL | Tres tarjetas existentes con interacciones de demostración | Se preservan flujos y se refuerza texto de tarjetas | Prueba funcional local parcial |
| Beneficios | 4.3.2 | PARCIAL | Selector de estudiantes/oficinas existente | Se conserva audiencia y diseño | Prueba funcional local parcial |
| Recursos | 4.3.2; 4.2.3 | PARCIAL | Tres recursos textuales, filtro por tema | Se conserva estructura; no se inventan imágenes | Prueba funcional local parcial |
| Preguntas frecuentes | 4.3.2 | CUMPLE estructural | Tres preguntas; primera desplegada | Se conserva sin alteración | COMPROBADO estructural |
| Contacto | 4.3.2; HU-021 | NO CUMPLE funcional completo | Copia mensaje, no lo envía | Mantiene declaración explícita de demo; no se simula backend | NO CUMPLE envío exigido; pendiente servicio |
| Evaluación / Riesgos | HU-031, HU-032 y relacionadas | PARCIAL | Controles y persistencia local sin backend | Se conservan flujos y validaciones | Pruebas locales, no 100 Gherkin |
| Mapa / Rutas | HU-034 y HU-045 | PARCIAL | Plano y trayecto son ficticios | Permanece advertencia para evitar falsa seguridad | COMPROBADO como simulación |
| Progreso / Checklist | HU-038 a HU-050 aplicables | PARCIAL | Estado local, historial, recomendaciones | Se conserva; no se presenta sincronización real | Prueba local dirigida |
| Footer | 4.1.2; 4.3.2 | NO CUMPLE visual antes | Existía, pero texto de ~13 px | Espaciado ampliado, texto y enlaces 16 px y foco visible | COMPROBADO local en capturas |
| Responsive | 4.1.2 | PARCIAL | Sin desbordamiento en pruebas previas | Menú 48 px, texto 16 px; 320–1920 px medidos | COMPROBADO en 7 anchos aislados |

## Contradicciones documentales

1. **Tipografía**: 4.1.1 define Inter para el sistema general, mientras 4.3.2 especifica Poppins en títulos de la web e Inter en textos y botones. Se mantiene esta decisión específica.
2. **Color**: 4.1.1 identifica azul #1565c0 y verde #2e7d32 como semánticos generales; 4.3.2 usa azul #1976d2, verde #28a745 y CTA #176c37 en la web. Se mantienen tokens diferenciados.
3. **Audiencia**: 4.3.1 contiene una referencia incongruente a personas adultas mayores; 4.3.2 y las demás secciones se centran en estudiantes y personal de oficina. No se amplía el público por esa frase aislada.
4. **Navegación**: el sistema web de 4.1.2/4.2.4 enumera funciones diferentes de las etiquetas visibles en los mockups y la implementación. No se agregaron enlaces o secciones para corregirlo sin una decisión del equipo.

## Observaciones y límites

- El PNG original en `assets/images/brand/` mide 70 × 22 px, modo RGBA pero sin transparencia: el píxel superior izquierdo es blanco opaco. Se conserva como evidencia.
- En la cabecera y el pie se utiliza una **reconstrucción temporal en CSS y texto** del círculo y nombre de marca. No equivale al logotipo maestro de Figma; requiere aprobación o sustitución por el original.
- Las imágenes de 4.3.2 son capturas de UI de baja resolución. No justifican insertar ilustraciones ajenas; por ello no se incorporaron imágenes de stock ni contenido extra.
- El mapa, sus rutas y estimaciones son demostrativos, nunca recorridos de evacuación reales.
- El contacto no realiza envío remoto. La cobertura de 30 HU core y de los 100 escenarios no está certificada.
- La URL pública nueva `https://sismolisto.github.io/sismolisto-landing-page/` fue aportada por el usuario, pero el navegador del entorno no permite comprobarla; **no afirmar publicación de la revisión**.
- Las fuentes externas Poppins/Inter no se cargaron en el navegador aislado; la inspección visual corresponde a fallback.

## Referencias técnicas

- W3C. (2023). *Web Content Accessibility Guidelines (WCAG) 2.2*. https://www.w3.org/TR/WCAG22/
- Google. (s. f.). *Google HTML/CSS Style Guide*. https://google.github.io/styleguide/htmlcssguide.html
- Mozilla. (s. f.). *Responsive web design*. https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
