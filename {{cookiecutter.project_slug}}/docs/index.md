# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Overview

{{ cookiecutter.project_name }} is a Django admin extension.

**Status:** This project is currently in early development.

## Quick Links

- [Installation](installation.md)
- [Configuration](configuration.md)
- [Development](development.md)

## Requirements

- Python 3.9+
- Django 4.2+

## License

{% if cookiecutter.open_source_license != 'No license file' %}{{ cookiecutter.open_source_license }}{% else %}MIT{% endif %} License - See [LICENSE](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/blob/main/LICENSE) file for details.
