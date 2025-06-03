from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from src.lib.logger import logger
from src.schemas.models.agent import AgentCollection


class AgentManager:
    """
    Provides instances of AI agents (Gemini or OpenAI) based on environment
    variable configurations.
    """

    def __init__(self):
        """
        Initializes the AgentProvider by loading model configurations from
        environment variables.
        """
        logger.info("Initializing AgentProvider...")
        self.main_model_name = os.getenv("MAIN_MODEL")
        self.user_id = os.getenv("USER_ID")
        self.alt_model_name = os.getenv(
            "ALTERNATIVE_MODEL", None
        )  # Ensure None if not set
        self.alt_model_2_name = os.getenv("ALTERNATIVE_MODEL_2", None)
        self.temperature = float(os.getenv("MODEL_TEMPERATURE", 0.0))

        logger.info(f"MAIN_MODEL: {self.main_model_name}")
        logger.info(f"ALTERNATIVE_MODEL: {self.alt_model_name}")
        logger.info(f"ALTERNATIVE_MODEL_2: {self.alt_model_2_name}")
        logger.info(f"MODEL_TEMPERATURE: {self.temperature}")

        if not self.main_model_name:  # Only MAIN_MODEL is mandatory
            logger.error("MAIN_MODEL environment variable must be set.")
            raise ValueError("MAIN_MODEL environment variable must be set.")
        logger.info("AgentProvider initialized successfully.")

    def _create_agent(self, model_instance, temperature: float) -> Agent:
        """
        Helper method to create an Agent instance.

        Args:
            model_instance: The language model instance (e.g., GeminiModel, OpenAIModel).
            temperature: The temperature setting for the model.

        Returns:
            An Agent instance.
        """
        settings = {"temperature": temperature}

        # Add X-User-Id header if user_id is set
        if self.user_id:
            settings["extra_headers"] = {"X-User-Id": self.user_id}
        return Agent(
            model=model_instance,
            model_settings=settings,
        )

    def get_gemini_agents(self) -> AgentCollection:
        """
        Retrieves Gemini agents based on the environment configuration.

        Returns:
            An AgentCollection instance containing one to three Gemini Agent instances.

        Raises:
            ValueError: If model configurations are invalid or GEMINI_API_KEY is not set.
        """
        logger.info("Attempting to retrieve Gemini agents...")
        if not os.getenv("GEMINI_API_KEY"):
            logger.error(
                "GEMINI_API_KEY environment variable not set for Gemini models."
            )
            raise ValueError(
                "GEMINI_API_KEY environment variable must be set to use Gemini models."
            )

        logger.info(f"Creating main Gemini agent with model: {self.main_model_name}")
        main_model = GeminiModel(model_name=self.main_model_name, provider="google-gla")
        main_agent = self._create_agent(main_model, self.temperature)
        logger.info("Main Gemini agent created.")

        alt_agent_instance: Agent | None = None
        if self.alt_model_name:
            if self.main_model_name == self.alt_model_name:
                logger.error(
                    "MAIN_MODEL and ALTERNATIVE_MODEL for Gemini are the same."
                )
                raise ValueError(
                    "MAIN_MODEL and ALTERNATIVE_MODEL for Gemini must be different if ALTERNATIVE_MODEL is set."
                )
            logger.info(
                f"Creating alternative Gemini agent with model: {self.alt_model_name}"
            )
            alt_model = GeminiModel(
                model_name=self.alt_model_name, provider="google-gla"
            )
            alt_agent_instance = self._create_agent(alt_model, self.temperature)
            logger.info("Alternative Gemini agent created.")

        alt_agent_2_instance: Agent | None = None
        if self.alt_model_2_name:
            if self.alt_model_2_name == self.main_model_name:
                logger.error(
                    "ALTERNATIVE_MODEL_2 and MAIN_MODEL for Gemini are the same."
                )
                raise ValueError(
                    "ALTERNATIVE_MODEL_2 for Gemini must be different from MAIN_MODEL if set."
                )
            if self.alt_model_name and self.alt_model_2_name == self.alt_model_name:
                logger.error(
                    "ALTERNATIVE_MODEL_2 and ALTERNATIVE_MODEL for Gemini are the same."
                )
                raise ValueError(
                    "ALTERNATIVE_MODEL_2 for Gemini must be different from ALTERNATIVE_MODEL if both are set."
                )
            logger.info(
                f"Creating second alternative Gemini agent with model: {self.alt_model_2_name}"
            )
            alt_model_2 = GeminiModel(
                model_name=self.alt_model_2_name, provider="google-gla"
            )
            alt_agent_2_instance = self._create_agent(alt_model_2, self.temperature)
            logger.info("Second alternative Gemini agent created.")

        logger.info("Gemini agents retrieved successfully.")
        return AgentCollection(
            main_agent=main_agent,
            alt_agent=alt_agent_instance,
            alt_agent_2=alt_agent_2_instance,
        )

    def get_openai_agents(self) -> AgentCollection:
        """
        Retrieves OpenAI agents based on the environment configuration.
        Assumes MAIN_MODEL, ALTERNATIVE_MODEL, and ALTERNATIVE_MODEL_2 (optional)
        environment variables are used for OpenAI model names.

        Returns:
            An AgentCollection instance containing one to three OpenAI Agent instances.

        Raises:
            ValueError: If model configurations are invalid or OPENAI_API_KEY is not set.
        """
        logger.info("Attempting to retrieve OpenAI agents...")
        if not os.getenv("AZURE_OPENAI_API_KEY"):
            logger.error(
                "AZURE_OPENAI_API_KEY environment variable not set for OpenAI models."
            )
            raise ValueError(
                "AZURE_OPENAI_API_KEY environment variable must be set to use OpenAI models."
            )

        client = AsyncAzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        )

        logger.info(f"Creating main OpenAI agent with model: {self.main_model_name}")
        main_model = OpenAIModel(
            model_name=self.main_model_name,
            provider=OpenAIProvider(openai_client=client),
        )
        main_agent = self._create_agent(main_model, self.temperature)
        logger.info("Main OpenAI agent created.")

        alt_agent_instance: Agent | None = None
        if self.alt_model_name:
            if self.main_model_name == self.alt_model_name:
                logger.error(
                    "MAIN_MODEL and ALTERNATIVE_MODEL for OpenAI are the same."
                )
                raise ValueError(
                    "MAIN_MODEL and ALTERNATIVE_MODEL for OpenAI must be different if ALTERNATIVE_MODEL is set."
                )
            logger.info(
                f"Creating alternative OpenAI agent with model: {self.alt_model_name}"
            )
            alt_model = OpenAIModel(
                model_name=self.alt_model_name,
                provider=OpenAIProvider(openai_client=client),
            )
            alt_agent_instance = self._create_agent(alt_model, self.temperature)
            logger.info("Alternative OpenAI agent created.")

        alt_agent_2_instance: Agent | None = None
        if self.alt_model_2_name:
            if self.alt_model_2_name == self.main_model_name:
                logger.error(
                    "ALTERNATIVE_MODEL_2 and MAIN_MODEL for OpenAI are the same."
                )
                raise ValueError(
                    "ALTERNATIVE_MODEL_2 for OpenAI must be different from MAIN_MODEL if set."
                )
            if self.alt_model_name and self.alt_model_2_name == self.alt_model_name:
                logger.error(
                    "ALTERNATIVE_MODEL_2 and ALTERNATIVE_MODEL for OpenAI are the same."
                )
                raise ValueError(
                    "ALTERNATIVE_MODEL_2 for OpenAI must be different from ALTERNATIVE_MODEL if both are set."
                )
            logger.info(
                f"Creating second alternative OpenAI agent with model: {self.alt_model_2_name}"
            )
            alt_model_2 = OpenAIModel(
                model_name=self.alt_model_2_name,
                provider=OpenAIProvider(openai_client=client),
            )
            alt_agent_2_instance = self._create_agent(alt_model_2, self.temperature)
            logger.info("Second alternative OpenAI agent created.")

        logger.info("OpenAI agents retrieved successfully.")
        return AgentCollection(
            main_agent=main_agent,
            alt_agent=alt_agent_instance,
            alt_agent_2=alt_agent_2_instance,
        )


