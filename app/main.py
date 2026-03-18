from fastapi import FastAPI

app = FastAPI(title="Backend Telemetry")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
