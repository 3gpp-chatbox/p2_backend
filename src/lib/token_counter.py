import os
import sys
from typing import Any

from dotenv import load_dotenv
from google import genai


def count_tokens_gemini(client: Any, model: str, contents: str) -> int:
    """
    Count tokens using the Gemini API directly.

    Args:
        client: The Gemini client instance
        model: The model name to use for token counting
        contents: The text content to count tokens for

    Returns:
        int: The number of tokens in the text
    """
    try:
        token = client.models.count_tokens(model=model, contents=contents)
        return token.total_tokens

    except Exception as e:
        print(f"Error: {e}")
        raise ValueError(f"Error in token counting: {e}")


if __name__ == "__main__":
    try:
        # Load environment variables
        load_dotenv()

        # Initialize Gemini client
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        model = "gemini-2.5-pro-exp-03-25"

        # Base content template
        base_content = """# Project Documentation
        
## Introduction
This document covers the technical specifications and implementation details of our system.
        
### Key Features
1. **Authentication & Authorization**
   - OAuth2.0 implementation
   - JWT token management
   - Role-based access control
        
2. **API Architecture**
   * RESTful endpoints
   * GraphQL interface
   * WebSocket support
        
## Code Examples
        
### Python Implementation
```python
def process_data(input_data: Dict[str, Any]) -> Result:
    try:
        validated_data = validate_input(input_data)
        result = transform_data(validated_data)
        return Result(success=True, data=result)
    except ValidationError as e:
        return Result(success=False, error=str(e))
```
        
### SQL Queries
```sql
SELECT 
    u.user_id,
    u.username,
    COUNT(t.transaction_id) as total_transactions
FROM users u
LEFT JOIN transactions t ON u.user_id = t.user_id
WHERE u.status = 'active'
GROUP BY u.user_id, u.username
HAVING COUNT(t.transaction_id) > 100;
```
        
## System Architecture
        
| Component | Technology | Purpose |
|-----------|------------|---------|
| Frontend | React.js | User Interface |
| Backend | FastAPI | API Server |
| Database | PostgreSQL | Data Storage |
| Cache | Redis | Performance |
        
### Performance Metrics
- Response Time: < 100ms
- Throughput: 1000 RPS
- Availability: 99.99%
        
## Implementation Notes
1. Use environment variables for configuration
2. Implement proper error handling
3. Follow the style guide:
   - Use type hints
   - Write docstrings
   - Add unit tests
        
> **Important**: Always follow security best practices and maintain comprehensive documentation.
        
### Mathematical Formulas
When calculating performance metrics:
- Latency = Processing Time + Network Delay
- Throughput = Requests / Time Unit
- Error Rate = (Failed Requests / Total Requests) * 100
        
## References
* [API Documentation](https://api.example.com/docs)
* [Style Guide](https://example.com/style-guide)
* [Security Policies](https://example.com/security)
"""

        # Generate large content by repeating and varying the base content
        sections = []
        for i in range(50):  # Repeat 50 times with variations
            section = base_content.replace(
                "Project Documentation", f"Project Documentation - Part {i + 1}"
            )
            section = section.replace(
                "Introduction", f"Introduction to Section {i + 1}"
            )
            section = section.replace("OAuth2.0", f"OAuth{i + 1}.0")
            section = section.replace("GraphQL", f"GraphQL{i + 1}")
            sections.append(section)

        # Join all sections with section breaks
        contents = "\n\n---\n\n".join(sections)

        # Count tokens using Gemini API
        print("Counting tokens for large content...")
        gemini_tokens = count_tokens_gemini(client, model, contents)
        print("\nToken count for ~100k tokens of content:")
        print(f"Gemini API token count: {gemini_tokens}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
