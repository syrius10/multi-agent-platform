from pydantic import BaseModel, Field
from typing import Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone

class Context(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    agent_id: UUID
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    memory: Dict[str, Any] = {}
    scratchpad: Dict[str, Any] = {}

    def get(self, key: str) -> Any:
        return self.memory.get(key)

    def set(self, key: str, value: Any) -> None:
        self.memory[key] = value
        self.updated_at = datetime.now(timezone.utc)
