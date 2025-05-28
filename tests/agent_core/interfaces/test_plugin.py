# tests/agent_core/interfaces/test_plugin.py

from agent_core.interfaces.plugin import PluginInterface

class DummyPlugin(PluginInterface):
    def on_event(self, event_type, payload):
        self.last_event = (event_type, payload)

def test_plugin_interface():
    plugin = DummyPlugin()
    plugin.on_event("event_x", {"foo": "bar"})

    assert plugin.last_event[0] == "event_x"
    assert plugin.last_event[1]["foo"] == "bar"
