# Texto de trabajo para incorporar al informe AV2 (sin afirmar despliegue)

## 5.1.3. Source Code Style Guide & Coding Conventions

Para el Landing Page de SismoListo se emplean HTML5 para la estructura semántica de las vistas y formularios, CSS3 para la presentación responsive y JavaScript para interacciones de la demostración. Los nombres técnicos de rutas, carpetas, archivos y funciones se expresan en inglés, conforme a las convenciones del Final Project Statement V4 (p. 18). El código organiza los estilos en módulos independientes por responsabilidad: `css/base`, `css/components`, `css/sections` y `css/features`. Los valores compartidos de color, tipografía, espaciado y radios se centralizan en `css/base/tokens.css` y se aplican a los componentes que corresponden con las decisiones del capítulo IV del TB1. Se mantiene el uso de HTML semántico, etiquetas de formularios y roles ARIA cuando resultan necesarios. Los cambios propuestos no alteran los identificadores HU del informe y conservan la arquitectura modular.

La ejecución local con Chromium aislado verificó que los archivos CSS y JavaScript son accesibles en el proyecto y que los flujos seleccionados no produjeron errores JavaScript durante las pruebas indicadas. Estas comprobaciones no constituyen una auditoría WCAG 2.2 AA completa ni validan una versión desplegada.

## 5.1.4. Software Deployment Configuration

Se dispone de un proyecto estático listo para publicación web, compuesto por `index.html`, directorios `css/`, `js/` y `assets/`. El repositorio de destino es `https://github.com/JeferSomBlan/sismolisto-landing-page`. La publicación está **PENDIENTE**: no existe evidencia verificable de una URL pública para esta versión. Como procedimiento de despliegue, tras revisar la rama de funcionalidad y fusionar un Pull Request hacia `develop`, el equipo deberá preparar su versión aprobada y publicar desde una rama admitida por GitHub Pages o el servicio que acuerde. Deberán registrarse la configuración, URL, fecha, capturas en escritorio y móvil y pruebas de navegación sobre la URL pública. No debe documentarse una simulación local como despliegue concluido.

## 5.2.X.1. Sprint Backlog

La versión corregida aborda incidencias funcionales relacionadas con HU-032, HU-034, HU-037, HU-038, HU-039, HU-040, HU-043, HU-045, HU-046, HU-047, HU-049 y HU-050. Para su inclusión en el Sprint Backlog del equipo deberán consignarse, usando datos verificados del tablero, IDs de work-items, responsables, estimaciones, estados y URL pública del tablero. No se han inventado horas, responsables ni estados de sprints no accesibles.

## 5.2.X.2. User Interface & Execution

Se elaboró y probó una implementación web modular que conserva la composición informativa del capítulo IV de SismoListo. La demostración permite evaluar ambientes ficticios, registrar riesgos, visualizar zonas y rutas ilustrativas, resolver micro-simulacros y consultar progreso local. Se prepararon capturas a 1440, 768 y 390 px. Las pruebas automatizadas disponibles y sus resultados se adjuntan como logs y no equivalen a validar 30 HU core. La verificación sobre la URL pública y el video de ejecución son PENDIENTES.

## 5.2.X.3. Team Collaboration Insights

El repositorio público se configuró con `main`, `develop` y una rama de documentación; se pudo verificar un Pull Request anterior sobre convenciones. Sin embargo, esta corrección de código no se ha subido mediante un nuevo Pull Request. Para completar esta sección debe conservarse la evidencia real de ramas, commits, Pull Requests y aportes de integrantes. No se atribuyen contribuciones de terceros sin historial verificado.

## 6.1. Acceptance Tests (preparación)

Se adjuntan archivos `.feature` derivados de los criterios Gherkin originales para 23 HU candidatas. Son especificaciones sin definiciones ejecutables de pasos y no se consideran pruebas superadas. La matriz CSV identifica resultados de inspección y pruebas puntuales con Playwright; una futura entrega debe enlazar el repositorio de pruebas y documentar las ejecuciones reales.
