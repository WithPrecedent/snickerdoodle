"""Main file for unit tests."""

from __future__ import annotations

import {{cookiecutter.repo_name}}


def test_{{cookiecutter.repo_name}}() -> None:
    assert {{cookiecutter.repo_name}}.__version__ == '{{cookiecutter.version}}'

if __name__ == '__main__':
    test_{{cookiecutter.repo_name}}()
