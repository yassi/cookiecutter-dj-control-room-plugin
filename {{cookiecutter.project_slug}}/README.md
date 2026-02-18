[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_slug }})
[![Python versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg)](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![License: {% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD' %}BSD{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Apache--2.0{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GPL--3.0{% else %}MIT{% endif %}](https://img.shields.io/badge/License-{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD' %}BSD{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Apache--2.0{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GPL--3.0{% else %}MIT{% endif %}-green.svg)](https://opensource.org/licenses/{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD' %}BSD-3-Clause{% elif cookiecutter.open_source_license == 'Apache-2.0' %}Apache-2.0{% elif cookiecutter.open_source_license == 'GPL-3.0' %}GPL-3.0{% else %}MIT{% endif %})




# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

**Compatible with [dj-control-room](https://github.com/yassi/dj-control-room).** Register this panel in the Control Room to manage it from a centralized dashboard.

- **Official site:** [djangocontrolroom.com](https://djangocontrolroom.com)
- **Project repo:** [dj-control-room](https://github.com/yassi/dj-control-room)

## Docs

[https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug }}/)

## Features

- **TBD**: Add your main features here


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

### 1. Install the Package

```bash
pip install {{ cookiecutter.project_slug }}
```

### 2. Add to Django Settings

Add `{{ cookiecutter.package_name }}` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{{ cookiecutter.package_name }}',  # Add this line
    # ... your other apps
]
```

### 3. Configure Settings (Optional)

Add any custom configuration to your Django settings if needed:

```python
# Optional: Add custom settings for {{ cookiecutter.package_name }}
{{ cookiecutter.package_name.upper() }}_SETTINGS = {
    # Add your configuration here
}
```




### 4. Include URLs

Add the Panel URLs to your main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/{{ cookiecutter.project_slug }}/', include('{{ cookiecutter.package_name }}.urls')),  # Add this line
    path('admin/', admin.site.urls),
]
```

### 5. Run Migrations and Create Superuser

```bash
python manage.py migrate
python manage.py createsuperuser  # If you don't have an admin user
```

### 6. Access the Panel

1. Start your Django development server:
   ```bash
   python manage.py runserver
   ```

2. Navigate to the Django admin at `http://127.0.0.1:8000/admin/`

3. Look for the "{{ cookiecutter.django_app_verbose_name.upper() }}" section in the admin interface


## DJ Control Room Integration

This panel is designed to work seamlessly with [DJ Control Room](https://github.com/yassi/dj-control-room), a centralized dashboard for managing Django admin panels.

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


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Development Setup

If you want to contribute to this project or set it up for local development:

### Prerequisites

- Python 3.9 or higher
- Redis server running locally
- Git
- Autoconf
- Docker

It is reccommended that you use docker since it will automate much of dev env setup

### 1. Clone the Repository

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
```

### 2a. Set up dev environment using virtualenv

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -e . # install {{ cookiecutter.project_slug }} package locally
pip intall -r requirements.txt  # install all dev requirements

# Alternatively
make install # this will also do the above in one single command
```

### 2b. Set up dev environment using docker

```bash
make docker_up  # bring up all services (redis, memached) and dev environment container
make docker_shell  # open up a shell in the docker conatiner
```

### 3. Set Up Example Project

The repository includes an example Django project for development and testing

```bash
cd example_project
python manage.py migrate
python manage.py createsuperuser
```

### 4. Populate Test Data (Optional)

Add any custom management commands for populating test data if needed.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/admin/` to access the Django admin with {{ cookiecutter.project_name }}.

### 7. Running Tests

The project includes a comprehensive test suite. You can run them by using make or
by invoking pytest directly:

```bash
# build and install all dev dependencies and run all tests inside of docker container
make test_docker

# Test without the docker on your host machine.
# note that testing always requires a redis and memcached service to be up.
# these are mostly easily brought up using docker
make test_local
```
