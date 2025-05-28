# tests/agent_core/registry/test_tool_registry.py

from agent_core.registry.tool_registry import ToolRegistry

def dummy_tool(input_data):
    # Using the input_data parameter in a meaningful way
    return f"ok: {input_data}"

def test_tool_registry_register_and_get():
    ToolRegistry.register("dummy", dummy_tool)
    tool = ToolRegistry.get("dummy")

    assert tool("test") == "ok: test"

def test_tool_registry_list():
    tools = ToolRegistry.list_tools()
    assert "dummy" in tools
