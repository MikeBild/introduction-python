"""Checks all exercises: pytest and mypy --strict per starting point and reference solution.

uv run python scripts/check.py            all exercises
uv run python scripts/check.py 05 11      only exercises 05 and 11
uv run python scripts/check.py --solution only the solutions

Every exercise runs in its own directory so that modules with the same name
(such as shop.py in start/ and solution/) do not get in each other's way.
Exercises with their own pyproject.toml (packages) run with uv in their own environment.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# starting points that deliberately have no type hints yet
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
