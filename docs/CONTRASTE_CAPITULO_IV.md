# Contraste verificable — capítulo IV del TB1 y Landing Page

**Alcance:** revisión documental + corrección visual del código existente. **No** constituye inspección del archivo editable Figma ni equivalencia píxel por píxel. Las fuentes originales permanecen intactas.

**Fuentes:** SismoListo TB1 (PDF/DOCX), pp. 88–92, 94–102; guía Final Project Statement V4, pp. 14–19 y 28; materiales de UI, usabilidad, IA y diseño inclusivo del curso. Figuras originales reproducidas en `docs/referencias-visuales/` tomadas de las imágenes incrustadas del DOCX.

## Resolución de divergencias normativas/documentales

1. **Tipografía:** 4.1.1 (p. 89) indica Inter para el sistema general, mientras 4.3.2 (p. 100) especifica *Poppins* en títulos web e *Inter* en cuerpo/botones. Para el Landing Page se aplica la regla específica de 4.3.2, respetando la general en UI. La fuente Poppins se solicita mediante Google Fonts; si el proveedor no responde, se usa la alternativa declarada. No se distribuyen binarios.
2. **Colores:** 4.1.1 (pp. 90–91) define azul `#1565C0`, verde `#2E7D32`, amarillo/naranja `#F57C00`, rojo `#D32F2F` y texto `#212121`. En 4.3.2 (p. 100) la web utiliza azul `#1976D2`, verde `#28A745` y CTA verde oscuro `#176C37`. Se asignaron variables web y otras semánticas (riesgo/seguridad) diferenciadas. Las capturas muestran también botones azules, divergencia que sigue sin aprobación explícita del equipo; para el CTA principal se adoptó la indicación textual específica de 4.3.2.
3. **Navegación:** 4.1.2 (p. 92) propone para web Inicio/Preparación/Zonas Seguras/Alertas/Perfil; el wireframe web 4.3.1 (p. 99) y mockups web (pp. 100–101) presentan Inicio/Problema/Cómo funciona/Simulacros/Beneficios/Recursos/Contacto. Se adopta la navegación **particular del Landing Page** para evitar fusionar menú de app móvil/dashboard con página de marketing.
4. **Header y autenticación:** el mockup muestra «Iniciar sesión» y «Crear cuenta», pero el proyecto actual carece de backend. Como 4.3.2 (p. 100) reconoce elementos visuales no funcionales, no se añadieron controles de login fingidos; se conserva el CTA existente «Comenzar mi preparación» que dirige a la demostración local. **Divergencia funcional pendiente de decisión del equipo.**
5. **Logo:** el mockup integra una marca circular azul. Se sustituyó la «S» inventada por un **recorte real del mockup** original (baja resolución); el original editable/vectorial no está disponible. No se afirma equivalencia en alta resolución.
6. **Footer:** el wireframe 4.3.1 (p. 99) representa un fondo turquesa, sin código cromático oficial específico. Se utilizó un fondo gris claro de la familia neutral para conservar legibilidad del logotipo azul recuperado. La tonalidad final del footer permanece **NO COMPROBADA**.

## Matriz de elementos

