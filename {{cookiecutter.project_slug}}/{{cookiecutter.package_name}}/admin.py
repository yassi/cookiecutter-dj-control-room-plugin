from django.contrib import admin
from dj_control_room_base.core import BasePanelAdmin

from .conf import panel_config
from .models import {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Placeholder


@admin.register({{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Placeholder)
class {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}PlaceholderAdmin(BasePanelAdmin):
    redirect_url_name = "{{ cookiecutter.package_name }}:index"
    panel_config = panel_config
