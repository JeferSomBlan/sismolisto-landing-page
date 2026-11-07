# 5.1.2. Source Code Management — Registro técnico de SismoListo

**Curso:** 1ASI0385 — IHC y Tecnologías Móviles, UPC, 2026-2 (NRC 16734)  
**Producto:** SismoListo  
**Repositorio de Landing Page:** https://github.com/JeferSomBlan/sismolisto-landing-page  
**Documento normativo:** `UPC-PRE-202620-1ASI0385-Final-Project-Statement_V4.pdf`, página 18.

## Repositorio y control de versiones

El equipo utiliza Git y GitHub como herramientas propuestas para registrar y rastrear las modificaciones del Landing Page. El repositorio señalado es público. Al inicio de esta preparación se observó una rama `main` y un archivo `README.md`, sin código HTML/CSS incorporado; la implementación funcional se encuentra pendiente de evidencia. La URL de las pruebas de aceptación (`.feature`) también está pendiente de definirse o verificarse.

## Flujo de trabajo acordado o por adoptar

Se propone **GitFlow** para separar la rama estable `main`, la integración `develop` y el desarrollo de funcionalidades mediante ramas `feature/*`. Cuando corresponda se crearán ramas `release/*` y `hotfix/*`. Cada rama de funcionalidad debe relacionarse con una tarea o historia de usuario y consolidarse a través de pull requests revisados. El detalle de convenciones se encuentra en `CONTRIBUTING.md`.

Ejemplo de secuencia verificable:
1. Crear `develop` desde `main`.
2. Crear `feature/source-code-management` desde `develop`.
3. Incorporar la documentación y registrar un commit `docs: define source control conventions`.
4. Abrir un pull request hacia `develop`.
5. Revisar el pull request y fusionarlo cuando se apruebe.

Los pasos que no cuenten con rama, commit o PR observables permanecen como **PENDIENTES** y no deben describirse como ejecución ya realizada.

## Convenciones de commits y versiones

Los commits seguirán Conventional Commits, usando términos técnicos en inglés: `feat`, `fix`, `docs`, `test`, `refactor`, `style` y `chore` según corresponda. Las publicaciones emplearán Semantic Versioning `MAJOR.MINOR.PATCH`; los tags se crearán únicamente al existir una versión real lista para publicación.

## Matriz de evidencias para el informe

| Evidencia | Qué mostrar en GitHub | Estado inicial |
| --- | --- | --- |
| E1. Repositorio | Página `Code`, propietario, nombre, visibilidad y URL | COMPROBADO |
| E2. Ramas | Selector de ramas que muestre `main` y `develop` | PENDIENTE |
| E3. Rama feature | Rama `feature/source-code-management` | PENDIENTE |
| E4. Commit | Historial y mensaje conforme a Conventional Commits | PENDIENTE |
| E5. Pull request | PR de feature a `develop` y su estado | PENDIENTE |
| E6. Versiones | Tag o release si efectivamente se publicó una versión | NO APLICA POR AHORA |
| E7. Pruebas | Repositorio o ruta con archivos `.feature` reales | PENDIENTE |

**Importante:** esta tabla debe actualizarse al terminar cada tarea, con URL y captura de evidencia. No reutilizar el estado inicial como evidencia de fases posteriores.

## Referencias metodológicas

Driessen, V. (2010, 5 de enero). *A successful Git branching model*. https://nvie.com/posts/a-successful-git-branching-model/

Conventional Commits. (s. f.). *Conventional Commits 1.0.0*. https://www.conventionalcommits.org/en/v1.0.0/

Preston-Werner, T. (s. f.). *Semantic Versioning 2.0.0*. https://semver.org/spec/v2.0.0.html

**Observación:** las referencias se han incluido como documentación de estándares. Su correspondencia bibliográfica debe confirmarse cuando se integre la sección al informe APA 7 final.
