import redis.asyncio as redis
from app.config import logger, REDIS_HOST, REDIS_PORT

redis_client = None

async def init_redis():
    global redis_client
    redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    logger.info("Redis cache initialized successfully.")

async def set_cache(key: str, value: str, expire: int = 300):
    try:
        await redis_client.set(name=key, value=value, ex=expire)
        logger.info("cache set successfully")
    except Exception as e:
        logger.error(f"Redis set cache encountered error {e}")

async def get_cache(key: str):
    try:
        return await redis_client.get(key)
    except Exception as e:
        logger.error(f"Redis get cache encountered error {e}")
        return None