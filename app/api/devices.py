from fastapi import APIRouter, HTTPException, Depends

from app.api.schemas.device import DeviceCreate, DeviceCreateResponse
import app.services.device_service as dev_service
from app.repositories.device_repo import DeviceRepository
from app.core.dependencies import get_device_repository

router = APIRouter()

@router.post("/devices", status_code=201, response_model=DeviceCreateResponse)
def register_device(device: DeviceCreate, repo: DeviceRepository = Depends(get_device_repository)) -> DeviceCreateResponse:
    try:
        return dev_service.register_device(device, repo)

    except ValueError:
        raise HTTPException(status_code=409, detail="Device already registered")

@router.get("/devices/{device_id}", response_model=DeviceCreateResponse)
def get_device(device_id: str, repo: DeviceRepository = Depends(get_device_repository)) -> DeviceCreateResponse:
    try:
        return dev_service.get_device(device_id, repo)
    except ValueError:
        raise HTTPException(status_code=404, detail="Device not found")

@router.get("/devices", response_model=list[DeviceCreateResponse])
def list_devices(repo: DeviceRepository = Depends(get_device_repository)) -> list[DeviceCreateResponse]:
    return dev_service.list_devices(repo)