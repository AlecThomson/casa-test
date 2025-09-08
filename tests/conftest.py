from __future__ import annotations

import shutil
from collections.abc import Generator
from importlib import resources
from pathlib import Path

import pytest

from casa_test import data


@pytest.fixture
def temp_ms(tmpdir: Path) -> Generator[Path]:
    ms_zip = Path(resources.files(data)) / "SB39400.RACS_0635-31.beam0.small.ms.zip"  # type: ignore[arg-type]

    out_name = ms_zip.name.replace(".zip", "")
    temp_path = Path(tmpdir)
    shutil.unpack_archive(ms_zip, temp_path)
    outpath = temp_path / out_name
    assert outpath.exists()
    yield outpath

    shutil.rmtree(outpath)
