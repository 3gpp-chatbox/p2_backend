import asyncio
import sys

from dotenv import load_dotenv
from fastapi import FastAPI

# Configure Windows-compatible event loop policy for async PostgreSQL
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from fastapi.middleware.cors import CORSMiddleware

from src.API.routes.delete_routes import router as delete_router
from src.API.routes.fetch_routes import router as fetch_router
from src.API.routes.insert_routes import router as insert_router
from src.lib.logger import setup_logger

app = FastAPI()

load_dotenv(override=True)

# Set up the logger
setup_logger()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the routers
app.include_router(fetch_router, prefix="/procedures")
app.include_router(insert_router, prefix="/procedures")
app.include_router(delete_router, prefix="/procedures")
