[![Django Control Room Panel](https://img.shields.io/badge/Django%20Control%20Room-Panel-0c4b33?logo=django)](https://github.com/django-control-room/dj-control-room)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }})
[![Python versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![License: {% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD' %}BSD{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Apache--2.0{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GPL--3.0{% else %}MIT{% endif %}](https://img.shields.io/badge/License-{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD' %}BSD{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Apache--2.0{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GPL--3.0{% else %}MIT{% endif %}-green.svg)](https://opensource.org/licenses/{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD' %}BSD-3-Clause{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Apache-2.0{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GPL-3.0{% else %}MIT{% endif %})




# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

**Compatible with [dj-control-room](https://github.com/django-control-room/dj-control-room).** Register this panel in the Control Room to manage it from a centralized dashboard.

- **Official site:** [djangocontrolroom.com](https://djangocontrolroom.com)
- **Project repo:** [dj-control-room](https://github.com/django-control-room/dj-control-room)

## Docs

[https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/)

## Features

- **TBD**: Add your main features here
- **AI Agent Integration (MCP)**: exposes tools defined in `tools.py` (a `hello_world` example ships by default) so AI agents can interact with your panel via [dj-control-room](https://github.com/django-control-room/dj-control-room)'s MCP server


### Project Structure

```
{{ cookiecutter.project_slug }}/
├── {{ cookiecutter.package_name }}/         # Main package
│   ├── templates/           # Django templates
│   ├── views.py             # Django views
│   └── urls.py              # URL patterns
├── example_project/         # Example Django project
├── tests/                   # Test suite
├── images/                  # Screenshots for README
└── requirements.txt         # Development dependencies
```

## Requirements

- Python 3.9+
- Django 4.2+



## Screenshots

### Django Admin Integration
Seamlessly integrated into your Django admin interface. A new section for {{ cookiecutter.project_slug }}
will appear in the same places where your models appear.

**NOTE:** This application does not actually introduce any model or migrations.

![Admin Home](https://raw.githubusercontent.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/main/images/admin_home.png)


## Installation

```bash
pip install {{ cookiecutter.project_slug }}
```

Add it to `INSTALLED_APPS`, include its URLs, and migrate:

```python
INSTALLED_APPS = [
    # ...
    '{{ cookiecutter.package_name }}',
]
```

```python
urlpatterns = [
    path('admin/{{ cookiecutter.project_slug }}/', include('{{ cookiecutter.package_name }}.urls')),
    path('admin/', admin.site.urls),
]
```

```bash
python manage.py migrate
```

Then visit `/admin/` and look for the "{{ cookiecutter.django_app_verbose_name.upper() }}" section.

For the full walkthrough and settings reference, see the [Installation](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/installation/) and [Configuration](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/configuration/) docs.


## DJ Control Room Integration

This panel is designed to work seamlessly with [DJ Control Room](https://github.com/django-control-room/dj-control-room), a centralized dashboard for managing Django admin panels.

### Integration

register your panel in django's installed apps

1. Add `dj_control_room` to `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       # ... other apps
       'dj_control_room',
       '{{ cookiecutter.package_name }}',
   ]
   ```

2. Include the Control Room URLs in your `urls.py`:
   ```python
   urlpatterns = [
       path('', include('{{ cookiecutter.package_name }}.urls')),  # Panel URLs
       path('admin/dj-control-room/', include('dj_control_room.urls')),  # Control Room
       path('admin/', admin.site.urls),
   ]
   ```

3. Visit `/admin/dj-control-room/` to see all your panels in one place!

### Panel Configuration

The panel is configured via the `panel.py` file with the following attributes:

- **ID**: `{{ cookiecutter.package_name }}`
- **Name**: {{ cookiecutter.project_name }}
- **Description**: {{ cookiecutter.project_description }}
- **Icon**: {{ cookiecutter.panel_icon }}

You can customize these values by editing `{{ cookiecutter.package_name }}/panel.py`.


## MCP Tools (AI Agent Integration)

Ships a `hello_world` example tool that [dj-control-room](https://github.com/django-control-room/dj-control-room)'s MCP server exposes to AI agents (Cursor, Claude, etc.). Add your own in `{{ cookiecutter.package_name }}/tools.py`.

See [Configuration → Panel Tools (MCP)](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/configuration/#panel-tools-mcp) for the full reference and [Scopes](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/scopes/) for how agent access is permissioned separately from the admin UI.

## Development Setup

Want to contribute or set up the project for local development? See [docs/contributing.md](docs/contributing.md) for prerequisites, Docker/virtualenv setup, running the example project, and the test suite.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
