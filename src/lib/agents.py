from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import Optional

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI
from pydantic import BaseModel, Field, field_validator
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from src.lib.logger import logger
from src.schemas.models.agent import AgentCollection


# Provider-specific configurations
class BaseModelConfig(BaseModel):
    """Base configuration for all model providers."""

    main_model: str = Field(..., description="Name of the main model")
    alt_model: Optional[str] = Field(None, description="Name of the alternative model")
    alt_model_2: Optional[str] = Field(
        None, description="Name of the second alternative model"
    )

    @field_validator("alt_model")
    def validate_alt_model(cls, v, info):
        if v and v == info.data.get("main_model"):
            raise ValueError("Alternative model must be different from main model")
        return v

    @field_validator("alt_model_2")
    def validate_alt_model_2(cls, v, info):
        if v:
            if v == info.data.get("main_model"):
                raise ValueError(
                    "Alternative model 2 must be different from main model"
                )
            if v == info.data.get("alt_model"):
                raise ValueError(
                    "Alternative model 2 must be different from alternative model"
                )
        return v


class GeminiConfig(BaseModelConfig):
    """Configuration specific to Gemini models."""

    temperature: float = Field(0.0, ge=0.0, le=1.0, description="Model temperature")
    api_key: str = Field(..., description="Gemini API key")


class OpenAIConfig(BaseModelConfig):
    """Configuration specific to OpenAI models."""

    azure_endpoint: str = Field(..., description="Azure OpenAI endpoint")
    api_version: str = Field(..., description="Azure OpenAI API version")
    api_key: str = Field(..., description="Azure OpenAI API key")
    user_id: Optional[str] = Field(
        None, description="User ID for Azure API request headers"
    )
    temperature: float = Field(
        0.0, ge=0.0, le=1.0, description="Temperature for non-thinking models"
    )

    # Per-model reasoning effort settings
    main_reasoning_effort: Optional[str] = Field(
        None, description="Main model reasoning effort (low/medium/high/none)"
    )
    alt_reasoning_effort: Optional[str] = Field(
        None, description="Alternative model reasoning effort (low/medium/high/none)"
    )
    alt2_reasoning_effort: Optional[str] = Field(
        None, description="Alternative model 2 reasoning effort (low/medium/high/none)"
    )

    @field_validator(
        "main_reasoning_effort", "alt_reasoning_effort", "alt2_reasoning_effort"
    )
    def validate_reasoning_effort(cls, v):
        if v is None:
            return v
        valid_values = ["low", "medium", "high", "none"]
        if v.lower() not in valid_values:
            raise ValueError(f"reasoning_effort must be one of {valid_values}")
        return v.lower()


# Agent Builder Interface
class AgentBuilder(ABC):
    """Abstract base class for agent builders."""

    @abstractmethod
    def build_main_agent(self) -> Agent:
        """Build the main agent."""
        pass

    @abstractmethod
    def build_alternative_agent(self) -> Optional[Agent]:
        """Build the alternative agent if configured."""
        pass

    @abstractmethod
    def build_alternative_agent_2(self) -> Optional[Agent]:
        """Build the second alternative agent if configured."""
        pass

    @abstractmethod
    def build_collection(self) -> AgentCollection:
        """Build and return the complete agent collection."""
        pass


class GeminiAgentBuilder(AgentBuilder):
    """Builder for Gemini agents."""

    def __init__(self, config: GeminiConfig):
        self.config = config

    def _create_agent(self, model_name: str) -> Agent:
        """Helper method to create a Gemini agent."""
        settings = {"temperature": self.config.temperature}

        model = GeminiModel(model_name=model_name, provider="google-gla")
        return Agent(model=model, model_settings=settings)

    def build_main_agent(self) -> Agent:
        logger.info(f"Creating main Gemini agent with model: {self.config.main_model}")
        return self._create_agent(self.config.main_model)

    def build_alternative_agent(self) -> Optional[Agent]:
        if not self.config.alt_model:
            return None
        logger.info(
            f"Creating alternative Gemini agent with model: {self.config.alt_model}"
        )
        return self._create_agent(self.config.alt_model)

    def build_alternative_agent_2(self) -> Optional[Agent]:
        if not self.config.alt_model_2:
            return None
        logger.info(
            f"Creating second alternative Gemini agent with model: {self.config.alt_model_2}"
        )
        return self._create_agent(self.config.alt_model_2)

    def build_collection(self) -> AgentCollection:
        return AgentCollection(
            main_agent=self.build_main_agent(),
            alt_agent=self.build_alternative_agent(),
            alt_agent_2=self.build_alternative_agent_2(),
        )


