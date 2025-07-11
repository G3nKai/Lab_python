#main.py
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.Infrastructure.database import Base, engine
from src.Application.Controllers.PersonController import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    print("Tables created")
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)