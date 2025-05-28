# agent_core/base/agent.py

from abc import ABC, abstractmethod
from agent_core.models.agent import Agent
from agent_core.models.message import Message
from memory_service.models.context import ExecutionContext
from workflow_engine.models.task import Task

class BaseAgent(ABC):
    def __init__(self, agent_schema: Agent):
        self.schema = agent_schema

    @abstractmethod
    def execute(self, task: Task, context: ExecutionContext) -> Message:
        """Execute the given task within the given context."""
        pass

    def receive_message(self, message: Message):
        """Handle incoming messages."""
        raise NotImplementedError(f"Message handling not implemented for this agent. Received message: {message}")
