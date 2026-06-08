from django.shortcuts import render

from .conf import panel_config


@panel_config.permission_required("index")
def index(request):
    context = panel_config.get_context(request, title="{{ cookiecutter.django_app_verbose_name }}")
    return render(request, "admin/{{ cookiecutter.package_name }}/index.html", context)
