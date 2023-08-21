# snickerdoodle

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&label=pypi&logo=PyPI&color=darkorange)](https://pypi.org/project/snickerdoodle/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/snickerdoodle?style=for-the-badge&label=branch&logo=github&color=navy)](https://github.com/WithPrecedent/snickerdoodle/releases)
| Status | [![Development Status](https://img.shields.io/badge/Development-Active-Green?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/badge/stability-beta-firebrick?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&logo=apache&color=goldenrod)](https://opensource.org/licenses/Apache-2.0)
| Docs | [![Hosted By](https://img.shields.io/badge/hosted_by-github_pages-blue?style=for-the-badge&logo=github&color=navy)](https://withprecedent.github.io/snickerdoodle)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&logo=python&color=darkorange)](https://pypi.python.org/pypi/snickerdoodle/) [![Linux](https://img.shields.io/badge/linux-maroon?style=for-the-badge&logo=linux&labelColor=gray)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/macos-yellow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=windows&labelColor=gray)](https://www.microsoft.com/en-us/windows?r=1)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/snickerdoodle?style=for-the-badge&logo=pypi&color=darkorange)](https://pypi.org/project/snickerdoodle) [![GitHub Contributors](https://img.shields.io/github/contributors/withprecedent/snickerdoodle?style=for-the-badge&label=contributors&logo=github&color=darksalmon)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Contributors](https://img.shields.io/github/issues/withprecedent/snickerdoodle?style=for-the-badge&label=issues&logo=github&color=deeppink)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Stars](https://img.shields.io/github/stars/withprecedent/snickerdoodle?style=for-the-badge&label=Stars&logo=github&color=firebrick)](https://github.com/withprecedent/snickerdoodle/stargazers) [![GitHub Forks](https://img.shields.io/github/forks/withprecedent/snickerdoodle?style=for-the-badge&label=forks&logo=github&color=coral)](https://github.com/withprecedent/snickerdoodle/forks)
| Tools | [![Documentation](https://img.shields.io/badge/mkdocs-magenta?style=for-the-badge&logo=markdown&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) [![Template Manager](https://img.shields.io/badge/cookiecutter-brown?style=for-the-badge&logo=cookiecutter&labelColor=gray)](https://www.cookiecutter.io/)
| | |

-----

## What is snickerdoodle?

`snickerdoodle`is an easy-to-use, general-purpose cookiecutter template for Python projects utilizing `pdm`, `mkdocs`, GitHub Actions, `ruff`, and other modern tools. To see what a repository looks like using the template, you can check out [`snickerdoodle_demo`](https://github.com/withprecedent/snickerdoodle_demo).

## Why use snickerdoodle?

There are an enormous number of cookiecutter templates. However, many are difficult to use, inflexible, and/or underdocumented. I created `snickerdoodle` because I couldn't find another `cookiecutter` template meeting these criteria:

* Modern: most templates are older and do not use current best practices, such as [`pyproject.toml`](https://peps.python.org/pep-0621/) and one of the [numerous dependency managers](https://jairoandres.com/management-dependencies-in-python/) that make project management much easier.
* PEP-Compatible: all included tools should meet the design specifications of all finalized [PEPs](https://peps.python.org/pep-0001/) (that rules out `poetry`, which, three years after PEP adoption, is still not [PEP 621](https://peps.python.org/pep-0621/) compatible).
* No External Services: I wanted a template that didn't require external services offering CI/CD, code coverage, code analysis, etc. This is particularly true for services that are neither free nor open-source (e.g. [sonarcloud.io](https://www.sonarsource.com/products/sonarcloud/), which is in an increasing number of newer templates).
* (Nearly) Turn-Key: a template should be easy to deploy and immediately use without having to understand or examine the underlying code.
* Flexible: beyond the core tools, a template should be easy to add other components too (including external services that you use).

To meet those goals, `snickerdoodle` uses [`pdm`](https://pdm.fming.dev/latest/), a modern dependency manager (that follows PEP 621 syntax), GitHub Actions for CI/CD, and GitHub Pages for documentation hosting. The only other dependency for the template is, obviuosly, `cookiecutter`.

Further, rather than adopting a rigid, opinionated approach, `snickerdoodle` includes nice-looking and functional defaults (like the badges table above, which will include several other badges in your created project). There are also nice extras, like an automatically generated credits page in the documentation, that should work with any Python project. `snickerdoodle`  makes no assumptions about the type of Python project you are creating and includes base template options that are (nearly) universal.

## Getting started

This section describes the basic usage of the `snickerdoodle` template. If you want to modify its settings or have other questions, you should consult the [template user guide](https://withprecedent.github.io/snickerdoodle/advanced/).

### Requirements

To use `snickerdoodle` and the repository that it creates, you need [`python`](https://www.python.org/), [`git`](https://git-scm.com/), [`cookiecutter`](https://www.cookiecutter.io/) (or [`cruft`](https://github.com/cruft/cruft)), and [`pdm`](https://pdm.fming.dev/latest/) installed on your system. You also need a GitHub account. If you have not already, set up your GitHub credentials on your local computer.

### Setup

If you are new to cookiecutter or simply want to make sure the created repository works as intended, follow the instructions in the [`snickerdoodle` tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/).

If you are familiar with creating cookiecutter templates, you can go about the normal template construction process with one important addition: after you create the remote repository on GitHub, change Settings/Actions/General/Workflow Permissions to "Read and Write Permissions." This is necessary for the repository documentation to be properly deployed. Then, follow the instructions for setting up your [virtual environment](https://withprecedent.github.io/snickerdoodle/tutorial/#Create-Virtual-Environment) and [deploying your documentation](https://withprecedent.github.io/snickerdoodle/tutorial/#Deploy-Documentation) in the [`snickerdoodle` tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/). It is especially important to follow the document deployment process for the first time - after that GitHub Actions will automatically update and redeploy the documentation (and you need not use the manual process again).

## Usage

After your repository is created, you can start setting the dependencies in `pyproject.toml`. Every push to GitHub will run any tests in the "Tests" folder, deploy documentation, and apply `ruff`. If you wish to publish your repository to [PyPi](https://pypi.org), I recommend using the [`pdm publish` command](https://pdm.fming.dev/latest/usage/publish/).

## Contributing

Contributors are always welcome and should find `snickerdoodle` easy to work with. The template is highly documented so that users and developers can make `snickerdoodle` work with their projects. Feel free to grab an issue to work on or make a suggested improvement. If you wish to contribute, please read the [Contribution Guide](./contributing.md) and [Code of Conduct](./code_of_conduct.md).

## Similar Projects

These are other templates using `pdm` as their dependency manager:

* [cookiecutter-docker-python-pdm](https://github.com/mnako/cookiecutter-docker-python-pdm): uses Docker and `black`.
* [cookie](https://github.com/chris-santiago/cookie): uses `mkdocs` and Github Actions, but also adds `conda`, Nox, `black`, and `pyright`.

And, these are other general-purpose templates that are well-maintained, modern, and well-documented:

* [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python): uses, among other tools, `sphinx`, GitHub Actions, Nox, `mypy`, `flake8`, and `poetry`. If you do not mind those choices and wanted a modern, maintained template, this is the one to use.
* [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary): a newer template that is minimal compared to most and uses, among other tools, `sphinx`, GitHub Actions, Setuptools, Tox, and Travis-CI.
* [wolt python package cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter): an interesting template that uses [`cruft`](https://github.com/cruft/cruft) instead of base `cookiecutter`. The created repository uses, among other tools, 'mkdocs', GitHub Actions, `black`, `flake8`, and `poetry`.

## Acknowledgements

I'd also like to extend a special thanks to [pawamoy](https://github.com/pawamoy) whose excellent pdm and mkdocs extensions and utlities are incorporated into `snickerdoodle`. Some of the scripts, documentation, configuration files, and other CI code were all adapted from pawamoy's repositories.

I would also like to thank the University of Kansas School of Law for tolerating and supporting this law professor's coding efforts, an endeavor which is well outside the typical scholarly activities in the discipline.
