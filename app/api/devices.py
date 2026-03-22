from fastapi import APIRouter, HTTPException
from uuid import uuid4

from app.api.schemas.device import DeviceCreate, DeviceCreateResponse

router = APIRouter()

# In-memory storage for registered devices
registered_devices: dict[str, DeviceCreateResponse] = {}

@router.post("/devices", status_code=201, response_model=DeviceCreateResponse)
def register_device(device: DeviceCreate) -> DeviceCreateResponse:
    if device.device_id in registered_devices:
        raise HTTPException(status_code=409, detail="Device already registered")

    new_id = str(uuid4())

    registered_devices[device.device_id] = DeviceCreateResponse(
        id=new_id,
        device_id=device.device_id,
        firmware_version=device.firmware_version,
        device_type=device.device_type
    )

    return registered_devices[device.device_id]

@router.get("/devices/{device_id}", response_model=DeviceCreateResponse)
def get_device(device_id: str) -> DeviceCreateResponse:
    if device_id not in registered_devices:
        raise HTTPException(status_code=404, detail="Device not found")

    return registered_devices[device_id]

@router.get("/devices", response_model=list[DeviceCreateResponse])
def list_devices() -> list[DeviceCreateResponse]:
    return list(registered_devices.values())