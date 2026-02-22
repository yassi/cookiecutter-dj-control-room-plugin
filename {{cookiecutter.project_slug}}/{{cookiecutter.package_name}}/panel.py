"""
DJ Control Room panel configuration.

This module defines the panel that will be discovered and registered
by DJ Control Room via entry points.
"""


class {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Panel:
    """
    Panel configuration for {{ cookiecutter.project_name }}.
    
    This class is discovered by DJ Control Room via the entry point
    defined in pyproject.toml under [project.entry-points."dj_control_room.panels"]
    """
    
    # Display name shown in the DJ Control Room dashboard
    name = "{{ cookiecutter.project_name }}"

    # Brief description shown on the panel card
    description = "{{ cookiecutter.project_description }}"

    # Icon to display (options: database, layers, link, chart, radio, cog, etc.)
    icon = "{{ cookiecutter.panel_icon }}"

    # Django app label as it appears in INSTALLED_APPS and the URL namespace
    # in urls.py. Defaults to the normalized dist name if not set.
    app_name = "{{ cookiecutter.package_name }}"

    # Optional links shown on the install/configure page.
    docs_url = "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}"
    pypi_url = "https://pypi.org/project/{{ cookiecutter.project_slug }}/"

    def get_url_name(self):
        """
        Return the URL name for the panel's main view.

        This should match the name of your main URL pattern in urls.py.
        Typically this is "index".

        Returns:
            str: The URL name (e.g., "index")
        """
        return "index"
