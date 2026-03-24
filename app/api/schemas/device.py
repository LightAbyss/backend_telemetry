from pydantic import BaseModel, Field, field_validator

class DeviceCreate(BaseModel):
    device_id: str = Field(..., min_length=1)
    firmware_version: str = Field(..., min_length=1)
    device_type: str = Field(..., min_length=1)
    description: str | None = Field(default=None)

    @field_validator("device_id", "firmware_version", "device_type", mode="before")
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

class DeviceCreateResponse(BaseModel):
    id: str
    device_id: str
    firmware_version: str
    device_type: str
    description: str | None