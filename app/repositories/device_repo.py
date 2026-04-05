from abc import ABC, abstractmethod

from app.api.schemas.device import DeviceCreateResponse

class DeviceRepository(ABC):
    @abstractmethod
    def register_device(self, device: DeviceCreateResponse) -> None:
        ...

    @abstractmethod
    def exists(self, device_id: str) -> bool:
        ...

    @abstractmethod
    def find_by_id(self, device_id: str) -> DeviceCreateResponse:
        ...

    @abstractmethod
    def list_all(self) -> list[DeviceCreateResponse]:
        ...