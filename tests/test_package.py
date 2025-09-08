from __future__ import annotations

import importlib.metadata

import casa_test as m


def test_version():
    assert importlib.metadata.version("casa_test") == m.__version__
