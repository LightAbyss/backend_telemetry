# Backend Telemetry

## Objetivo
Proveer un backend para recibir, almacenar y consultar telemetría proveniente de dispositivos embebidos.

## Instalación

1. Clonar este proyecto:
```bash
git clone https://github.com/LightAbyss/backend_telemetry.git
cd backend_telemetry
```

2. Instalar las dependencias utilizando `uv`
```bash
uv sync
```

## Ejecutar servidor
Una vez instaladas las dependencias, se puede lanzar el servidor con el comando:
```bash
uv run uvicorn app.main:app
```

Para ejecutar el servidor, y que este detecte cambios en el código se utiliza:
```bash
uv run uvicorn app.main:app --reload
```

## Endpoints disponibles

### `/health`
Permite verificar que la aplicación está en ejecución y respondiendo correctamente.

## Estructura inicial

- `app/main.py`: punto de entrada de la aplicación
- `app/api/`: routers y endpoints
- `tests/`: pruebas del proyecto
