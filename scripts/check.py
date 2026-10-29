"""Prüft alle Übungen: pytest und mypy --strict je Startpunkt und Lösung.

uv run python scripts/check.py            alle Übungen
uv run python scripts/check.py 05 11      nur die Übungen 05 und 11
uv run python scripts/check.py --solution nur die Lösungen

Jede Übung läuft in ihrem eigenen Verzeichnis, damit gleichnamige Module
(etwa shop.py in start/ und solution/) sich nicht in die Quere kommen.
Übungen mit eigener pyproject.toml (Pakete) laufen mit uv in ihrer eigenen Umgebung.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# Startpunkte, die absichtlich noch keine Typ-Hinweise haben
UNTYPED_STARTS = {"09-py-type-hints"}


def run(command: list[str], cwd: Path) -> bool:
    print(f"$ ({cwd.relative_to(ROOT)}) {' '.join(command)}", flush=True)
    return subprocess.run(command, cwd=cwd).returncode == 0


def check(directory: Path) -> bool:
    exercise = directory.parent.name
    if (directory / "pyproject.toml").exists():
        prefix = ["uv", "run", "--locked", "--quiet", "--"]
        mypy_targets = ["src", "tests"]
    else:
        prefix = [sys.executable, "-m"]
        mypy_targets = ["."]
    ok = run([*prefix, "pytest"], directory)
    if directory.name == "solution" or exercise not in UNTYPED_STARTS:
        ok = run([*prefix, "mypy", "--strict", *mypy_targets], directory) and ok
    return ok


def main(args: list[str]) -> int:
    kinds = ["solution"] if "--solution" in args else ["solution", "start"]
    filters = [arg for arg in args if not arg.startswith("--")]
    failed = []
    for exercise in sorted((ROOT / "exercises").iterdir()):
        if filters and not any(exercise.name.startswith(f) for f in filters):
            continue
        for kind in kinds:
            if not check(exercise / kind):
                failed.append(f"{exercise.name}/{kind}")
    if failed:
        print("\nFehlgeschlagen – die Ursache steht in der Ausgabe darüber:", *failed, sep="\n  ")
        return 1
    print("\nAlle Übungen geprüft.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
