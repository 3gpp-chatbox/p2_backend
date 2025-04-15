# API Instructions

## Prerequisites

- setup the postgresql db
- create tables (src/db/table.sql and graph_table.sql)
- insert data (src/db dummy data.sql and /retrieval store_chunks.py and /extraction store_graphs.py)

## Setup Instructions

1. **Create and activate virtual environment**
   ```powershell
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment (Windows)
   .\venv\Scripts\activate
   ```

2. **Install dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Environment Variables**
   Create a `.env` file in the root directory with the following variables. Here an example:
   ```
    DB_HOST=localhost
    DB_NAME=postgres
    DB_USER=postgres
    DB_PASSWORD="your_ password"
    DB_PORT=5433
   ```

## Running the API

1. **Start the FastAPI server**
   ```powershell
   # Development mode with auto-reload
   src.API.main:app --reload 
  
2. **Access the API Documentation**
   - Swagger UI: http://localhost:8000/docs

