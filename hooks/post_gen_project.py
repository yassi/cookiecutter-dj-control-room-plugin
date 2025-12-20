#!/usr/bin/env python
"""
Post-generation hook for cookiecutter-django-admin-panel.

This script runs after the project is generated to perform cleanup tasks.
"""

import os
import sys


def remove_file(filepath):
    """Remove a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Removed: {filepath}")


def main():
    """Run post-generation tasks."""
    # Get the license choice from cookiecutter context
    license_choice = "{{ cookiecutter.open_source_license }}"

    # Remove LICENSE file if "No license file" was selected
    if license_choice == "No license file":
        remove_file("LICENSE")
        print("✓ No license file generated")
    else:
        print(f"✓ Generated {license_choice} license file")

    print("\n" + "=" * 70)
    print("🎉 Project generated successfully!")
    print("=" * 70)
    print("\nNext steps:")
    print("  1. cd {{ cookiecutter.project_slug }}")
    print("  2. git init")
    print("  3. make install")
    print("  4. cd example_project")
    print("  5. python manage.py migrate")
    print("  6. python manage.py createsuperuser")
    print("  7. python manage.py runserver")
    print("\nVisit http://127.0.0.1:8000/admin/ to see your panel!")
    print("\nFor more information, see the README.md file.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