class OpenAIAgentBuilder(AgentBuilder):
    """Builder for OpenAI agents."""

    def __init__(self, config: OpenAIConfig):
        self.config = config
        self.client = AsyncAzureOpenAI(
            azure_endpoint=config.azure_endpoint,
            api_version=config.api_version,
            api_key=config.api_key,
        )

    def _create_agent(
        self, model_name: str, reasoning_effort: Optional[str] = None
    ) -> Agent:
        """Helper method to create an OpenAI agent.

        Args:
            model_name: Name of the model to create
            reasoning_effort: Optional reasoning effort setting. If not None and not 'none',
                            will be included in the agent settings. If 'none' or None,
                            temperature will be used instead.
        """
        settings = {}
        if reasoning_effort and reasoning_effort.lower() != "none":
            settings["reasoning_effort"] = reasoning_effort.lower()
        else:
            # For non-thinking models, use temperature
            settings["temperature"] = self.config.temperature

        if self.config.user_id:
            settings["extra_headers"] = {"X-User-Id": self.config.user_id}

        model = OpenAIModel(
            model_name=model_name, provider=OpenAIProvider(openai_client=self.client)
        )
        return Agent(model=model, model_settings=settings)

    def build_main_agent(self) -> Agent:
        logger.info(f"Creating main OpenAI agent with model: {self.config.main_model}")
        return self._create_agent(
            self.config.main_model, self.config.main_reasoning_effort
        )

    def build_alternative_agent(self) -> Optional[Agent]:
        if not self.config.alt_model:
            return None
        logger.info(
            f"Creating alternative OpenAI agent with model: {self.config.alt_model}"
        )
        return self._create_agent(
            self.config.alt_model, self.config.alt_reasoning_effort
        )

    def build_alternative_agent_2(self) -> Optional[Agent]:
        if not self.config.alt_model_2:
            return None
        logger.info(
            f"Creating second alternative OpenAI agent with model: {self.config.alt_model_2}"
        )
        return self._create_agent(
            self.config.alt_model_2, self.config.alt2_reasoning_effort
        )

    def build_collection(self) -> AgentCollection:
        return AgentCollection(
            main_agent=self.build_main_agent(),
            alt_agent=self.build_alternative_agent(),
            alt_agent_2=self.build_alternative_agent_2(),
        )


class AgentManager:
    """
    Provides instances of AI agents (Gemini or OpenAI) based on environment
    variable configurations.
    """

    def __init__(self):
        """Initialize the AgentManager with configurations from environment variables."""
        logger.info("Initializing AgentManager...")
        load_dotenv()  # Ensure environment variables are loaded

        self.main_model = os.getenv("MAIN_MODEL")
        if not self.main_model:
            raise ValueError("MAIN_MODEL environment variable must be set")

    def get_gemini_agents(self) -> AgentCollection:
        """Build and return Gemini agents based on environment configuration."""
        try:
            config = GeminiConfig(
                main_model=self.main_model,
                alt_model=os.getenv("ALTERNATIVE_MODEL"),
                alt_model_2=os.getenv("ALTERNATIVE_MODEL_2"),
                temperature=float(os.getenv("MODEL_TEMPERATURE", "0.0")),
                api_key=os.getenv("GEMINI_API_KEY"),
            )
            builder = GeminiAgentBuilder(config)
            return builder.build_collection()
        except Exception as e:
            logger.error(f"Failed to create Gemini agents: {str(e)}")
            raise

    def get_openai_agents(self) -> AgentCollection:
        """Build and return OpenAI agents based on environment configuration."""
        try:
            config = OpenAIConfig(
                main_model=self.main_model,
                alt_model=os.getenv("ALTERNATIVE_MODEL"),
                alt_model_2=os.getenv("ALTERNATIVE_MODEL_2"),
                main_reasoning_effort=os.getenv("OPENAI_MAIN_REASONING_EFFORT"),
                alt_reasoning_effort=os.getenv("OPENAI_ALT_REASONING_EFFORT"),
                alt2_reasoning_effort=os.getenv("OPENAI_ALT2_REASONING_EFFORT"),
                temperature=float(os.getenv("MODEL_TEMPERATURE", "0.0")),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", ""),
                user_id=os.getenv("USER_ID"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION", ""),
                api_key=os.getenv("AZURE_OPENAI_API_KEY", ""),
            )
            builder = OpenAIAgentBuilder(config)
            return builder.build_collection()
        except Exception as e:
            logger.error(f"Failed to create OpenAI agents: {str(e)}")
            raise


if __name__ == "__main__":
    try:
        agent_manager = AgentManager()
        print("AgentManager initialized.")

        print("\n--- Getting Gemini Agents ---")
        try:
            gemini_agents = agent_manager.get_gemini_agents()
            print(
                f"Successfully retrieved Gemini agents. Main: {gemini_agents.main_agent.model.model_name}"
            )
            if gemini_agents.alt_agent:
                print(f"  Alt Model: {gemini_agents.alt_agent.model.model_name}")
            if gemini_agents.alt_agent_2:
                print(f"  Alt Model 2: {gemini_agents.alt_agent_2.model.model_name}")
        except Exception as e:
            print(f"Error getting Gemini agents: {e}")

        print("\n--- Getting OpenAI Agents ---")
        try:
            openai_agents = agent_manager.get_openai_agents()
            print(
                f"Successfully retrieved OpenAI agents. Main: {openai_agents.main_agent.model.model_name}"
            )
            if openai_agents.alt_agent:
                print(f"  Alt Model: {openai_agents.alt_agent.model.model_name}")
            if openai_agents.alt_agent_2:
                print(f"  Alt Model 2: {openai_agents.alt_agent_2.model.model_name}")
        except Exception as e:
            print(f"Error getting OpenAI agents: {e}")

    except Exception as e:
        print(f"Error: {e}")
