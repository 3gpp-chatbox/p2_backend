import json
import logging
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Enable CORS - allow both localhost and 127.0.0.1
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent.resolve()

# Paths - using absolute paths based on script location
MOCK_DATA_PATH = SCRIPT_DIR / "data" / "mock_pydantic" / "mockstep3.json"
EDITED_DATA_PATH = (
    SCRIPT_DIR.parent / "frontend" / "src" / "assets" / "edited_mock.json"
)


@app.get("/")
async def root():
    """Root endpoint for testing connection"""
    return {"status": "ok", "message": "Server is running"}


@app.get("/api/mock-data")
async def get_mock_data():
    """Fetch mock data from mockstep3.json"""
    try:
        logger.info(f"Attempting to read mock data from: {MOCK_DATA_PATH}")

        if not MOCK_DATA_PATH.exists():
            logger.error(f"Mock data file not found at: {MOCK_DATA_PATH}")
            raise HTTPException(
                status_code=404,
                detail=f"Mock data file not found at path: {MOCK_DATA_PATH}",
            )

        with open(MOCK_DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Successfully loaded mock data")
            return data

    except FileNotFoundError as e:
        logger.error(f"File not found error: {str(e)}")
        raise HTTPException(
            status_code=404,
            detail=f"Mock data file not found at path: {MOCK_DATA_PATH}",
        )
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Invalid JSON in mock data file: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error reading mock data: {str(e)}"
        )


@app.post("/api/save-edit")
async def save_edit(data: dict):
    """Save edited data to edited_mock.json"""
    try:
        # Create parent directories if they don't exist
        EDITED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

        logger.info(f"Attempting to save edited data to: {EDITED_DATA_PATH}")
        with open(EDITED_DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info("Successfully saved edited data")
        return {"message": f"Data saved successfully to {EDITED_DATA_PATH}"}
    except Exception as e:
        logger.error(f"Error saving data: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Failed to save edited data: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting server...")
    logger.info(f"Mock data will be read from: {MOCK_DATA_PATH}")
    logger.info(f"Edited data will be saved to: {EDITED_DATA_PATH}")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
