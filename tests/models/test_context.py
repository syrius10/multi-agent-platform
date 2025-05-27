import pytest
from uuid import uuid4, UUID
from memory_service.models.context import Context

def test_context_get_set():
    ctx = Context(agent_id=uuid4())
    ctx.set("topic", "AI agents")

    assert ctx.get("topic") == "AI agents"
    assert isinstance(ctx.updated_at.isoformat(), str)
