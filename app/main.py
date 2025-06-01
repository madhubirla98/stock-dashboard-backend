from fastapi import FastAPI
from app.routes import stocks
import app.config  # Initialize Firebase
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()

app.include_router(stocks.router, prefix="/api")
