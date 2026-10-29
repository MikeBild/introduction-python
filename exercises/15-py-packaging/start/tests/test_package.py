import email
import shutil
import subprocess
import zipfile
from pathlib import Path

import pytest

from werkstatt_money import format_cents, main, to_cents

pytestmark = pytest.mark.skip(reason="Entferne diese Zeile, um die Tests zu aktivieren.")

PROJECT = Path(__file__).resolve().parents[1]


def test_api_round_trip() -> None:
    assert format_cents(to_cents("12,34")) == "12,34 €"
    assert format_cents(to_cents("1234,56")) == "1.234,56 €"


def test_main_prints_cents(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["12,34", "0,5"]) == 0
    assert capsys.readouterr().out == "1234\n50\n"


@pytest.fixture(scope="module")
def wheel(tmp_path_factory: pytest.TempPathFactory) -> zipfile.ZipFile:
    uv = shutil.which("uv")
    assert uv is not None, "uv muss im PATH liegen"
    out = tmp_path_factory.mktemp("dist")
    subprocess.run([uv, "build", "--wheel", "--out-dir", str(out)], cwd=PROJECT, check=True, capture_output=True)
    [path] = out.glob("werkstatt_money-*.whl")
    return zipfile.ZipFile(path)


def test_wheel_contains_typed_package(wheel: zipfile.ZipFile) -> None:
    names = wheel.namelist()
    assert "werkstatt_money/__init__.py" in names
    assert "werkstatt_money/py.typed" in names
    assert not any(name.startswith("tests/") for name in names)


def test_wheel_metadata(wheel: zipfile.ZipFile) -> None:
    [metadata_path] = [name for name in wheel.namelist() if name.endswith(".dist-info/METADATA")]
    metadata = email.message_from_bytes(wheel.read(metadata_path))
    assert metadata["Name"] == "werkstatt-money"
    assert metadata["Version"] == "1.0.0"
    assert metadata["Requires-Python"] == ">=3.15"
    assert metadata["License-Expression"] == "MIT"
    assert metadata["Summary"]


def test_wheel_installs_the_command(wheel: zipfile.ZipFile) -> None:
    [entry_points] = [name for name in wheel.namelist() if name.endswith(".dist-info/entry_points.txt")]
    assert "werkstatt-money = werkstatt_money:main" in wheel.read(entry_points).decode()
