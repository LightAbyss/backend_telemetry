from pydantic import BaseModel, Field, field_validator
import re

class DeviceBase(BaseModel):
    device_id: str = Field(..., min_length=1)
    firmware_version: str = Field(...)
    device_type: str = Field(..., min_length=1)
    description: str | None = Field(None)

    @field_validator("device_id", "device_type", mode="before")
    def normalize_and_validate_string(cls, value) -> str:
        if value is None:
            raise ValueError("Must not be null")
        
        if not isinstance(value, str):
            raise ValueError("Must be a string")
        
        new_value = value.strip()

        if len(new_value) > 0:
            return new_value
        else:
            raise ValueError("Must not be empty or whitespace")

    @field_validator("firmware_version", mode="before")
    def validate_firmware_version(cls, value) -> str:
        if value is None:
            raise ValueError("Must not be null")
        
        if not isinstance(value, str):
            raise ValueError("Must be a string")
        
        new_value = value.strip()

        if len(new_value) == 0:
            raise ValueError("Must not be empty or whitespace")

        if not re.match(r"^\d+\.\d+(\.\d+)?$", new_value):
            raise ValueError("Must be in the format 'X.Y' or 'X.Y.Z' where X, Y, Z are numbers")
        
        return new_value

    @field_validator("description", mode="before")
    def normalize_description(cls, value) -> str | None:
        if value is None:
            return None
        
        if not isinstance(value, str):
            raise ValueError("Must be a string")
        
        new_value = value.strip()

        if len(new_value) > 0:
            return new_value
        else:
            raise ValueError("Must not be empty or whitespace")


class DeviceCreate(DeviceBase):
    pass
    
class DeviceCreateResponse(DeviceBase):
    id: str