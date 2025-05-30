from typing import Dict, Any
from langchain.llms import BaseLLM
from langchain.llms import OpenAI
# from langchain.llms import AzureOpenAI # Example for Azure OpenAI
# Add other LLM types as needed
from src.auth.gateway import GatewayAuthenticator  # Assuming a gateway authentication class
from src.config.settings import Settings  # Assuming a settings class to hold configurations


class LLMFactory_V1:
    """
    A factory class for creating and configuring Language Models (LLMs).
    Supports local models and authenticated gateway access.
    """

    def __init__(self, settings: Settings = None):
        """
        Initializes the LLMFactory with optional settings.

        Args:
            settings (Settings, optional): Configuration settings for LLMs. Defaults to None.
        """
        self.settings = settings or Settings()  # Load default settings if none provided
        self.gateway_authenticator = GatewayAuthenticator(self.settings) if self.settings.use_gateway else None

    def create_llm(self, model_name: str, params: Dict[str, Any] = None) -> BaseLLM:
        """
        Creates and configures an LLM instance based on the specified model name and parameters.

        Args:
            model_name (str): The name of the LLM to create (e.g., "gpt-3.5-turbo").
            params (Dict[str, Any], optional): A dictionary of parameters to configure the LLM. Defaults to None.

        Returns:
            BaseLLM: A configured instance of the specified LLM.

        Raises:
            ValueError: If the specified model is not supported or if gateway authentication fails.
        """
        if self.settings.use_gateway:
            # Authenticate with the gateway
            credentials = self.gateway_authenticator.authenticate()
            if not credentials:
                raise ValueError("Failed to authenticate with the gateway.")

            # Example: Assuming the gateway expects an API key
            # and the model name to be passed in the headers or as a query parameter
            gateway_url = self.settings.gateway_url
            headers = {"Authorization": f"Bearer {credentials.api_key}"}  # Example header
            params = params or {}
            params["model"] = model_name  # Pass model name as a parameter

            return self._create_llm_instance(model_name, gateway_url, params, headers=headers)
        else:
            # Local LLM creation
            return self._create_llm_instance(model_name, **(params or {}))

    def _create_llm_instance(self, model_name: str, base_url: str = None, params: Dict[str, Any] = None, headers: Dict[str, Any] = None) -> BaseLLM:
        """
        Creates a specific LLM instance based on the model name and provided parameters.

        Args:
            model_name (str): The name of the LLM to create.
            base_url (str, optional): The base URL for the LLM if it's accessed via a gateway. Defaults to None.
            params (Dict[str, Any], optional): A dictionary of parameters to configure the LLM. Defaults to None.
            headers (Dict[str, Any], optional): A dictionary of headers for gateway authentication. Defaults to None.

        Returns:
            BaseLLM: A configured instance of the specified LLM.

        Raises:
            ValueError: If the specified model is not supported.
        """
        if model_name.startswith("gpt"):  # Example: OpenAI models
            if base_url:  # Gateway access
                return OpenAI(
                    model_name=model_name,
                    openai_api_base=base_url,
                    openai_api_key=headers["Authorization"].split(" ")[1],  # Extract API key from header
                    **params
                )
            else:  # Local access
                return OpenAI(model_name=model_name, **params)
        # elif model_name.startswith("azure"):  # Example: Azure OpenAI
        #     return AzureOpenAI(
        #         model_name=model_name,
        #         openai_api_base=base_url,
        #         openai_api_key=headers["Authorization"].split(" ")[1],
        #         **params
        #     )
        else:
            raise ValueError(f"Unsupported model: {model_name}")