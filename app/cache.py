import boto3
import time
from app.config import AWS_REGION, DYNAMODB_CACHE_TABLE, logger

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
cache_table = dynamodb.Table(DYNAMODB_CACHE_TABLE)

async def set_cache(key: str, value: str, expire: int = 300):
    try:
        ttl = int(time.time())+expire
        cache_table.put_item(Item={
            "cache_key": key,
            "cache_value": value,
            "ttl_timestamp": ttl
        })
        logger.info("Cache stored successfully")
    except Exception as e:
        logger.error(f"Cache set error {e}")

async def get_cache(key:str):
    try:
        result = cache_table.get_item(Key={"cache_key":key})
        return result.get("Item", {}).get("cache_value")
    except Exception as e:
        logger.error(f"Cache get error {e}")
