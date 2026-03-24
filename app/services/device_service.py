from uuid import uuid4

from app.api.schemas.device import DeviceCreate, DeviceCreateResponse

# In-memory storage for registered devices
registered_devices: dict[str, DeviceCreateResponse] = {}

def register_device(device: DeviceCreate) -> DeviceCreateResponse:
    if device.device_id in registered_devices:
        raise ValueError("Device already registered")

    new_id = str(uuid4())

    registered_devices[device.device_id] = DeviceCreateResponse(
        id=new_id,
        device_id=device.device_id,
        firmware_version=device.firmware_version,
        device_type=device.device_type
    )

    return registered_devices[device.device_id]

def get_device(device_id: str) -> DeviceCreateResponse:
    if device_id not in registered_devices:
        raise ValueError("Device not found")

    return registered_devices[device_id]

def list_devices() -> list[DeviceCreateResponse]:
    return list(registered_devices.values())