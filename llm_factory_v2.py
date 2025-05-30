import logging
import os
import time
from typing import Any, Dict, List, Optional, Type, Union, Literal

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
from langchain_core.tools import BaseTool
from langchain_core.pydantic_v1 import BaseModel
from langgraph.prebuilt import create_react_agent


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class LLMFactory_v2:
    MAX_RETRIES = 3
    RETRY_DELAY = 30

    def __init__(self):
        """Init LLM Factory."""
        self.__llm_instances = {}
        self.__llm_token_fetcher = None
        self.__llm_token = None
    
    def get_llm(self, 
                acccess_method: Literal["local", "gateway", "api"] = "local", 
                llm_type: Literal["openai", "ollama"] = "openai",
                model_name: str = "gpt-4o",
                temperature: float = 0.7,
                streaming: bool = False,
                max_tokens: int = 4096,
                structured_output_model: Optional[Type[BaseModel]] = None,
                base_url: Optional[str] = None,
                **kwargs: Any
                ) -> BaseChatModel:
        """
        Get LLM instance based on specified parameters.
        This method creates and configures an LLM instance based on the specified access method, type, and parameters.
        
        Args:
            acccess_method (Literal["local", "gateway", "api"]): Access method for the LLM.
            llm_type (Literal["openai", "ollama"]): Type of LLM to use.
            model_name (str): Name of the model to use.
            temperature (float): Temperature setting for the model.
            streaming (bool): Whether to enable streaming.
            max_tokens (int): Maximum tokens for the model.
            structured_output_model (Optional[Type[BaseModel]]): Model for structured output.
            base_url (Optional[str]): Base URL for API calls.
            **kwargs: Additional keyword arguments.

        Returns:
            BaseChatModel: Configured LLM instance.
        """
        if acccess_method == "openai":
            return self.__get_openai_llm(model_name, params)
        elif acccess_method == "ollama":
            return self.__get_ollama_llm(model_name, params)
        else:
            raise ValueError(f"Unsupported access method: {acccess_method}")






