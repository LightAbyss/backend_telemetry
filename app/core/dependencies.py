from app.repositories.device_repo import DeviceRepository
from app.repositories.mem_repo import InMemDeviceRepository

_device_repository: DeviceRepository = InMemDeviceRepository()

def get_device_repository() -> DeviceRepository:
    return _device_repository