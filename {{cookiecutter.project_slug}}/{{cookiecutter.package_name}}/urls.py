from django.urls import path
from . import views

app_name = "{{ cookiecutter.package_name }}"

urlpatterns = [
    path("", views.index, name="index"),
]
