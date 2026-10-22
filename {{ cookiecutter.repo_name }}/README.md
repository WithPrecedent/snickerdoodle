{%- set on = ("y", "Y", True, "true", "True") -%}
# {{cookiecutter.project_name}}

| | |
| --- | --- |
| Version |{% if cookiecutter.pypi in on %} [![PyPI Latest Release](https://img.shields.io/pypi/v/{{ cookiecutter.package_name }}.svg?style={{ cookiecutter.badge_style }}&color=cornflowerblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/{{ cookiecutter.package_name }}/){% endif %} [![GitHub Latest Release](https://img.shields.io/github/v/tag/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}?style={{ cookiecutter.badge_style }}&color=forestgreen&label=GitHub&logo=github)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}/releases) |
| Status |{% if cookiecutter.github_actions in on %} [![Build Status](https://img.shields.io/github/actions/workflow/status/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}/ci.yml?style={{ cookiecutter.badge_style }}&branch=main&color=cadetblue&label=Tests&logo=pytest)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}/actions/workflows/ci.yml?query=branch%3Amain){% endif %}{% if cookiecutter.github_actions in on and cookiecutter.code_coverage in on %} [![Code Coverage](https://img.shields.io/codecov/c/github/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}?style={{ cookiecutter.badge_style }}&color=cadetblue&label=Coverage&logo=codecov)](https://app.codecov.io/gh/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}){% endif %} [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style={{ cookiecutter.badge_style }}&logo=git)](https://www.repostatus.org/#active){% if cookiecutter.pypi in on %} [![Project Stability](https://img.shields.io/pypi/status/{{ cookiecutter.package_name }}?style={{ cookiecutter.badge_style }}&logo=pypi&label=Stability&logoColor=yellow)](https://pypi.org/project/{{ cookiecutter.package_name }}/){% endif %} |
{% if cookiecutter.mkdocs in on %}| Documentation | [![Hosted By](https://img.shields.io/badge/Hosted_by-Github_Pages-blue?style={{ cookiecutter.badge_style }}&color=forestgreen&logo=github)](https://{{ cookiecutter.github_user }}.github.io/{{ cookiecutter.repo_name }}) |
{% endif %}| Tools |{% if cookiecutter.mkdocs in on %} [![Documentation](https://img.shields.io/badge/MkDocs-magenta?style={{ cookiecutter.badge_style }}&color=deepskyblue&logo=markdown&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/){% endif %} [![Linter](https://img.shields.io/endpoint?style={{ cookiecutter.badge_style }}&url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff){% if cookiecutter.mypy in on %} [![Type Checker](https://img.shields.io/badge/mypy-steelblue?style={{ cookiecutter.badge_style }}&logo=python&logoColor=white&labelColor=gray)](https://mypy-lang.org/){% endif %} [![Dependency Manager](https://img.shields.io/badge/uv-mediumpurple?style={{ cookiecutter.badge_style }}&logo=uv&labelColor=gray)](https://docs.astral.sh/uv/){% if cookiecutter.pre_commit in on %} [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style={{ cookiecutter.badge_style }}&logo=pre-commit&logoColor=white&labelColor=gray)](https://pre-commit.com/){% endif %}{% if cookiecutter.github_actions in on %} [![CI](https://img.shields.io/badge/GitHub_Actions-forestgreen?style={{ cookiecutter.badge_style }}&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions){% endif %} [![Editor Settings](https://img.shields.io/badge/Editor_Config-paleturquoise?style={{ cookiecutter.badge_style }}&logo=editorconfig&labelColor=gray)](https://editorconfig.org/) [![Repository Template](https://img.shields.io/badge/snickerdoodle-bisque?style={{ cookiecutter.badge_style }}&logo=cookiecutter&labelColor=gray)](https://www.github.com/WithPrecedent/snickerdoodle){% if cookiecutter.dependabot in on %} [![Dependency Maintainer](https://img.shields.io/badge/dependabot-forestgreen?style={{ cookiecutter.badge_style }}&logo=dependabot&logoColor=white&labelColor=gray)](https://github.com/dependabot){% endif %} |
| Compatibility | {% if cookiecutter.pypi in on %}[![Compatible Python Versions](https://img.shields.io/pypi/pyversions/{{ cookiecutter.package_name }}?style={{ cookiecutter.badge_style }}&color=cornflowerblue&label=Python&logo=python&logoColor=yellow)](https://pypi.org/project/{{ cookiecutter.package_name }}/){% else %}[![Compatible Python Versions](https://img.shields.io/badge/Python-3.11+-cornflowerblue?style={{ cookiecutter.badge_style }}&logo=python&logoColor=yellow)](https://www.python.org/){% endif %} [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style={{ cookiecutter.badge_style }}&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-antiquewhite?style={{ cookiecutter.badge_style }}&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/Windows-blue?style={{ cookiecutter.badge_style }})](https://www.microsoft.com/en-us/windows?r=1) |
| Stats |{% if cookiecutter.pypi in on %} [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/{{ cookiecutter.package_name }}?style={{ cookiecutter.badge_style }}&color=cornflowerblue&label=Downloads%20💾&logo=pypi&logoColor=yellow)](https://pypi.org/project/{{ cookiecutter.package_name }}/){% endif %} [![GitHub Stars](https://img.shields.io/github/stars/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}?style={{ cookiecutter.badge_style }}&color=forestgreen&label=Stars%20⭐&logo=github)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}?style={{ cookiecutter.badge_style }}&color=forestgreen&label=Contributors%20🙋&logo=github)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}?style={{ cookiecutter.badge_style }}&color=forestgreen&label=Issues%20📘&logo=github)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}/issues) [![GitHub Forks](https://img.shields.io/github/forks/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}?style={{ cookiecutter.badge_style }}&color=forestgreen&label=Forks%20🍴&logo=github)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}/forks) |
| | |

-----

## What is {{cookiecutter.project_name}}?

[TODO: Brief summary of the project]

## Why use {{cookiecutter.project_name}}?

[TODO: Features and reasons to use the project (and, possibly, not to use it)]

## Getting started

### Requirements

[TODO: List any OS or other restrictions and pre-installation dependencies]

### Installation

To install `{{ cookiecutter.project_name }}`, use `pip`:

```sh
{% if cookiecutter.pypi in on %}pip install {{ cookiecutter.package_name }}{% else %}pip install git+https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repo_name }}.git{% endif %}
```

### Usage

[TODO: Describe common use cases, with possible example(s)]

## Contributing

Contributors are always welcome. Feel free to grab an [issue](https://www.github.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}/issues) to work on or make a suggested improvement. If you wish to contribute, please read the [Contribution Guide](https://www.github.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}/blob/main/CONTRIBUTING.md) and [Code of Conduct](https://www.github.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}/blob/main/CODE_OF_CONDUCT.md).

## Similar Projects

[TODO: If they exist, it is always nice to acknowledge other similar efforts]

## Acknowledgments

[TODO: Mention any people or organizations that warrant a special acknowledgment]

## License

Use of this repository is authorized under the [{{cookiecutter.license}}](https://www.github.com/{{cookiecutter.github_user}}/{{cookiecutter.repo_name}}/blob/main/LICENSE).
