from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base
import asyncio
import os



engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_table())