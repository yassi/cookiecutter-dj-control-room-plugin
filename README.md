# cookiecutter-dj-control-room-plugin

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/django-control-room/cookiecutter-dj-control-room-plugin/main/images/hero-dark.png">
  <img src="https://raw.githubusercontent.com/django-control-room/cookiecutter-dj-control-room-plugin/main/images/hero-light.png" alt="cookiecutter-dj-control-room-plugin">
</picture>

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for generating Django admin panel libraries like `dj-redis-panel`, `dj-cache-panel`, and `dj-celery-panel`.

Libraries generated from this template are **compatible with [dj-control-room](https://github.com/django-control-room/dj-control-room)** and can be registered as panels in its centralized dashboard.

- **Official site:** [djangocontrolroom.com](https://djangocontrolroom.com)
- **Project repo:** [dj-control-room](https://github.com/django-control-room/dj-control-room)

This template provides a complete, production-ready structure for building Django libraries that integrate seamlessly with the Django admin interface. 

## Features

### Admin Integration
- Placeholder model appears in Django admin
- Clicking it redirects to custom panel views
- No actual database models or migrations
- Seamless integration with Django admin UI

### Complete Development Setup
- Docker Compose for services and development container
- Makefile with common tasks
- pytest configuration with coverage
- MkDocs for documentation

### Modern Python Packaging
- Uses `pyproject.toml` (PEP 517/518)
- Setuptools backend
- Proper package data inclusion
- Development and build dependencies separated

### Flexible Licensing
- Supports multiple open-source licenses
- Generates appropriate LICENSE file
- Updates classifiers in pyproject.toml
- Option for no license



## Requirements

- Python 3.9+
- [cookiecutter](https://github.com/cookiecutter/cookiecutter) >= 2.0.0

Install cookiecutter:

```bash
pip install cookiecutter
```

## Usage

### Create a New Project

Create a new project by referencing this template directly from github
```bash
cookiecutter https://github.com/django-control-room/cookiecutter-dj-control-room-plugin
```

### Template Variables

You'll be prompted to enter the following information:

- **project_name**: Human-readable project name (e.g., "Django Redis Panel")
- **project_slug**: URL/package-friendly name (auto-generated from project_name)
- **package_name**: Python package name (auto-generated from project_slug)
- **project_description**: Short description of your project
- **author_name**: Your name
- **author_email**: Your email address
- **github_username**: Your GitHub username
- **version**: Initial version number (default: 0.1.0)
- **django_app_verbose_name**: Display name in Django admin
- **open_source_license**: Choose from MIT, BSD, Apache-2.0, GPL-3.0, or No license

### Example

```bash
$ cookiecutter cookiecutter-dj-control-room-plugin

project_name [Django Example Panel]: Django Redis Panel
project_slug [django-redis-panel]: 
package_name [django_redis_panel]: 
project_description [A Django Admin panel for inspecting and managing X]: A Django Admin panel for inspecting and managing Redis instances
author_name [Your Name]: John Doe
author_email [your.email@example.com]: john@example.com
github_username [yourusername]: johndoe
version [0.1.0]: 
django_app_verbose_name [Django Redis Panel]: 
open_source_license [MIT]: 
```

## What's Generated

The template creates a complete Django package with:

```
your-project/
├── your_package/              # Main Python package
│   ├── __init__.py
│   ├── admin.py              # Django admin integration
│   ├── apps.py               # Django app configuration
│   ├── models.py             # Placeholder model for admin
│   ├── urls.py               # URL routing
│   ├── views.py              # View logic
│   └── templates/            # Django templates
│       └── admin/
│           └── your_package/
│               ├── base.html
│               ├── index.html
│               └── styles.css
├── tests/                     # Test suite
│   ├── conftest.py
│   ├── base.py
│   └── test_admin.py
├── example_project/           # Example Django project for development
│   ├── example_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   ├── manage.py
│   └── Dockerfile
├── docs/                      # MkDocs documentation
│   ├── index.md
│   ├── installation.md
│   ├── configuration.md
│   └── development.md
├── images/                    # Screenshots for README
├── pyproject.toml            # Python package configuration
├── setup.py                  # Setuptools entry point
├── requirements.txt          # Development dependencies
├── Makefile                  # Common development tasks
├── docker-compose.yml        # Docker services configuration
├── mkdocs.yml               # Documentation configuration
├── pytest.ini               # Pytest configuration
├── codecov.yml              # Code coverage configuration
├── MANIFEST.in              # Package manifest
├── LICENSE                  # License file
└── README.md                # Project README

```

Note that this includes both an installable package as well as an example application for active development and testing.

## After Generation

Once your project is generated, follow these steps:

### 1. Initialize Git Repository

```bash
cd your-project
git init
git add .
git commit -m "Initial commit from cookiecutter template"
```

### 2. Set Up Development Environment

```bash
# Using virtualenv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
make install

# Or using Docker
make docker_up
make docker_shell  # this will open up a new shell in a docker container
```

### 3. Run Tests

```bash
# Local
make test_local

# Docker
make test_docker
```

### 4. Start Development Server

```bash
cd example_project
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit http://127.0.0.1:8000/admin/ to see your panel in action!

### 5. Customize Your Panel

- Modify `your_package/views.py` to add your business logic
- Update templates in `your_package/templates/admin/your_package/`
- Add tests in `tests/`
- Update documentation in `docs/`

## Development Tasks

The generated Makefile includes common development tasks:

```bash
make install             # Install dependencies and package
make test_local          # Run tests locally
make test_docker         # Run tests in Docker
make test_coverage       # Run tests with coverage report
make build               # Build distribution packages
make docs                # Build documentation
make docs_serve          # Serve documentation locally
make docker_up           # Start Docker services
make docker_down         # Stop Docker services
make docker_shell        # Open shell in dev container
```

## Project Structure Philosophy

This template is designed for Django libraries that integrate with the admin interface:

- **No Real Models**: Uses a placeholder model to appear in the admin
- **URL-based Views**: Custom views accessible through Django admin
- **Admin Styling**: Templates extend Django admin templates for consistency
- **Minimal Dependencies**: Only requires Django core

This template is extensible and you don't have to abide by these guidelines. In fact, this template
can be used as a starting point for creating any type of django app/library.

## Examples of Projects Using This Pattern

- [dj-redis-panel](https://github.com/django-control-room/dj-redis-panel) - Redis inspection and management
- [dj-cache-panel](https://github.com/django-control-room/dj-cache-panel) - Django cache backends inspector
- [dj-celery-panel](https://github.com/django-control-room/dj-celery-panel) - Celery task monitoring

## Template Development

### Working with Django Templates

Since both cookiecutter (Jinja2) and Django use the same template syntax (`{% %}`), special care is needed when adding or modifying Django template files. See [DJANGO_TEMPLATES.md](DJANGO_TEMPLATES.md) for a comprehensive guide on handling Django templates in this cookiecutter template.

**Quick tip**: Wrap Django template tags in `{% raw %}{% endraw %}` blocks to prevent cookiecutter from trying to process them.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Testing Your Changes

This repo has its own automated test suite (in `tests/`, separate from the
tests that get generated *inside* a project) that bakes the template with
[`cookiecutter`](https://github.com/cookiecutter/cookiecutter) and
[`pytest-cookies`](https://github.com/hackebrot/pytest-cookies), then
installs the generated project into an isolated virtualenv exactly like a
real consumer would (`pip install -r requirements.txt && pip install -e .`)
and runs **its** generated test suite. This is what catches bugs where
rendered code doesn't actually agree with itself -- e.g. a helper renamed in
`tools.py` without updating the test that imports it.

Run it with:

```bash
make test          # bakes several project variants and runs their test suites
make test_fast      # skips the slow bake+install+run checks
```

or directly:

```bash
pip install -r requirements-test.txt
pytest tests/ -v
```

This also runs automatically in CI (`.github/workflows/test.yml`) across
several Python versions.

Before submitting a PR, additionally sanity-check the template by hand:

1. **Generate a project**:
   ```bash
   cookiecutter /path/to/your/fork
   ```

2. **Test the generated project**:
   ```bash
   cd generated-project
   make install
   make test_local
   cd example_project
   python manage.py migrate
   python manage.py runserver
   ```

3. **Verify all features work**:
   - Package installation
   - Tests pass
   - Documentation builds
   - Docker setup works
   - Admin integration works

## License

This template is licensed under the MIT License. The projects generated from this template will use the license you select during generation.
