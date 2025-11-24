import json
from datetime import datetime, timezone
from app.models import Telemetry

# Mocking S3 upload: save to local folder
LOCAL_STORAGE_PATH = "local_s3"

import os
os.makedirs(LOCAL_STORAGE_PATH, exist_ok=True)

async def upload_to_s3(data: Telemetry):
    """
    Mock S3: Save telemetry JSON locally
    """
    now = datetime.now(timezone.utc)
    key = f"{now.year}_{now.month}_{now.day}_{data.device_id}_{data.timestamp}.json"
    file_path = os.path.join(LOCAL_STORAGE_PATH, key)

    with open(file_path, "w") as f:
        json.dump(data.model_dump(), f, indent=4)

    print(f"[Mock S3] Saved file: {file_path}")