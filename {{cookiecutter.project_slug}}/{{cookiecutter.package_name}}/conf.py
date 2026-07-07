from dj_control_room_base.core import PanelConfig

from .tools import registry as tool_registry

panel_config = PanelConfig(
    settings_key="{{ cookiecutter.package_name|upper }}_SETTINGS",
    defaults={
        "LOAD_DEFAULT_CSS": True,
        "EXTRA_CSS": [],
    },
    tools=tool_registry.tools,
)
