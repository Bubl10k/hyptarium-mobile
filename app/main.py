from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.database.setup import init_models
from app.routes.health_check_route import router as health_check_router
from app.routes.user_route import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router=health_check_router)
app.include_router(router=user_router)
