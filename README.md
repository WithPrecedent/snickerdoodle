# snickerdoodle

<div align="center">

| | |
| --- | --- |
| Status | [![CI Build](https://img.shields.io/github/actions/workflow/status/GITHUB_USER/snickerdoodle/update.yml?branch=main&label=tests&style=for-the-badge&logo=pytest)](https://github.com/GITHUB_USER/snickerdoodle/actions/workflows/update.yml?query=branch%3Amain) [![Code Coverage](https://img.shields.io/codecov/c/github/GITHUB_USER/snickerdoodle?style=for-the-badge&logo=codecov&logoColor=white)](https://codecov.io/gh/GITHUB_USER/snickerdoodle) [![Project Status](https://img.shields.io/badge/Development-Active-Green?style=for-the-badge&logo=git)](https://www.repostatus.org/#active)
| Package | [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&logo=PyPI)](https://pypi.org/project/snickerdoodle/) [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&logo=python)](https://pypi.python.org/pypi/snickerdoodle/) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&logo=apache)](https://opensource.org/licenses/Apache-2.0)
| Docs | [![Hosted By](https://img.shields.io/badge/hosted_by-github_pages-blue?style=for-the-badge&logo=github)](https://WithPrecedent.github.io/snickerdoodle) [![Documentation](https://img.shields.io/badge/theme-MkDocs%20material-yellow.svg?style=for-the-badge&logo=markdown)](https://WithPrecedent.github.io/snickerdoodle)
| Tools | [![Linter](https://img.shields.io/endpoint?style=for-the-badge&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff) [![Dependency Manager](https://img.shields.io/badge/PDM-blueviolet?style=for-the-badge&logo=affinity&labelColor=gray)](https://PDM.fming.dev) [![Template](https://img.shields.io/badge/cookiecutter-brown?style=for-the-badge&logo=cookiecutter&labelColor=gray)](https://www.cookiecutter.io/) [![Pre-commit](https://img.shields.io/badge/pre--commit-brightgreen?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml) [![CI](https://img.shields.io/badge/github_actions-yellow?style=for-the-badge&logo=githubactions&labelColor=gray)](https://github.com/features/actions)[![Editor Settings](https://img.shields.io/badge/editor_config-blue?style=for-the-badge&logo=editorconfig&labelColor=gray)](https://github.com/features/actions)
| | |

</div>

-----

## What is snickerdoodle?

*`snickerdoodle` is still under heavy construction and is not feature complete (see Issues for missing features).*

`snickerdoodle`is an easy-to-use cookiecutter template for Python projects utilizing `PDM`, `MkDocs`, `GitHub Actions`, `Ruff`, and other modern tools.

## Why use snickerdoodle?

There are an enormous number of cookiecutter templates. However, many are difficult to use, inflexible, and underdocumented. Also, many template use tools that do not meet the requirements of PEPs approved in recent years. In contrast, `snickerdoodle` incorporates:

* [PDM](https://PDM.fming.dev/latest/): although [Poetry](https://python-poetry.org/) is more popular, its syntax [is not compliant](https://github.com/python-poetry/roadmap/issues/3) with [PEP 621](https://peps.python.org/pep-0621/). I was a long-time `Poetry` user, but eventually ran into some packages and libraries (particularly `MkDocs` extensions) that would not properly install because of `Poetry`'s non-standard `pyproject.toml` formatting. `PDM` is not yet as polished as `Poetry`, but it is rock-solid and I have never run into dependency installation issues with it.
* [MkDocs](https://www.MkDocs.org/): similarly, `sphinx` is the dominant documentation package, but it is not nearly as accessible as `MkDocs`, which allows all of your documentation to be created in Markdown and is beautiful out-of-the-box when using the [Material Theme](https://squidfunk.github.io/MkDocs-material/).
* [Ruff](https://github.com/astral-sh/Ruff): a relatively new player in formatting, it aims to serve as a one-stop, extremely fast (it's written in `Rust`) formatting and linting package. `snickerdoodle` implements some reasonable defaults while still allowing user flexibility (e.g., it does not implement [Black](https://github.com/psf/black) - although you can do that through `Ruff`, if you would prefer). By default, it activates the parts of `Ruff` that apply, among other packages: `Flake8`, `Bandit`, `pydocstyle`, and `pylint`.
* [Github Actions](https://github.com/features/actions): if you store your package on Github, which `snickerdoodle` assumes, [there are strong reasons](https://resources.github.com/devops/tools/automation/actions/) to prefer `Github Actions` as your CI/CD tool. `snickerdoodle` includes workflows for updating, releasing, and publishing your package while also deploying the accompanying documentation.
* [GitHub Pages](https://pages.github.com/): There is a lot to be said for [Read the Docs](https://readthedocs.com) as a documentation host site. However, `MkDocs` works better on `GitHub Pages` and once you start using `GitHub Actions`, the automatic updating advantage of `Read the Docs` disappears. I also like that `GitHub Pages` is not dependent on ads placed on documentation pages for its survival. This was a close call and I might consider adding a `Read the Docs` option in a future version of `snickerdoodle`.
* Flexible templates: rather than adopting a rigid, opinionated approach, `snickerdoodle` includes nice-looking and functional defaults (like the badges table above, which will include several other badges in your created project). In addition to the packages above, there are nice extras, like an automatically generated credits page in the documentation, that should work with any Python project. It makes no assumptions about the type of Python project you are creating but includes template options that are (nearly) universal.

## Getting started

## Requirements

### Installation

In addition to `git`, you must have `cookiecutter` installed on your system, as follows:

```sh
pip install --user cookiecutter
```

To create a repository from the `snickerdoodle` template, you can use `cookiecutter` to access it directly from GitHub:

```sh
cookiecutter gh:WithPrecedent/snickerdoodle
```

Or, you can clone the repository and then apply the template:

```sh
git clone git@github.com:WithPrecedent/snickerdoodle.git
cookiecutter snickerdoodle/
```

### Usage

After your repository is created, you can start setting the dependencies in `pyproject.toml` and then build your distribution using `PDM install`. This will also create a virtual environment for your project that you may using for testing, debugging, and documentation deployment.

#### Change GitHub Repository Settings

Unfortunately, there is no way to integrate GitHub repository settings into a `cookiecutter` template. There are two settings in your repository that you should change for your project based on `snickerdoodle` should work.

1) Change Settings/Display/Pages/Source to "GitHub Actions". This will delegate documentation construction and deployment to `GitHub Actions` and prevent it from automatically running an extra action for documentation deployment.
2) Change Settings/Actions/General/Workflow Permissions to "Read and Write Permissions." This is necessary for proper documentation deployment.

#### Badges

If you would prefer the standard [Shields.io dynamic badges](https://shields.io) instead of the "for-the-badge" style used in `snickerdoodle`, do a find and replace in the `readme.md` file to replace "?style=for-the-badge&" with "?" and "?style=for-the-badge" with "". A pending issue for this template is to make this an option in the `cookiecutter` construction.

#### Formatting and Linting

All of the options for `Ruff` are incorporated into the created project's `pyproject.toml` file. So, you can adjust any [`Ruff` rules](https://beta.Ruff.rs/docs/rules/) there.

#### Versioning

When you publish a new version, you should first manually adjust the version in the created repository's `__init__.py` file. It will then be automatically adjusted in `pyproject.toml` as well. I decided not to use automatic semantic versioning because the process thinks so many minor updates are "major" and you will find yourself on version 12.0.0 and still in alpha or beta.

## Contributing

Contributors are always welcome and should find `snickerdoodle` easy to work with. The template is highly documented so that users and developers can make `snickerdoodle` work with their projects. Feel free to grab an issue to work on or make a suggested improvement. If you wish to contribute, please read the [Contribution Guide](./contributing.md) and [Code of Conduct](./code_of_conduct.md).

## Similar Projects

These are other templates using `PDM`:

* [cookiecutter-docker-python-PDM](https://github.com/mnako/cookiecutter-docker-python-PDM): template which uses `Docker` and `Black`.
* [cookie](https://github.com/chris-santiago/cookie): simlar to `snickerdoodle`, this template uses `MkDocs` and `Github Actions`, but also adds `Conda`, `Nox`, `Black`, and `PyRight`.

## Acknowledgements
