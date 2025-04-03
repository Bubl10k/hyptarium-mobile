from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.setup import init_models
from app.routes.creation_router import router as creation_router
from app.routes.health_check_route import router as health_check_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=health_check_router)
app.include_router(router=creation_router)
