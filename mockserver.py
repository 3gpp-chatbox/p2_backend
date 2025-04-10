import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
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


@app.get("/api/mock-data")
async def get_mock_data():
    """Fetch mock data from mockstep3.json"""
    try:
        print(f"Attempting to read mock data from: {MOCK_DATA_PATH}")  # Debug line
        with open(MOCK_DATA_PATH, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail=f"Mock data file not found at path: {MOCK_DATA_PATH}",
        )
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON in mock data file")


@app.post("/api/save-edit")
async def save_edit(data: dict):
    """Save edited data to edited_mock.json"""
    try:
        # Create parent directories if they don't exist
        EDITED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

        print(f"Attempting to save edited data to: {EDITED_DATA_PATH}")  # Debug line
        with open(EDITED_DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return {"message": f"Data saved successfully to {EDITED_DATA_PATH}"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to save edited data: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn

    print(f"Mock data will be read from: {MOCK_DATA_PATH}")
    print(f"Edited data will be saved to: {EDITED_DATA_PATH}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
