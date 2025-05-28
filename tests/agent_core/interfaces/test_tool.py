# tests/agent_core/interfaces/test_tool.py

from agent_core.interfaces.tool import ToolInterface

class DummyTool(ToolInterface):
    def run(self, input_data):
        return input_data.get("x", 0) + 1

def test_tool_interface():
    tool = DummyTool()
    result = tool.run({"x": 2})
    assert result == 3
