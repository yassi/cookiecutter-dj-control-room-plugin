"""
DJ Control Room panel plugin for {{ cookiecutter.project_name }}.

Registers this package with the hub via the entry point defined in
``pyproject.toml`` under ``[project.entry-points."dj_control_room.panels"]``.
"""

from dj_control_room_base.core import PanelPlugin


class {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Panel(PanelPlugin):
    name = "{{ cookiecutter.project_name }}"
    description = "{{ cookiecutter.project_description }}"
    icon = "{{ cookiecutter.panel_icon }}"

    app_name = "{{ cookiecutter.package_name }}"
    docs_url = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"
    pypi_url = "https://pypi.org/project/{{ cookiecutter.project_slug }}/"

    def get_config(self):
        from .conf import panel_config
        return panel_config
