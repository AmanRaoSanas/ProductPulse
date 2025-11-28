from fastapi import FastAPI, HTTPException
from mangum import Mangum
from models import Telemetry
from s3_utils import upload_telemetry
from cache import set_cache
from meta import update_metadata
from config import logger
import json

app = FastAPI(title="ProductPulse")

@app.get("/")
async def root():
    return {"message": "ProductPulse Phase 1 Backend is Running"}

@app.post("/telemetry")
async def telemetry_ingestion(data:Telemetry):
    try:
        logger.info(f"Telemetry data received: {data}")

        # actual data
        await upload_telemetry(data)
        # caching latest data
        await set_cache(f"last_telemetry_data:{data.device_id}", json.dumps(data.model_dump()))
        # storing metadata
        update_metadata(data.device_id, data.timestamp)

        logger.info(f"Telemetry data uploaded successfully: {data.device_id}")
        return {"status": "Success", "device_id": data.device_id}

    except Exception as e:
        logger.error(f"Error during uploading telemetry data {e}")
        raise HTTPException(status_code=500, detail='Internal server error')


handler = Mangum(app)