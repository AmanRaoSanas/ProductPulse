import json
import os
import boto3
from datetime import datetime, timezone
from app.models import Telemetry
from app.config import BUCKET_NAME, AWS_REGION, logger, MOCK_S3

if not MOCK_S3:
    s3_client = boto3.client("s3", region_name = AWS_REGION)

# Mocking S3 upload for local testing the logic by saving to local folder this code can be removed in future once AWS local testing setup
LOCAL_STORAGE_PATH = "local_s3"
os.makedirs(LOCAL_STORAGE_PATH, exist_ok=True)

async def upload_telemetry(data: Telemetry):
    try:
        now  = datetime.now(timezone.utc)
        key = f"{now.year}/{now.month}/{now.day}/{data.device_id}/{data.timestamp}.json"

        if MOCK_S3:
            # local save for testing
            filepath = os.path.join(LOCAL_STORAGE_PATH, f"{data.device_id}_{data.timestamp}.json")
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w") as f:
                json.dump(data.model_dump(), f)

        else:
            # actual S3 storing
            s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=key,
                Body=json.dumps(data.model_dump())
            )
            logger.info(f"Telemetry data uploaded successfully {data.device_id}")

    except Exception as e:
        logger.error(f"Telemetry data upload failed {e}")
        raise
