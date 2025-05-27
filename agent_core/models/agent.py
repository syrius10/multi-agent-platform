from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from uuid import UUID, uuid4

class Agent(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    role: str
    description: Optional[str] = None
    goals: List[str] = []
    capabilities: List[str] = []
    metadata: Dict[str, str] = {}
