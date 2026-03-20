from fastapi import FastAPI

from app.core.config import Settings
from app.api.health import router as health_router
from app.api.devices import router as devices_router

config = Settings()
app = FastAPI(title=config.app_name)
app.include_router(health_router)
app.include_router(devices_router)