from dj_control_room_base.core import PanelPlaceholderModel


class {{ cookiecutter.project_name.replace(' ', '').replace('-', '').replace('_', '') }}Placeholder(PanelPlaceholderModel):
    class Meta(PanelPlaceholderModel.Meta):
        verbose_name = "{{ cookiecutter.django_app_verbose_name }}"
        verbose_name_plural = "{{ cookiecutter.django_app_verbose_name }}"
