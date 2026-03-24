from fastapi import APIRouter, HTTPException

from app.api.schemas.device import DeviceCreate, DeviceCreateResponse
import app.services.device_service as dev_service

router = APIRouter()

@router.post("/devices", status_code=201, response_model=DeviceCreateResponse)
def register_device(device: DeviceCreate) -> DeviceCreateResponse:
    try:
        return dev_service.register_device(device)

    except ValueError:
        raise HTTPException(status_code=409, detail="Device already registered")

@router.get("/devices/{device_id}", response_model=DeviceCreateResponse)
def get_device(device_id: str) -> DeviceCreateResponse:
    try:
        return dev_service.get_device(device_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Device not found")

@router.get("/devices", response_model=list[DeviceCreateResponse])
def list_devices() -> list[DeviceCreateResponse]:
    return dev_service.list_devices()