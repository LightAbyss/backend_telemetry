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

### `/devices`
Permite registrar un dispositivo en el sistema.
**Método**: POST
**Body**:
```json
{
	'device_id': 'str',
	'firmware_version' : 'X.Y.Z',
	'device_type': 'str',
	'description': 'str'
}
```
**Response**:
```json
{
	'device_id': 'str',
	'firmware_version' : 'X.Y.Z',
	'device_type': 'str',
	'description': 'str',
	'id': 'str'
}
```
### `/devices/{device_id}`
Permite consultar los datos de un dispositivo registrado a partir de su `device_id`.
**Método**: GET
**Response**:
```json
{
	'device_id': 'str',
	'firmware_version' : 'X.Y.Z',
	'device_type': 'str',
	'description': 'str',
	'id': 'str'
}
```

### `/devices`
Enlista todos los dispositivos registrados
**Método**: GET
**Response**:
```json
[
	{
		'device_id': 'str',
		'firmware_version' : 'X.Y.Z',
		'device_type': 'str',
		'description': 'str',
		'id': 'str'
	},
	...
]
```

## Estructura inicial

- `app/main.py`: punto de entrada de la aplicación
- `app/api/`: routers y endpoints
- `tests/`: pruebas del proyecto
