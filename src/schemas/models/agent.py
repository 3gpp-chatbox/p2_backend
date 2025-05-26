from typing import Any, Optional

from pydantic import BaseModel, ConfigDict
from pydantic_ai import Agent


# Define a Pydantic model to hold the agents
class AgentCollection(BaseModel):
    main_agent: Any  # Using Any here since Agent will be validated at runtime
    alt_agent: Optional[Any] = None
    alt_agent_2: Optional[Any] = None

    model_config = ConfigDict(arbitrary_types_allowed=True, validate_assignment=True)

    def __init__(self, **data):
        super().__init__(**data)
        if not isinstance(self.main_agent, Agent):
            raise ValueError("main_agent must be an Agent")
        if self.alt_agent is not None and not isinstance(self.alt_agent, Agent):
            raise ValueError("alt_agent must be None or an Agent")
        if self.alt_agent_2 is not None and not isinstance(self.alt_agent_2, Agent):
            raise ValueError("alt_agent_2 must be None or an Agent")
