import boto3
from botocore.exceptions import ClientError
from app.config import logger, AWS_REGION

dynamodb = boto3.resource("dynamodb", region_name = AWS_REGION)
TABLE_NAME = "TelemetryMetadata"

def init_table():
    try:
        table = dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[{"AttributeName":"device_id", "KeyType":"HASH"}],
            AttributeDefinitions=[{"AttributeName": "device_id", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST",
        )
        table.wait_until_exists()
        logger.info(f"DynamoDB table {TABLE_NAME} created successfully")

    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            logger.info(f"DynamoDB table {TABLE_NAME} already exists")
        else:
            logger.error(f"Error occurred while creating dynamodb table {e}")
            raise

def update_metadata(device_id: str, last_timestamp: str):
    try:
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={
            "device_id": device_id,
            "last_seen": last_timestamp
        })
        logger.info(f"Metadata updated for device: {device_id}")
    except Exception as e:
        logger.error(f"Metadat update failed {e}")
