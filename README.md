# snickerdoodle
<!-- 
<div align="center"> -->

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&label=pypi&logo=PyPI&color=darkorange)](https://pypi.org/project/snickerdoodle/) [![GitHub Latest Release](https://img.shields.io/github/tag/withprecedent/snickerdoodle?style=for-the-badge&label=branch&logo=github&color=navy)](https://github.com/withprecedent/snickerdoodle/graphs/tags) 
| Status | [![Build Status](https://img.shields.io/github/actions/workflow/status/withprecedent/snickerdoodle/ci.yml?branch=main&label=tests&style=for-the-badge&logo=pytest&color=cadetblue)](https://github.com/withprecedent/snickerdoodle/actions/workflows/ci.yml?query=branch%3Amain) [![Code Coverage](https://img.shields.io/codecov/c/github/withprecedent/snickerdoodle?style=for-the-badge&logo=codecov&logoColor=white)](https://codecov.io/gh/withprecedent/snickerdoodle) [![Development Status](https://img.shields.io/badge/Development-Active-Green?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/badge/Stability-Alpha-firebrick?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&logo=apache&color=goldenrod)](https://opensource.org/licenses/Apache-2.0)
| Docs | [![Hosted By](https://img.shields.io/badge/hosted_by-github_pages-blue?style=for-the-badge&logo=github&color=navy)](https://withprecedent.github.io/snickerdoodle)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&logo=python&color=darkorange)](https://pypi.python.org/pypi/snickerdoodle/) [![Linux](https://img.shields.io/badge/linux-maroon?style=for-the-badge&logo=linux&labelColor=gray)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/macos-yellow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=windows&labelColor=gray)](https://www.microsoft.com/en-us/windows?r=1)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/snickerdoodle?style=for-the-badge&logo=pypi&color=darkorange)](https://pypi.org/project/snickerdoodle) [![GitHub Contributors](https://img.shields.io/github/contributors/withprecedent/snickerdoodle?style=for-the-badge&label=contributors&logo=github&color=darksalmon)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Contributors](https://img.shields.io/github/issues/withprecedent/snickerdoodle?style=for-the-badge&label=issues&logo=github&color=deeppink)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Stars](https://img.shields.io/github/stars/withprecedent/snickerdoodle?style=for-the-badge&label=Stars&logo=github&color=firebrick)](https://github.com/withprecedent/snickerdoodle/stargazers) [![GitHub Forks](https://img.shields.io/github/forks/withprecedent/snickerdoodle?style=for-the-badge&label=forks&logo=github&color=coral)](https://github.com/withprecedent/snickerdoodle/forks)
| Tools | [![Documentation](https://img.shields.io/badge/MkDocs-magenta?style=for-the-badge&logo=markdown&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) [![Linter](https://img.shields.io/endpoint?style=for-the-badge&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff) [![Dependency Manager](https://img.shields.io/badge/PDM-blueviolet?style=for-the-badge&logo=affinity&labelColor=gray)](https://PDM.fming.dev) [![Pre-commit](https://img.shields.io/badge/pre--commit-brightgreen?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml) [![CI](https://img.shields.io/badge/github_actions-yellow?style=for-the-badge&logo=githubactions&labelColor=gray)](https://github.com/features/actions) [![Editor Settings](https://img.shields.io/badge/editor_config-blue?style=for-the-badge&logo=editorconfig&labelColor=gray)](https://github.com/features/actions) [![Template Manager](https://img.shields.io/badge/cookiecutter-brown?style=for-the-badge&logo=cookiecutter&labelColor=gray)](https://www.cookiecutter.io/)
| | |

<!-- </div> -->

-----

## What is snickerdoodle?

*`snickerdoodle` is still under heavy construction and is not feature complete (see Issues for missing features).*

`snickerdoodle`is an easy-to-use cookiecutter template for Python projects utilizing `PDM`, `MkDocs`, GitHub Actions, `Ruff`, and other modern tools. To see what a repository looks like using the template, you can check out [`snickerdoodle_demo`](https://github.com/withprecedent/snickerdoodle_demo).

## Why use snickerdoodle?

There are an enormous number of cookiecutter templates. However, many are difficult to use, inflexible, and underdocumented. I use `snickerdoodle` in my projects and will continue to update it while meeting the goals desribed above. I created `snickerdoodle` because I couldn't find another `cookiecutter` template meeting these criteria:

* Modern: most templates are older and do not use current best practices, such as [`pyproject.toml`](https://peps.python.org/pep-0621/) and one of the [numerous dependency managers](https://jairoandres.com/management-dependencies-in-python/) that make project management much easier.
* PEP-Compatible: all included tools should meet the design specifications of all finalized [PEPs](https://peps.python.org/pep-0001/) (that rules out `Poetry`, which, three years after PEP adoption, is still not [PEP 621](https://peps.python.org/pep-0621/) compatible).
* No External Services: I wanted a template that didn't require external services offering CI/CD, code coverage, code analysis, etc. This is particularly true for services that are neither free nor open-source (e.g. [sonarcloud.io](https://www.sonarsource.com/products/sonarcloud/), which is in an increasing number of newer templates).
* (Nearly) Turn-Key: a template should be easy to deploy and immediately use without having to understand or examine the underlying code.
* Flexible: beyond the core tools, a template should be easy to add other components too (included external services that you use).

To meet those goals, `snickerdoodle` uses [`PDM`](https://PDM.fming.dev/latest/), a modern dependency manager (that meets PEP 621 requirements), GitHub Actions for CI/CD, and GitHub Pages for documentation hosting. The only other requirement is, obviuosly, `cookiecutter`. Further, rather than adopting a rigid, opinionated approach, `snickerdoodle` includes nice-looking and functional defaults (like the badges table above, which will include several other badges in your created project). There are also nice extras, like an automatically generated credits page in the documentation, that should work with any Python project. It makes no assumptions about the type of Python project you are creating but includes template options that are (nearly) universal.

## Getting started

These are the tools that `snickerdoodle` incorporates:

* [`PDM`](https://PDM.fming.dev/latest/): although [Poetry](https://python-poetry.org/) is more popular, as mentioned earlier, its syntax [is not compliant](https://github.com/python-poetry/roadmap/issues/3) with [PEP 621](https://peps.python.org/pep-0621/). I was a long-time `Poetry` user, but eventually ran into some packages and libraries (particularly `MkDocs` extensions) that would not properly install because of `Poetry`'s non-standard `pyproject.toml` formatting. `PDM` is not yet as polished as `Poetry`, but it is rock-solid and I have never run into dependency installation issues with it.
* [`MkDocs`](https://www.MkDocs.org/): similarly, `sphinx` is the dominant documentation package, but it is not nearly as accessible as `MkDocs`, which allows all of your documentation to be created in Markdown and is beautiful out-of-the-box when using the [Material Theme](https://squidfunk.github.io/MkDocs-material/).
* [`Ruff`](https://github.com/astral-sh/Ruff): a relatively new player in formatting, it aims to serve as a one-stop, extremely fast (it's written in `Rust`) formatting and linting package. `snickerdoodle` implements some reasonable defaults while still allowing user flexibility (e.g., it does not implement [Black](https://github.com/psf/black) - although you can do that through `Ruff`, if you would prefer). By default, the template activates the parts of `Ruff` that incorporate, among other packages: `Flake8`, `Bandit`, `pydocstyle`, and `pylint`.
* [Github Actions](https://github.com/features/actions): if you store your package on Github, which `snickerdoodle` assumes, [there are strong reasons](https://resources.github.com/devops/tools/automation/actions/) to prefer Github Actions as your CI/CD tool. `snickerdoodle` includes workflows for updating, releasing, and publishing your package while also deploying the accompanying documentation.
* [GitHub Pages](https://pages.github.com/): There is a lot to be said for [Read the Docs](https://readthedocs.com) as a documentation host site. However, `MkDocs` works better on GitHub Pages and once you start using GitHub Actions, the automatic updating advantage of Read the Docs disappears. I also like that GitHub Pages is not dependent on ads placed on documentation pages for its survival. This was a close call and I might consider adding a Read the Docs option in a future version of `snickerdoodle`.

### Requirements

To use `snickerdoodle`, you need [`python`](https://www.python.org/), [`git`](https://git-scm.com/), [`cookiecutter`](https://www.cookiecutter.io/) (or [`cruft`](https://github.com/cruft/cruft)), and [`PDM`](https://PDM.fming.dev/latest/) installed on your system. You also need a GitHub account.

### Installation

To create a repository from the `snickerdoodle` template, you can use `cookiecutter` to access it directly from GitHub:

```sh
cookiecutter gh:WithPrecedent/snickerdoodle
```

Or, you can clone the repository and then apply the template:

```sh
# Go to folder where your cookiecutter templates are stored locally.
git clone git@github.com:WithPrecedent/snickerdoodle.git
# Go to folder where your code repostiories are stored locally.
cookiecutter snickerdoodle/
```

### Usage

As with any `cookiecutter`, project generation requires you to answer several questions. `snickerdoodle` attempts to make this process quick, easy, and painless. The default options, often created from your previous answers, are sensible so that you can just hit "return" in reponse to most questions. The questionnaire is derived from the `cookiecutter.json` file, if you wish to implement different questions. There are couple distinctions between questions worth mentioning:

* "project_name" refers to the title for the project that you would like to appear on the top of the README file and docs. Spaces and capital letters are allowed in the "project_name".
* "package_name" means the name used to store the package at [PyPi](https://pypi.org). Dashes, but not underscores or capital letters, are allowed in the "package_name." The default option will be the "project_name" with any spaces converted to dashes and all uppercase letters changed to lowercase.
* "repo_name" is the end of the URL for the repository. Underscores, but not dashes or capital letters, are allowed in the "package_name." The default option will be the "project_name" with any spaces converted to underscores and all uppercase letters changed to lowercase.

So, if you have a "project_name" of "MeowMeow Beans", the "package_name" would be "meowmeow-beans" and the "repo_name" would be "meowmeow_beans." For single word, lowercase packages, there are no differences between the three names. Unless you have a really good reason, you should simply accept the defaults for the "package_name" and "repo_name."

After your repository is created, you can start setting the dependencies in `pyproject.toml` and then build your distribution using `pdm install`. This will also create a virtual environment for your project that you may using for testing, debugging, and documentation deployment.

#### Change GitHub Repository Settings

Unfortunately, there is no easy way to integrate GitHub repository settings into a `cookiecutter` template. There are two settings in your repository that you should change for your project based on `snickerdoodle` to work.

1) In your repository, change Settings/Display/Pages/Source to "GitHub Actions". This will delegate documentation construction and deployment to GitHub Actions and prevent it from automatically running an extra action for documentation deployment.
2) In your repository, change Settings/Actions/General/Workflow Permissions to "Read and Write Permissions." This is necessary for proper documentation deployment.

#### Badges

If you would prefer the standard [Shields.io dynamic badges](https://shields.io) instead of the "for-the-badge" style used in `snickerdoodle`, do a find and replace in the `readme.md` file to replace "?style=for-the-badge&" with "?" and "?style=for-the-badge" with "". A pending issue for this template is to make this an option in the `cookiecutter` construction.

#### Formatting and Linting

All of the options for `Ruff` are incorporated into the created project's `pyproject.toml` file. So, you can adjust any [`Ruff` rules](https://beta.Ruff.rs/docs/rules/) there.

#### Versioning

When you publish a new version, you should first manually adjust the version in the created repository's `__init__.py` file. It will then be automatically adjusted in `pyproject.toml` as well. I decided not to use automatic semantic versioning because the process thinks so many minor updates are "major" and you will [find yourself on version 12.0.0](https://hynek.me/articles/semver-will-not-save-you/) and still in alpha or beta.

## Contributing

Contributors are always welcome and should find `snickerdoodle` easy to work with. The template is highly documented so that users and developers can make `snickerdoodle` work with their projects. Feel free to grab an issue to work on or make a suggested improvement. If you wish to contribute, please read the [Contribution Guide](./contributing.md) and [Code of Conduct](./code_of_conduct.md).

## Similar Projects

These are other templates using `PDM`:

* [cookiecutter-docker-python-PDM](https://github.com/mnako/cookiecutter-docker-python-PDM): template which uses `Docker` and `Black`.
* [cookie](https://github.com/chris-santiago/cookie): simlar to `snickerdoodle`, this template uses `MkDocs` and `Github Actions`, but also adds `Conda`, `Nox`, `Black`, and `PyRight`.

## Acknowledgements

I'd also like to extend a special thanks to [pawamoy](https://github.com/pawamoy) whose excellent PDM and MkDocs extensions and utlities are incorporated into `snickerdoodle`. Some of the scripts, documentation, configuration files, and other CI code were all adapted from pawamoy's repositories.

I would also like to thank the University of Kansas School of Law for tolerating and supporting this law professor's coding efforts, an endeavor which is well outside the typical scholarly activities in the discipline.
