# tests/agent_core/base/test_agent.py

from uuid import uuid4
from agent_core.base.agent import BaseAgent
from agent_core.models.agent import Agent
from agent_core.models.message import Message
from memory_service.models.context import ExecutionContext
from workflow_engine.models.task import Task

class DummyAgent(BaseAgent):
    def execute(self, task: Task, context: ExecutionContext) -> Message:
        # Use both task and context parameters
        task_info = f"Executed task: {task.name} with inputs: {task.inputs} in context: {context.task_id}"
        return Message(sender_id=uuid4(), receiver_id=uuid4(), content=task_info)

def test_agent_execution():
    agent = DummyAgent(
        Agent(
            name="Dummy",
            role="tester",
            description="A dummy test agent",
            goals=["test"],
            capabilities=["none"],
            metadata={}
        )
    )

    task = Task(id=uuid4(), name="Sample Task", inputs={"key": "value"})
    context = ExecutionContext(task_id=task.id, session_id=uuid4(), metadata={})
    result = agent.execute(task, context)

    assert isinstance(result, Message)
    assert "Executed task: Sample Task" in result.content
    assert "inputs: {'key': 'value'}" in result.content
    assert f"in context: {context.task_id}" in result.content
