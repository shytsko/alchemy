from config import settings
from sqlalchemy import create_engine, URL, Text
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

sync_engine = create_engine(url=settings.db_url_psycopg, echo=True, pool_size=5, max_overflow=10)
async_engine = create_async_engine(url=settings.db_url_asyncpg, echo=True, pool_size=5, max_overflow=10)