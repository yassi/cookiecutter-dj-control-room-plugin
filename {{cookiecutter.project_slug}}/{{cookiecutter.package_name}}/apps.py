from django.apps import AppConfig


class {{ cookiecutter.package_name.title().replace('_', '') }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.package_name }}"
    verbose_name = "{{ cookiecutter.django_app_verbose_name }}"
