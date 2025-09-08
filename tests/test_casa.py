from __future__ import annotations

import subprocess as sp
from pathlib import Path
from shlex import split


def test_casa(temp_ms: Path) -> None:
    cmd_str = f"casa_test_casa {temp_ms.as_posix()}"

    sp.run(split(cmd_str), check=True)


def test_casa_opt(temp_ms: Path) -> None:
    cmd_str = f"casa_test_casa_opt {temp_ms.as_posix()}"

    sp.run(split(cmd_str), check=True)
