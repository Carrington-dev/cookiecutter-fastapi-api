import aioredis
from typing import Optional

redis: Optional[aioredis.Redis] = None

async def get_redis():
    global redis
    if not redis:
        redis = await aioredis.from_url("redis://localhost", decode_responses=True)
    return redis
