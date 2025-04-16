import sys
from pathlib import Path

from fastapi import FastAPI

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))
from fastapi.middleware.cors import CORSMiddleware

from src.API.routes.fetch_routes import router as fetch_router
from src.API.routes.insert_routes import router as insert_router

app = FastAPI()

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
