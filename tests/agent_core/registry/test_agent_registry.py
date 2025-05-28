# tests/agent_core/registry/test_agent_registry.py

from agent_core.registry.agent_registry import AgentRegistry
from agent_core.base.agent import BaseAgent
from agent_core.models.agent import Agent
from agent_core.models.message import Message
from memory_service.models.context import ExecutionContext
from workflow_engine.models.task import Task

class DummyAgent(BaseAgent):
    def execute(self, task: Task, context: ExecutionContext) -> Message:
        # Use the task and context parameters to avoid the "not accessed" warning
        return Message(sender="Dummy", recipient="System", content=f"Test for task: {task.id} with context ID: {context.id}")

def test_agent_registry_register_and_get():
    agent_name = "DummyAgent"
    dummy = DummyAgent(Agent(name="DummyAgent", role="x", description="x", goals=[], capabilities=[], metadata={}))

    AgentRegistry.register(agent_name, dummy)
    fetched = AgentRegistry.get(agent_name)

    assert isinstance(fetched, BaseAgent)
    assert fetched.schema.name == agent_name

def test_agent_registry_list():
    agents = AgentRegistry.list_agents()
    assert isinstance(agents, list)
