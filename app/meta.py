import boto3
from config import logger, AWS_REGION, DYNAMODB_METADATA_TABLE

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
metadata_table = dynamodb.Table(DYNAMODB_METADATA_TABLE)

def update_metadata(device_id: str, last_timestamp: str):
    try:
        metadata_table.put_item(Item={
            "device_id": device_id,
            "last_seen": last_timestamp
        })
        logger.info(f"Metadata updated for device: {device_id}")
    except Exception as e:
        logger.error(f"Metadata update failed: {e}")
