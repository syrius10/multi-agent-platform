import pytest
from uuid import uuid4, UUID
from workflow_engine.models.task import Task

def test_create_task():
    task = Task(
        name="Summarize document",
        description="Use LLM to summarize",
        assigned_agent_id=uuid4(),
        inputs={"url": "https://example.com/article"}
    )

    assert isinstance(task.id, UUID)
    assert task.status == "pending"
    assert "url" in task.inputs
