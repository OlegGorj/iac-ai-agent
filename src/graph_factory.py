import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.language_models import BaseChatModel, BaseLLM
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import BaseTool
from typing_extensions import Self

from analyzer import Analyzer


class GraphFactory(ABC):
    """
    This is an abstract class that represents a factory for creating a langgraph runnable.
    """

    def __init__(self, recursion_limit: int):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.analyzer = Analyzer(temperature=0.5)  # Initialize the Analyzer object

        self.runnable_config: RunnableConfig = {
            "recursion_limit": recursion_limit,
            "max_concurrency": 10,
        }
        self.graph = self.build()

        self._tools = []
        self._chat_prompt = None
        self._agent_executor_cfg = {}
        self._llm: Optional[BaseChatModel] = None

    @abstractmethod
    def build(self, *args, **kwargs):
        pass

    # Utility functions for the derived classes

    def _agent_executor(self, **kwargs) -> AgentExecutor:
        tools = self._tools
        if "tools" in kwargs:
            tools = kwargs.pop("tools")
        if not tools:
            tools = []
        agent = create_openai_tools_agent(self._llm, tools, self._chat_prompt)
        return AgentExecutor(
            tools=tools,
            agent=agent,
            **self._agent_executor_cfg,
            **kwargs,
        )

    def tools(self, tools: List[BaseTool]) -> Self:
        self._tools = tools
        return self

    def chat_prompt(self, chat_prompt) -> Self:
        self._chat_prompt = chat_prompt
        return self

    def agent_executor_cfg(self, agent_executor_cfg: Dict) -> Self:
        self._agent_executor_cfg = agent_executor_cfg
        return self

    def llm(self, llm: BaseLLM) -> Self:
        self._llm = llm
        return self
    
    