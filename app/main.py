from cgitb import handler

from fastapi import FastAPI
from app.models import Telemetry
from app.s3_utils import upload_to_s3
from mangum import Mangum

app = FastAPI(title="ProductPulse")

@app.get("/")
async def root():
    return {"message": "ProductPulse Phase 1 Backend is Running"}

@app.post("/telemetry")
async def telemetry_ingestion(data:Telemetry):

    await upload_to_s3(data)
    return {"status": "Success", "device_id": data.device_id}

handler = Mangum(app)