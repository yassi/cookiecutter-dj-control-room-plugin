"""
Tests for the MCP tools exposed via conf.py's `tools=tool_registry.tools`.
"""

from dj_control_room_base.core.panel_tool import PanelToolContext

from {{ cookiecutter.package_name }}.conf import panel_config
from {{ cookiecutter.package_name }}.tools import handle_hello_world

from .base import PanelTestCase


def _ctx(**inputs) -> PanelToolContext:
    return PanelToolContext(user=None, inputs=inputs, config=panel_config)


class TestHelloWorld(PanelTestCase):
    def test_returns_success(self):
        result = handle_hello_world(_ctx())
        self.assertTrue(result.success)
        self.assertEqual(result.data["message"], "Hello, World!")
