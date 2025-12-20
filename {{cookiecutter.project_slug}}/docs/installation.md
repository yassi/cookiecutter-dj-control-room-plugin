# Installation

## 1. Install the Package

```bash
pip install {{ cookiecutter.project_slug }}
```

## 2. Add to Django Settings

Add `{{ cookiecutter.package_name }}` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '{{ cookiecutter.package_name }}',  # Add this
    # ... your other apps
]
```

## 3. Include URLs

Add the Panel URLs to your main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/{{ cookiecutter.project_slug }}/', include('{{ cookiecutter.package_name }}.urls')),
    path('admin/', admin.site.urls),
]
```

## 4. Run Migrations

```bash
python manage.py migrate
```

## 5. Access the Panel

1. Start your Django development server:
   ```bash
   python manage.py runserver
   ```

2. Navigate to `http://127.0.0.1:8000/admin/`

3. Look for the "{{ cookiecutter.django_app_verbose_name.upper() }}" section

That's it!
