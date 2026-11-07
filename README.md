# SismoListo — Landing Page, corrección AV2

Implementación académica de SismoListo en HTML5, CSS3 y JavaScript básico. Se conserva la organización CSS modular, los recursos y la referencia a la guía del capítulo IV del informe TB1.

## Probar localmente

```bash
python -m http.server 8000
```
Abre `http://localhost:8000` en un navegador. Para pruebas automatizadas se requiere `pip install -r requirements-dev.txt` y `python -m playwright install chromium`. En el entorno de ejecución de este paquete, las pruebas se han realizado con montaje en memoria debido a restricciones de navegación local; no equivalen a pruebas de despliegue.

## Documentación

- `docs/ALCANCE_FUNCIONAL_Y_BRECHAS.md`: qué está corregido y qué sigue sin demostrarse.
- `docs/MATRIZ_50_HU_AV2.csv`: clasificación y resultados por HU.
- `docs/MATRIZ_100_ESCENARIOS_AV2.csv`: 100 criterios originales y evidencia diferenciada.
- `docs/INSTRUCCIONES_VSCODE_GITHUB.md`: integración sin sobrescribir el historial.

**Advertencia**: mapas, zonas, rutas y tiempos del sitio son ejemplos de entrenamiento NO validados para emergencias reales. No existe backend, autentificación ni sincronización remota.
