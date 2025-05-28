# agent_core/registry/tool_registry.py

from typing import Dict, Callable

class ToolRegistry:
    _registry: Dict[str, Callable] = {}

    @classmethod
    def register(cls, tool_name: str, tool_callable: Callable):
        cls._registry[tool_name] = tool_callable

    @classmethod
    def get(cls, tool_name: str) -> Callable:
        if tool_name not in cls._registry:
            raise ValueError(f"Tool '{tool_name}' is not registered.")
        return cls._registry[tool_name]

    @classmethod
    def list_tools(cls):
        return list(cls._registry.keys())
