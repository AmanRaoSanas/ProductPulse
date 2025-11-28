import json
import os
import boto3
from datetime import datetime, timezone
from models import Telemetry
from config import BUCKET_NAME, AWS_REGION, logger

s3_client = boto3.client("s3", region_name = AWS_REGION)

async def upload_telemetry(data: Telemetry):
    try:
        now  = datetime.now(timezone.utc)
        key = f"{now.year}/{now.month}/{now.day}/{data.device_id}/{data.timestamp}.json"

        s3_client.put_object(
                Bucket=BUCKET_NAME,
                Key=key,
                Body=json.dumps(data.model_dump())
            )
        logger.info(f"Telemetry data uploaded successfully {data.device_id}")

    except Exception as e:
        logger.error(f"Telemetry data upload failed {e}")
        raise