from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.contrib import admin

from {{ cookiecutter.package_name }}.conf import get_css_context


@staff_member_required
def index(request):
    """
    Display panel dashboard.
    """
    context = admin.site.each_context(request)
    context.update(get_css_context())
    context.update(
        {
            "title": "{{ cookiecutter.django_app_verbose_name }}",
        }
    )
    return render(request, "admin/{{ cookiecutter.package_name }}/index.html", context)
