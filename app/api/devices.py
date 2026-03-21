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