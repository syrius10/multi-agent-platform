# agent_core/registry/agent_registry.py

from typing import Dict
from agent_core.base.agent import BaseAgent

class AgentRegistry:
    _registry: Dict[str, BaseAgent] = {}

    @classmethod
    def register(cls, agent_name: str, agent: BaseAgent):
        cls._registry[agent_name] = agent

    @classmethod
    def get(cls, agent_name: str) -> BaseAgent:
        if agent_name not in cls._registry:
            raise ValueError(f"Agent '{agent_name}' is not registered.")
        return cls._registry[agent_name]

    @classmethod
    def list_agents(cls):
        return list(cls._registry.keys())
