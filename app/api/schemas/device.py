from pydantic import BaseModel, Field

class DeviceCreate(BaseModel):
    device_id: str = Field(..., min_length=1)
    firmware_version: str = Field(..., min_length=1)
    device_type: str = Field(..., min_length=1)

class DeviceCreateResponse(BaseModel):
    id: str
    device_id: str
    firmware_version: str
    device_type: str