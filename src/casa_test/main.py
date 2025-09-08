#!/usr/bin/env python
from __future__ import annotations

import logging
from argparse import ArgumentParser
from pathlib import Path

from casacore.tables import table

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)


def do_something(
    ms_path: Path,
) -> list[str]:
    with table(str(ms_path)) as tab:
        columns: list[str] = tab.colnames()

    msg = f"{columns=}"
    logger.info(msg)

    return columns


def get_parser() -> ArgumentParser:
    parser = ArgumentParser(description="A dummy script using casacore")

    parser.add_argument("ms", type=Path, help="A MeasurementSet.")

    return parser


def main() -> None:
    parser = get_parser()
    args = parser.parse_args()

    _ = do_something(
        ms_path=args.ms,
    )


if __name__ == "__main__":
    main()
