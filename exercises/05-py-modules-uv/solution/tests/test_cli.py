import shutil
import subprocess

import pytest

import werkstatt
from werkstatt.cli import main


def test_package_exports_its_public_functions() -> None:
    assert werkstatt.format_cents(5097) == "50,97 €"
    assert werkstatt.order_total([werkstatt.parse_item("2x1299")]) == 2598


def test_main_prints_the_order_total(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["2x1299", "1x2499"]) == 0
    assert capsys.readouterr().out == "50,97 €\n"


def test_script_is_installed_as_command() -> None:
    command = shutil.which("werkstatt")
    assert command is not None, "Fehlt [project.scripts] in pyproject.toml? Dann uv sync."
    result = subprocess.run([command, "3x250"], capture_output=True, text=True, check=True)
    assert result.stdout == "7,50 €\n"
