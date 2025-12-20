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

## Advanced Configuration

Advanced configuration options will be added in future releases.
