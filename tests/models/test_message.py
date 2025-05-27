import pytest
from uuid import uuid4, UUID
from agent_core.models.message import Message

def test_create_message():
    msg = Message(
        sender_id=uuid4(),
        receiver_id=uuid4(),
        content="Hello agent!",
        type="text",
        metadata={"priority": "high"}
    )

    assert isinstance(msg.id, UUID)
    assert msg.content == "Hello agent!"
    assert msg.type == "text"
    assert "priority" in msg.metadata
