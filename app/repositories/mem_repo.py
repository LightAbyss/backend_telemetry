from .device_repo import DeviceRepository

from app.api.schemas.device import DeviceCreateResponse

class InMemDeviceRepository(DeviceRepository):
    def __init__(self):
        self._storage: dict[str, DeviceCreateResponse] = {}

    def register_device(self, device: DeviceCreateResponse) -> None:
        self._storage[device.device_id] = device

    def exists(self, device_id: str) -> bool:
        if device_id in self._storage:
            return True
        return False
    
    def find_by_id(self, device_id: str) -> DeviceCreateResponse | None:
        return self._storage.get(device_id)
    
    def list_all(self) -> list[DeviceCreateResponse]:
        return list(self._storage.values())