from django.db import models


class CeleryPanelPlaceholder(models.Model):
    """
    This is a fake model used to create an entry in the admin panel for {{ cookiecutter.package_name }}.
    When we register this app with the admin site, it is configured to simply load
    the panel templates.
    """

    class Meta:
        managed = False
        verbose_name = "{{ cookiecutter.django_app_verbose_name }}"
        verbose_name_plural = "{{ cookiecutter.django_app_verbose_name }}"
