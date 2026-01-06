from fastapi import FastAPI
from app.api.routes import router 
from app.core.config import settings
from app.core.logging import setup_logging
from contextlib import asynccontextmanager
import logging

setup_logging(settings.log_level)
logger = logging.getLogger(__name__)

@asynccontextmanager
#I use FastAPI lifespan handlers to manage startup and shutdown of GenAI resources like vector stores and model clients.
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting GenAI RAG Service")
    yield
    # Shutdown
    logger.info("Shutting down GenAI RAG Service")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,   
    lifespan=lifespan   
)

app.include_router(router)

