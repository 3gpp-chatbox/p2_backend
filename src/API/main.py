import sys
from pathlib import Path

from fastapi import FastAPI

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))
from fastapi.middleware.cors import CORSMiddleware

from src.API.routes.fetch_routes import router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the router
app.include_router(router, prefix="/procedures")
