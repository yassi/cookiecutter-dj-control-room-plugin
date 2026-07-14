"""
Tests that bake this cookiecutter template and validate what comes out.

The fast tests only exercise cookiecutter's rendering step. The tests marked
``slow`` additionally install the generated project into an isolated
virtualenv and run *its own* test suite -- this is what catches bugs where
rendered code doesn't actually agree with itself, e.g. a helper renamed in
``tools.py`` without updating the test that imports it.
"""

import pytest

DEFAULT_CONTEXT = {"project_name": "Django Widget Panel"}


def test_bake_with_defaults_succeeds(cookies):
    result = cookies.bake(extra_context=DEFAULT_CONTEXT)

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.is_dir()


def test_bake_produces_expected_layout(cookies):
    result = cookies.bake(extra_context=DEFAULT_CONTEXT)
    project_dir = result.project_path
    package_dir = project_dir / "django_widget_panel"

    assert (project_dir / "pyproject.toml").is_file()
    assert (project_dir / "requirements.txt").is_file()
    assert (project_dir / "Makefile").is_file()
    assert package_dir.is_dir()
    assert (package_dir / "panel.py").is_file()
    assert (package_dir / "tools.py").is_file()
    assert (package_dir / "conf.py").is_file()
    assert (project_dir / "tests" / "test_admin.py").is_file()
    assert (project_dir / "tests" / "test_panel.py").is_file()
    assert (project_dir / "tests" / "test_tools.py").is_file()
    assert (project_dir / "example_project" / "manage.py").is_file()


@pytest.mark.parametrize(
    "license_choice, expect_license_file",
    [
        ("MIT", True),
        ("BSD", True),
        ("Apache-2.0", True),
        ("GPL-3.0", True),
        ("No license file", False),
    ],
)
def test_bake_license_selection(cookies, license_choice, expect_license_file):
    result = cookies.bake(
        extra_context={**DEFAULT_CONTEXT, "open_source_license": license_choice}
    )

    assert result.exit_code == 0
    assert (result.project_path / "LICENSE").is_file() is expect_license_file


def test_bake_derives_slug_and_package_name_from_project_name(cookies):
    result = cookies.bake(extra_context={"project_name": "My Cool Panel-Thing"})

    assert result.exit_code == 0
    assert result.project_path.name == "my-cool-panel-thing"
    assert (result.project_path / "my_cool_panel_thing").is_dir()


@pytest.mark.slow
@pytest.mark.parametrize(
    "extra_context",
    [
        DEFAULT_CONTEXT,
        {**DEFAULT_CONTEXT, "open_source_license": "No license file"},
    ],
    ids=["default", "no-license"],
)
def test_generated_project_test_suite_passes(cookies, install_and_test, extra_context):
    """Bake a project, install it exactly like a real consumer would (mirrors
    `make install`), and run its generated test suite end-to-end.
    """
    result = cookies.bake(extra_context=extra_context)
    assert result.exit_code == 0
    assert result.exception is None

    install_and_test(result.project_path)
