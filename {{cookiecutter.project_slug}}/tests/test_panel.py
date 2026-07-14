"""
Tests for the {{ cookiecutter.project_name }} plugin declaration ({{ cookiecutter.package_name }}.panel).
"""

from django.test import SimpleTestCase

from {{ cookiecutter.package_name }}.conf import panel_config
from {{ cookiecutter.package_name }}.panel import {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Panel


class Test{{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Panel(SimpleTestCase):
    """Test cases for the {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Panel PanelPlugin subclass."""

    def test_validate_passes(self):
        """validate() should not raise since all required attrs are set."""
        panel = {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Panel()
        panel.validate()  # Raises on failure; no assertion needed.

    def test_get_config_returns_panel_config(self):
        """get_config() returns the module-level PanelConfig singleton."""
        panel = {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Panel()
        self.assertIs(panel.get_config(), panel_config)
