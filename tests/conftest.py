"""
Shared fixtures for testing the cookiecutter-dj-control-room-plugin template
itself.

The `cookies` fixture used throughout these tests comes from the
`pytest-cookies` plugin and bakes real projects from this template using
cookiecutter's own API (see ``--template`` in pytest's ``-h`` output; it
defaults to the current working directory, so these tests must be run from
the repo root, e.g. ``pytest tests/`` or ``make test``).
"""

import os
import subprocess
import venv
from pathlib import Path

import pytest


def run(cmd, cwd=None, timeout=600):
    """Run a subprocess, failing the test with full output on non-zero exit."""
    result = subprocess.run(
        [str(part) for part in cmd],
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        pytest.fail(
            "Command failed ({}): {}\n\n--- stdout ---\n{}\n--- stderr ---\n{}".format(
                result.returncode,
                " ".join(str(part) for part in cmd),
                result.stdout,
                result.stderr,
            )
        )
    return result


def venv_python(venv_dir: Path) -> Path:
    bin_dir = "Scripts" if os.name == "nt" else "bin"
    exe = "python.exe" if os.name == "nt" else "python"
    return venv_dir / bin_dir / exe


@pytest.fixture
def install_and_test(tmp_path_factory):
    """Install a baked project the same way a real consumer would, then run
    its generated test suite.

    Mirrors the generated ``make install`` target: ``requirements.txt``
    first (this is what pulls in Django, dj-control-room-base,
    dj-control-room, and the pytest tooling), then an editable install of
    the generated package itself.
    """

    def _run_generated_suite(project_dir: Path, pytest_args=None):
        venv_dir = tmp_path_factory.mktemp("venv")
        venv.EnvBuilder(with_pip=True).create(venv_dir)
        python = venv_python(venv_dir)

        run([python, "-m", "pip", "install", "--upgrade", "pip"])
        run([python, "-m", "pip", "install", "-r", "requirements.txt"], cwd=project_dir)
        run([python, "-m", "pip", "install", "-e", "."], cwd=project_dir)

        return run(
            [python, "-m", "pytest", "tests/", "-v", *(pytest_args or [])],
            cwd=project_dir,
        )

    return _run_generated_suite
