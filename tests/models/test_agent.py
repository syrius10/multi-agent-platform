import pytest
from uuid import UUID
from agent_core.models import Agent
def test_create_agent():
    agent = Agent(
        name="ResearcherBot",
        role="researcher",
        description="Finds latest papers on a topic",
        goals=["gather information", "summarize content"],
        capabilities=["web_search", "summarization"],
        metadata={"team": "science"}
    )

    assert isinstance(agent.id, UUID)
    assert agent.name == "ResearcherBot"
    assert "summarization" in agent.capabilities
