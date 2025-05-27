from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone

class Message(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    sender_id: UUID
    receiver_id: Optional[UUID] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    content: str
    type: str = "text"
    metadata: Dict[str, Any] = {}
