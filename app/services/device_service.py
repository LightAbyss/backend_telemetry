from uuid import uuid4

from app.api.schemas.device import DeviceCreate, DeviceCreateResponse
from app.repositories.device_repo import DeviceRepository

def register_device(device: DeviceCreate, repo: DeviceRepository) -> DeviceCreateResponse:
    if repo.exists(device.device_id):
        raise ValueError("Device already registered")

    new_id = str(uuid4())

    new_dev = DeviceCreateResponse(
        id=new_id,
        device_id=device.device_id,
        firmware_version=device.firmware_version,
        device_type=device.device_type,
        description=device.description
    )

    repo.register_device(new_dev)

    return new_dev

def get_device(device_id: str, repo: DeviceRepository) -> DeviceCreateResponse:
    device = repo.find_by_id(device_id)
    if not device:
        raise ValueError("Device not found")

    return device

def list_devices(repo: DeviceRepository) -> list[DeviceCreateResponse]:
    return repo.list_all()