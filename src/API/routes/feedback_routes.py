import sys
from pathlib import Path
from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[3].resolve()))
from src.API.pydantic_models import FeedbackCreate, FeedbackItem, FeedbackResolve
from src.db.db_handler import DatabaseHandler
from src.lib.logger import get_logger

logger = get_logger(__name__)
router = APIRouter()

@router.post("/", response_model=FeedbackItem)
async def create_feedback(feedback: FeedbackCreate):
    """
    Create new feedback for a graph.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            INSERT INTO feedback (graph_id, comment, user_email, feedback_type)
            VALUES (%s, %s, %s, %s)
            RETURNING id, graph_id, comment, 
                     TO_CHAR(created_at, 'DD-MM-YYYY HH24:MI') as created_at,
                     user_email, status, feedback_type
            """
            parameters = (feedback.graph_id, feedback.comment, feedback.user_email, feedback.feedback_type)
            result = db.execute_query(query, parameters)
            
            if not result:
                raise HTTPException(status_code=500, detail="Failed to create feedback")
            
            return FeedbackItem(**result[0])

    except Exception as e:
        logger.error(f"Failed to create feedback: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to create feedback: {str(e)}")

@router.get("/graph/{graph_id}", response_model=List[FeedbackItem])
async def get_feedback_for_graph(graph_id: UUID):
    """
    Get all feedback for a specific graph.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT id, graph_id, comment, 
                   TO_CHAR(created_at, 'DD-MM-YYYY HH24:MI') as created_at,
                   user_email, status, feedback_type, resolution_reason
            FROM feedback
            WHERE graph_id = %s
            ORDER BY created_at DESC
            """
            results = db.execute_query(query, (graph_id,))
            
            return [FeedbackItem(**row) for row in results]

    except Exception as e:
        logger.error(f"Failed to fetch feedback: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch feedback: {str(e)}")

@router.get("/admin/all", response_model=List[FeedbackItem])
async def get_all_feedback():
    """
    Get all feedback (admin endpoint).
    """
    try:
        with DatabaseHandler() as db:
            query = """
            SELECT id, graph_id, comment, 
                   TO_CHAR(created_at, 'DD-MM-YYYY HH24:MI') as created_at,
                   user_email, status, feedback_type, resolution_reason
            FROM feedback
            ORDER BY created_at DESC
            """
            results = db.execute_query(query)
            
            return [FeedbackItem(**row) for row in results]

    except Exception as e:
        logger.error(f"Failed to fetch all feedback: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch all feedback: {str(e)}")

@router.post("/resolve", response_model=FeedbackItem)
async def resolve_feedback(resolution: FeedbackResolve):
    """
    Resolve a feedback item with a reason.
    """
    try:
        with DatabaseHandler() as db:
            query = """
            UPDATE feedback 
            SET status = 'resolved', resolution_reason = %s
            WHERE id = %s
            RETURNING id, graph_id, comment, 
                     TO_CHAR(created_at, 'DD-MM-YYYY HH24:MI') as created_at,
                     user_email, status, resolution_reason, feedback_type
            """
            parameters = (resolution.resolution_reason, resolution.feedback_id)
            result = db.execute_query(query, parameters)
            
            if not result:
                raise HTTPException(status_code=404, detail="Feedback not found")
            
            return FeedbackItem(**result[0])

    except Exception as e:
        logger.error(f"Failed to resolve feedback: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to resolve feedback: {str(e)}") 