"""
MCP-facing tools for {{ cookiecutter.project_name }}.

Panel tools are optional, structured callables that the dj-control-room hub
can aggregate across every installed panel and expose through a unified API
(e.g. to an AI agent). Instantiate one ToolRegistry here, then decorate each
handler with @registry.register(...) so its metadata sits directly above the
function it describes.

Use local imports inside handlers for anything that touches Django models -
this keeps this module safe to import at any point in the Django startup
sequence.

See: https://yassi.github.io/dj-control-room-base/building-panels/#panel-tools
"""

from dj_control_room_base.core.panel_tool import (
    PanelToolContext,
    PanelToolResult,
    ToolRegistry,
)

registry = ToolRegistry()


@registry.register(
    name="hello_world",
    scope="hello",
    description=("Returns a simple 'Hello, World!' message."),
    input_schema={
        "type": "object",
        "properties": {},
        "additionalProperties": False,
    },
)
def handle_get_resolved_settings(ctx: PanelToolContext) -> PanelToolResult:
    """Return a simple 'Hello, World!' message."""
    return PanelToolResult(
        success=True,
        message="A simple 'Hello, World!' message.",
        data={"message": "Hello, World!"},
    )
