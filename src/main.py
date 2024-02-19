import asyncio

from database import sync_engine, async_engine
from sqlalchemy import text
from config import settings


async def get_version():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(res.first())

if __name__ == '__main__':
    asyncio.run(get_version())

