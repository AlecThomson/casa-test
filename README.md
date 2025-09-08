# casa-test

[![Actions Status][actions-badge]][actions-link]
<!-- [![Documentation Status][rtd-badge]][rtd-link] -->

<!-- [![PyPI version][pypi-version]][pypi-link] -->
<!-- [![Conda-Forge][conda-badge]][conda-link] -->
<!-- [![PyPI platforms][pypi-platforms]][pypi-link] -->

<!-- [![GitHub Discussion][github-discussions-badge]][github-discussions-link] -->

<!-- SPHINX-START -->

<!-- prettier-ignore-start -->
[actions-badge]:            https://github.com/AlecThomson/casa-test/workflows/CI/badge.svg
[actions-link]:             https://github.com/AlecThomson/casa-test/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/casa-test
[conda-link]:               https://github.com/conda-forge/casa-test-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/AlecThomson/casa-test/discussions
[pypi-link]:                https://pypi.org/project/casa-test/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/casa-test
[pypi-version]:             https://img.shields.io/pypi/v/casa-test
[rtd-badge]:                https://readthedocs.org/projects/casa-test/badge/?version=latest
[rtd-link]:                 https://casa-test.readthedocs.io/en/latest/?badge=latest

<!-- prettier-ignore-end -->

A demo repo combining python-casacore scripts with monolithic CASA scripts.

## Installation

Requires monolithic `CASA>=6` and `python>=3.10`.

Module is installed with `pip`.

## Usage

Dummy scripts are:

```bash
casa_test # Run python-casacore
casa_test_bash # Run bash
casa_test_casa # Run CASA from bash
casa_test_casa_opt # Run CASA directly (requires coreutils>=8.30)
```
