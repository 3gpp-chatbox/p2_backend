"""
Wrapper script to control which extraction method to use based on environment variable.
"""

import asyncio
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

# Add parent directory to Python path
sys.path.append(str(Path(__file__).parents[2].resolve()))

from src.extraction.extract_procedure import main as extract_with_accuracy
from src.extraction.extract_procedure_simple import main as extract_without_accuracy
from src.lib.logger import get_logger

logger = get_logger(__name__)

# Set Windows event loop policy
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    try:
        # Load environment variables
        load_dotenv(override=True)
        
        # Get accuracy checking configuration
        USE_ACCURACY_CHECKING = os.getenv("USE_ACCURACY_CHECKING", "0") == "1"
        
        if USE_ACCURACY_CHECKING:
            logger.info("Running extraction with accuracy checking...")
            await extract_with_accuracy()
        else:
            logger.info("Running simplified extraction without accuracy checking...")
            await extract_without_accuracy()
            
    except Exception as e:
        logger.error(f"Error in extraction wrapper: {e}")
        raise

if __name__ == "__main__":
    asyncio.run(main()) 