# agent_core/interfaces/plugin.py

from abc import ABC, abstractmethod
from typing import Any, Dict

class PluginInterface(ABC):
    @abstractmethod
    def on_event(self, event_type: str, payload: Dict[str, Any]) -> None:
        """Handle an event from the system."""
        pass
