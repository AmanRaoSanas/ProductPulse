import boto3
from app.config import logger, AWS_REGION, DYNAMODB_TABLE

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
TABLE_NAME = DYNAMODB_TABLE  # Table is created by terraform

def update_metadata(device_id: str, last_timestamp: str):
    try:
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={
            "device_id": device_id,
            "last_seen": last_timestamp
        })
        logger.info(f"Metadata updated for device: {device_id}")
    except Exception as e:
        logger.error(f"Metadata update failed: {e}")
