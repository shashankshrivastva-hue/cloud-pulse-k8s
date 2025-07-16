"""FastAPI monitoring & telemetry endpoint."""
from fastapi import FastAPI
from pydantic import BaseModel
from ..controller.reconciler import AutoscalerReconciler

app = FastAPI(title="CloudPulse K8s Controller API")
reconciler = AutoscalerReconciler()

class TelemetryPayload(BaseModel):
    deployment: str
    cpu_percent: float

@app.get("/health")
def health():
    return {"status": "operational", "reconciler": "active"}

@app.post("/api/v1/telemetry")
def submit_telemetry(payload: TelemetryPayload):
    return reconciler.step(payload.deployment, payload.cpu_percent)
