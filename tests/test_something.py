from __future__ import annotations

from pathlib import Path

from casa_test.main import do_something


def test_something(temp_ms: Path) -> None:
    assert temp_ms.exists()
    column_names = do_something(
        temp_ms,
    )
    assert "DATA" in column_names
