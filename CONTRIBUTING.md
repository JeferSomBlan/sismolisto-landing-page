# Guía de contribución — SismoListo Landing Page

Este documento establece las convenciones de colaboración para el código del Landing Page de SismoListo (UPC, IHC y Tecnologías Móviles, 2026-2). Se trata de las reglas propuestas para el repositorio; su cumplimiento deberá acreditarse con ramas, commits y pull requests reales.

## Estrategia de ramas: GitFlow

| Rama | Finalidad | Regla |
| --- | --- | --- |
| `main` | Mantener versiones publicables y aprobadas | Integrar cambios provenientes de `release/*` o `hotfix/*` tras revisión. |
| `develop` | Integrar funcionalidad en desarrollo | Recibir pull requests de `feature/*`. |
| `feature/<identificador>-<descripcion>` | Desarrollar una capacidad concreta | Nacer de `develop` y regresar a `develop` mediante pull request. |
| `release/<version>` | Preparar una versión | Nacer de `develop`; revisar, integrar en `main` y devolver correcciones a `develop`. |
| `hotfix/<version>-<descripcion>` | Corregir incidencias urgentes de producción | Nacer de `main` y reintegrarse a `main` y `develop`. |

Ejemplos de nombres válidos: `feature/hu-031-environment-assessment`, `feature/responsive-navigation`, `release/1.0.0`, `hotfix/1.0.1-navigation-fix`.

**Nota:** los ejemplos anteriores son nombres de referencia; no indican que esas ramas ya hayan sido creadas. Las ramas `release/*` y `hotfix/*` se crearán únicamente cuando exista una publicación o incidencia que las justifique.

## Proceso de colaboración

1. Actualizar la rama `develop`.
2. Crear una rama `feature/*` para una tarea o historia de usuario concreta.
3. Desarrollar y verificar los cambios en esa rama.
4. Registrar commits descriptivos según Conventional Commits.
5. Abrir un pull request hacia `develop`, indicando HU involucradas, alcance y pruebas realizadas.
6. Revisar los cambios antes de fusionarlos.
7. Preparar una rama `release/*` cuando una versión esté lista para aceptación y publicación.

## Mensajes de commit: Conventional Commits

Formato: `<tipo>(<alcance opcional>): <descripción en inglés>`.

Tipos principales: `feat` (capacidad), `fix` (corrección), `docs` (documentación), `style` (formato sin cambio funcional), `refactor` (reestructuración), `test` (pruebas), `chore` (mantenimiento).

Ejemplos:
- `docs: define source control conventions`
- `feat(navigation): add responsive header`
- `fix(forms): preserve entered values on validation error`
- `test(hu-031): add environment assessment scenarios`

No se debe declarar una prueba superada sin registro de ejecución.

## Versiones: Semantic Versioning

Utilizar `MAJOR.MINOR.PATCH` para las publicaciones: `MAJOR` ante cambios incompatibles, `MINOR` ante nuevas capacidades compatibles y `PATCH` ante correcciones compatibles. Las etiquetas de versión llevarán el prefijo `v` (por ejemplo `v1.0.0`). El repositorio no debe publicarse bajo una versión que aún no haya sido preparada y validada.

## Identificadores y estilo

- Conservar la nomenclatura `HU-001` a `HU-050` definida por el informe del proyecto.
- Utilizar nombres técnicos en inglés para rutas, archivos, funciones y ramas.
- Documentar en cada pull request las HU relacionadas y el alcance implementado o simulado.
- No incorporar datos personales, credenciales ni claves de API en commits.
- Mantener la estructura HTML/CSS responsive y las decisiones UX/UI de la guía aprobada.

## Estado inicial de adopción

La existencia de este archivo acredita la definición de convenciones, pero **no** demuestra por sí sola la ejecución de GitFlow, la participación de colaboradores o la publicación de releases. Esas actividades requieren evidencia independiente en GitHub.
