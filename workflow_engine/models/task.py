from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone

class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    assigned_agent_id: Optional[UUID] = None
    status: str = "pending"
    inputs: Dict[str, Any] = {}
    outputs: Optional[Dict[str, Any]] = None
