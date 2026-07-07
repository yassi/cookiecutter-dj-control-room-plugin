# Configuration

{{ cookiecutter.project_name }} currently works out of the box with minimal configuration.

## Basic Setup

The only required configuration is adding the app to your `INSTALLED_APPS` and including the URLs in your URL configuration.

See the [Installation](installation.md) guide for setup instructions.

## URLs Configuration

```python
# urls.py
urlpatterns = [
    path('admin/{{ cookiecutter.project_slug }}/', include('{{ cookiecutter.package_name }}.urls')),  # Custom path
    path('admin/', admin.site.urls),
]
```

## Security

{{ cookiecutter.project_name }} uses Django's built-in admin authentication:

- Only staff users (`is_staff=True`) can access the panel
- All views require authentication via `@staff_member_required`
- No additional security configuration needed

## CSS Customization

You can customize panel styling with `{{ cookiecutter.package_name|upper }}_SETTINGS`:

### `LOAD_DEFAULT_CSS`

**Type:** `bool`  
**Default:** `True`  
**Description:** Whether to load the built-in panel stylesheet. Set to `False` to use your own styles.

### `EXTRA_CSS`

**Type:** `list[str]`  
**Default:** `[]`  
**Description:** Additional stylesheets to load after the default CSS. Accepts static file paths or full URLs.

```python
{{ cookiecutter.package_name|upper }}_SETTINGS = {
    'LOAD_DEFAULT_CSS': True,
    'EXTRA_CSS': [
        '{{ cookiecutter.package_name }}/css/overrides.css',
        'https://cdn.example.com/theme.css',
    ],
}
```

## Panel Tools

{{ cookiecutter.project_name }} ships with `{{ cookiecutter.package_name }}/tools.py`, a `ToolRegistry` of MCP-facing tools that the dj-control-room hub can aggregate and expose to an AI agent. A `get_resolved_settings` tool is included by default.

Add your own by decorating a handler with `@registry.register(...)` in `tools.py`:

```python
# {{ cookiecutter.package_name }}/tools.py
@registry.register(
    name="get_item",
    scope="read",
    description="Fetch a single item by key.",
    input_schema={
        "type": "object",
        "properties": {"key": {"type": "string"}},
        "required": ["key"],
    },
)
def handle_get_item(ctx: PanelToolContext) -> PanelToolResult:
    ...
```

Tools are picked up automatically via `conf.py`'s `tools=tool_registry.tools`. See the [dj-control-room-base panel tools guide](https://yassi.github.io/dj-control-room-base/building-panels/#panel-tools) for the full API.

## Advanced Configuration

Other advanced configuration options may be added in future releases.
