import pytest  # type: ignore

from helpers import run_pipx_cli
from tests.package_info import PKG


def test_show(pipx_temp_env, capsys):
    val = run_pipx_cli(["install", PKG["pycowsay"]["spec"]])
    assert not run_pipx_cli(["show", "pycowsay"])
    captured = capsys.readouterr()
    assert "nothing has been installed with pipx" in captured.err