# Example of how to use the AgentProvider (optional, for demonstration)
if __name__ == "__main__":
    # This ensures .env is loaded if you run this file directly for testing
    load_dotenv()

    print("Attempting to initialize AgentProvider...")
    try:
        agent_provider = AgentManager()
        print("AgentProvider initialized.")

        print("\n--- Getting Gemini Agents ---")
        try:
            gemini_agents_collection = (
                agent_provider.get_gemini_agents()
            )  # No headers needed anymore
            print(
                f"Successfully retrieved Gemini agents. Main: {gemini_agents_collection.main_agent.model.model_name}"
            )
            if gemini_agents_collection.alt_agent:
                print(
                    f"  Gemini Agent Alt Model: {gemini_agents_collection.alt_agent.model.model_name}"
                )
            if gemini_agents_collection.alt_agent_2:
                print(
                    f"  Gemini Agent Alt 2 Model: {gemini_agents_collection.alt_agent_2.model.model_name}"
                )
        except ValueError as e:
            print(f"Error getting Gemini agents: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with Gemini agents: {e}")

        print("\n--- Getting OpenAI Agents ---")
        try:
            openai_agents_collection = (
                agent_provider.get_openai_agents()
            )  # No headers needed anymore
            print(
                f"Successfully retrieved OpenAI agents. Main: {openai_agents_collection.main_agent.model.model_name}"
            )
            if openai_agents_collection.alt_agent:
                print(
                    f"  OpenAI Agent Alt Model: {openai_agents_collection.alt_agent.model.model_name}"
                )
            if openai_agents_collection.alt_agent_2:
                print(
                    f"  OpenAI Agent Alt 2 Model: {openai_agents_collection.alt_agent_2.model.model_name}"
                )
        except ValueError as e:  # Catch ValueError for missing API key or other issues
            print(f"Error getting OpenAI agents: {e}")
        except Exception as e:
            print(f"An unexpected error occurred with OpenAI agents: {e}")

    except ValueError as e:
        print(f"Error initializing AgentProvider: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during AgentProvider initialization: {e}")