| Elemento | Evidencia capítulo IV | Estado anterior | Corrección / resultado | Estado después |
|---|---|---|---|---|
| Identidad del logotipo | Mockups web pp. 100–101: círculo azul + SismoListo | Insignia «S» de elaboración propia | Sustituida por imagen recortada del mockup original | CUMPLE parcialmente; resolución original pendiente |
| Header | Wireframe p. 99 y mockups p. 100 | Logo tipográfico, estructura más pesada | Header blanco compacto y composición simplificada | CUMPLE en estructura general; no pixel-perfect |
| Navbar | P. 99: Inicio, Problema, Cómo funciona, Simulacros, Beneficios, Recursos, Contacto | Faltaban Inicio/Beneficios; «Funcionalidades» reemplazaba enlaces | Etiquetas y orden del wireframe, sin eliminar sección de funcionalidades | CUMPLE, salvo menú de autenticación pendiente |
| Hero | Wireframe p. 99: título, CTA doble y visual de apoyo a la derecha | Fondo degradado y tarjeta muy elevada | Fondo blanco, proporción, márgenes y sombra reducida; textos conservados | CUMPLE en composición general |
| Tipografía web | 4.3.2 p. 100: Poppins headings, Inter cuerpo | Inter/sistema en todo | Variables para Poppins + Inter; enlace al proveedor | CUMPLE configuracional; descarga real NO COMPROBADA |
| Paleta de marca | 4.3.2 p. 100: `#1976D2`, `#28A745`, `#176C37` | Azul `#1565C0`, verde `#2E7D32` como identidad | Variables de web diferenciadas de estados semánticos | CUMPLE definición; revisar todos los componentes secundarias |
| Espaciado | 4.1.1 pp. 90–91: escala de 8 px | Varios gaps arbitrarios | Tokens 4/8/16/24/32/48; se normalizaron las secciones principales | PARCIAL: no todas las medidas heredadas son múltiplos de 8 |
| Radios | 4.1.1 p. 91: cards 12 px, botones 8–12 px | Cards 15 px; hero 19 px | Radios de 12 px en tarjetas principales y 10 px en CTA | CUMPLE en áreas corregidas |
| CTA | 4.3.2 p.100 texto recomienda verde oscuro, mockup muestra azules | CTA principal azul | CTA principal verde oscuro con hover/focus/disabled | CUMPLE regla textual; divergencia visual documentada |
| Estados | 4.1.1 p. 91: default/hover/focus/disabled | Focus/disabled parciales | Se completaron estados de botones/inputs | PARCIAL: auditoría de todos los estados pendiente |
| Simulacros | Mockup incrustado 4.3.2 p.101, 3 tarjetas y botón de prueba | Tres tarjetas funcionales existentes | Se mantuvieron estructura de tres escenarios y mejoras de color; no se inventaron | CUMPLE en estructura general; no idéntico al original |
| Beneficios | Mockup incrustado pp. 99–101, tarjetas, etiquetas por segmento | Caja con lista de viñetas | Tarjetas visuales filtrables, preservando las tres ventajas existentes | PARCIAL: mockup presenta cuatro tarjetas, la fuente funcional actual solo acredita tres |
| Recursos y FAQ | Wireframe p.99 + 4.3.2 p.100: tres recursos y FAQ | Recursos y FAQ funcionales existentes | Se preservan, sin nuevas preguntas ni recursos | CUMPLE en cobertura básica; composición exacta pendiente |
| Contacto | Wireframe p.99 | Borrador copiable (sin envío) | Se preserva para no simular envío; validación de campos | PARCIAL: comportamiento no equivale a servicio final |
| Footer | Wireframe p.99, pie de secciones y enlaces | Pie azul oscuro con «S» distinta | Pie claro con logo fuente, sin enlaces nuevos | NO COMPROBADO en tonalidad/layout final |
| Responsive | 4.1.2 p. 92 | CSS con puntos 590/800/1080 | Se añadieron bandas precisas 320–767, 768–1023, ≥1024 | CUMPLE en anchuras medidas; navegadores reales por verificar |
| Funcionalidad core | Guía p. 16–17 y 28, mínimo 30 HU core | Demostración parcial local | Se conserva JS existente sin nuevas HU | NO COMPROBADO 30 HU core completas |

## Comparaciones visuales

- `evidence/comparacion-simulacros.jpg` y `evidence/comparacion-beneficios.jpg` en el paquete de evidencias.
- Las imágenes originales son capturas de baja resolución incrustadas en el DOCX, no frames vectoriales.
- Las capturas actuales se generaron en Chromium aislado; no equivalen a verificación del enlace público.

**Criterios aplicados de IHC:** consistencia y estándares (navegación/identidad), reconocimiento antes que recuerdo (etiquetas), visibilidad del estado (enlace actual), prevención y recuperación de errores (formularios existentes), y legibilidad y diseño inclusivo (foco y contraste). No se crearon funcionalidades nuevas para exhibir estas heurísticas.
