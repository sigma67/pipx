from pathlib import Path

from pipx.commands.common import venv_health_check
from pipx.venv import VenvContainer, Venv


def show(venv_dir: Path, package: str):
    venv = Venv(venv_dir)

    (venv_problems, warning_message) = venv_health_check(venv, package)
    if venv_problems.any_():
        return (warning_message, venv_problems)
