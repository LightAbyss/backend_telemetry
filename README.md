# Backend Telemetry

## Objetivo
Proveer un servidor que pueda adquirir la telemetría de diferentes dispositivos de sistemas embebidos.

## Instalación

1. Clonar este proyecto:
```bash
git clone https://github.com/LightAbyss/backend_telemetry.git
```

2. Instalar las dependencias
  1. Utilizando uv
  ```bash
  uv sync
  ```

  2. Utilizando pip
  ```bash
  pip install -e .
  ```

## Ejecutar servidor
Una vez instaladas las dependencias, se puede lanzar el servidor con el comando:
```bash
uv run uvicorn app.main:app
```

Para ejecutar el servidor, y que este detecte cambios en el código se utiliza:
```bash
uv  run uvicorn app.main:app --reload
```

## Endpoints disponibles

### /health
Permite comprobar que el servidor se esté ejecutando de forma adecuada y reciba los mensajes.
