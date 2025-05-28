# agent_core/interfaces/tool.py

from abc import ABC, abstractmethod
from typing import Any, Dict

class ToolInterface(ABC):
    @abstractmethod
    def run(self, input_data: Dict[str, Any]) -> Any:
        """Run the tool with the given input data."""
        pass
