# Git, Visual Studio Code y despliegue — SismoListo

**Estado verificado en GitHub el 7 de noviembre de 2026:**
- Repositorio web público: https://github.com/JeferSomBlan/sismolisto-landing-page
- Ramas `main`, `develop` y `feature/source-code-management` registradas.
- PR #1 fusionado hacia `develop`: https://github.com/JeferSomBlan/sismolisto-landing-page/pull/1
- Repositorio de pruebas de aceptación: https://github.com/JeferSomBlan/sismolisto-acceptance-tests (sin `.feature` verificados en esta revisión).
- **El código web de este paquete se generó y probó localmente. No se ha publicado aún en esos repositorios.** La integración conectada de GitHub permitió consultar pero devolvió 403 al intentar crear ramas y PR.

## Integración desde Visual Studio Code

1. Abrir VS Code → Terminal → Nueva terminal.
2. Clonar y entrar al repositorio:

```bash
git clone https://github.com/JeferSomBlan/sismolisto-landing-page.git
cd sismolisto-landing-page
git switch develop
git pull origin develop
git switch -c feature/landing-page-core
```

3. Copiar el contenido de **este paquete** a la carpeta clonada, conservando los archivos ya existentes `README.md`/`CONTRIBUTING.md` cuando sea necesario; sustituir README solo después de comparar versiones.
4. Abrir el proyecto (`code .`) e iniciar servidor local:

```bash
python -m http.server 5500
```

5. Navegar a `http://localhost:5500`. Revisar los pasos de `docs/PRUEBAS.md`.
6. Revisar cambios antes del commit:

```bash
git status
git diff --check
git add index.html css/ js/ assets/ docs/ tests/ README.md .gitignore
git commit -m "feat(web): implement SismoListo core interaction demo"
git push -u origin feature/landing-page-core
```

7. En GitHub, abrir Pull Request: **base `develop`** ← compare `feature/landing-page-core`. Revisar los cambios y fusionar solo después de validarlos.
8. La publicación estable se hará desde una rama `release/x.y.z`, fusionando a `main` tras validaciones y creando entonces el tag correspondiente; no declarar una release antes de ese hecho.

## Despliegue futuro (5.1.4)

Una vez fusionada y aprobada la versión, se puede publicar un sitio estático mediante GitHub Pages desde la rama preparada para publicación y su raíz. Comprobar disponibilidad/configuración de Pages en `Settings > Pages`, elegir el origen autorizado por el equipo y esperar una URL mostrada por GitHub. **No se proporciona URL de despliegue no verificada.** Confirmar que `index.html`, todos los módulos de `css/` y `js/app.js` cargan con rutas relativas; ensayar en viewport desktop (1440 px), tableta (768 px) y móvil (390 px). La URL real y la fecha de publicación se registran solamente cuando estén comprobadas.

## Evidencias requeridas (sección 5.2.X)

- Capturas de `Code`, ramas, comparación, commits y PR real.
- Pantallas funcionales desktop y mobile de los recorridos core y sus alternativas.
- Video de navegación y ejecución de un sprint, con enlace publicado.
- Tablero del sprint, HU, tareas, estimación en horas, responsable y estado reales; no inventar tareas terminadas.
- Captura del despliegue público cuando exista.

## Convenciones

Véase `CONTRIBUTING.md` existente en GitHub (`develop`). Los nombres técnicos de archivo, rama y commit se mantienen en inglés. Historias y narrativas se redactan en español.
