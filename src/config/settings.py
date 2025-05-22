import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings:
    """
    Configuration settings for the LLM Factory.
    """
    def __init__(self):
        """
        Initializes the settings, loading values from environment variables or providing defaults.
        """
        self.use_gateway: bool = os.getenv("USE_GATEWAY", "False").lower() == "true"
        """Whether to use an authenticated gateway for accessing LLMs."""
        self.gateway_url: Optional[str] = os.getenv("GATEWAY_URL")
        """The URL of the gateway, if used."""
        self.gateway_auth_method: str = os.getenv("GATEWAY_AUTH_METHOD", "api_key")
        """The authentication method for the gateway (e.g., "api_key", "oauth")."""
        # Add other settings as needed, e.g., default model name, API keys, etc.
        self.default_model: str = os.getenv("DEFAULT_MODEL", "gpt-3.5-turbo")
        """The default LLM model to use."""
        self.openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
        """OpenAI API key, if using OpenAI models directly."""

        # Example of additional settings with defaults
        self.max_tokens: int = int(os.getenv("MAX_TOKENS", "200"))
        """Maximum number of tokens for LLM responses."""
        self.temperature: float = float(os.getenv("TEMPERATURE", "0.7"))
        """Temperature setting for LLM responses."""

