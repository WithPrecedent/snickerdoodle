# snickerdoodle

<p align="center">
<img src="https://github.com/WithPrecedent/snickerdoodle/blob/main/docs/img/snickerdoodle.png?raw=true" alt="snickerdoodle cookie logo" style="width:250px;"/>
</p>

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&color=steelblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/snickerdoodle/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/snickerdoodle?style=for-the-badge&color=navy&label=GitHub&logo=github)](https://github.com/WithPrecedent/snickerdoodle/releases) |
| Status | [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/pypi/status/snickerdoodle?style=for-the-badge&logo=pypi&label=Stability&logoColor=yellow)](https://pypi.org/project/snickerdoodle/) |
| Documentation | [![Hosted By](https://img.shields.io/badge/hosted_by-GitHub_Pages-blue?style=for-the-badge&color=navy&logo=github)](https://withprecedent.github.io/snickerdoodle) |
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&color=steelblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/snickerdoodle/) [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style=for-the-badge&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-snow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/)  [![Windows](https://img.shields.io/badge/Windows-blue?style=for-the-badge)](https://www.microsoft.com/en-us/windows?r=1) |
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/snickerdoodle?style=for-the-badge&color=steelblue&label=Downloads%20💾&logo=pypi&logoColor=yellow)](https://pypi.org/project/snickerdoodle) [![GitHub Stars](https://img.shields.io/github/stars/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Stars%20⭐&logo=github)](https://github.com/withprecedent/snickerdoodle/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Contributors%20🙋&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Issues%20📘&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Forks](https://img.shields.io/github/forks/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Forks%20🍴&logo=github)](https://github.com/withprecedent/snickerdoodle/forks) |
| | |

## What is snickerdoodle?

`snickerdoodle` is an easy-to-use, general-purpose cookiecutter template for
Python projects utilizing modern tools and best practices. To see an example repository using this template,
check out
[`snickerdoodle_demo`](https://github.com/withprecedent/snickerdoodle_demo).

## Why use snickerdoodle?

There are a lot of cookiecutter templates. However, many are difficult to use,
overly opinionated, or underdocumented. I created `snickerdoodle` because I
couldn't find another `cookiecutter` template meeting these criteria:

* **Modern**: follows best practices, using modern, actively developed tools.
* **Batteries Included**: allows you to start coding immediately.
* **Flexible**: no required usage of any external services.
  (SonarCloud, Travis, CircleCI, Tox, etc.).
* **Low-Maintenance**: every commit automatically deploys the documentation as
  well as lints, formats, and tests the repository.
* **Powerful**: supports easy publication to GitHub and PyPI.
* **Well-Documented**: the
  [documentation](https://withprecedent.github.io/snickerdoodle) includes
  complete guides for [new](https://withprecedent.github.io/snickerdoodle/tutorial/) and [advanced](https://withprecedent.github.io/snickerdoodle/advanced/) users.
* **PEP-Compliant**: all included tools follow accepted
  [PEPs](https://peps.python.org/pep-0001/), particularly [PEP 621](https://peps.python.org/pep-0621/) and
  [PEP 631](https://peps.python.org/pep-0631/).

### Tools

To accomplish those goals, `snickerdoodle` includes modern, stable tools for package construction and
management that do not require any external services or costs:

* Dependency Management: [![Dependency Manager](https://img.shields.io/badge/uv-mediumpurple?style=flat-square&logo=uv&labelColor=gray)](https://docs.astral.sh/uv/)
* Documentation:
  [![Documentation Tool](https://img.shields.io/badge/MkDocs-magenta?style=flat-square&color=deepskyblue&logo=markdown&labelColor=gray)](https://www.mkdocs.org/)
  on [![Documentation Host](https://img.shields.io/badge/GitHub_Pages-blue?style=flat-square&color=navy&logo=github&labelColor=gray)](https://withprecedent.github.io/snickerdoodle)
* Testing:
  [![Testing](https://img.shields.io/badge/pytest-steelblue?style=flat-square&logo=pytest&logoolor=white&labelColor=gray)](https://docs.pytest.org/en/stable/)
  and
  [![Coverage](https://img.shields.io/badge/codecov-pink?style=flat-square&logo=codecov&logoolor=white&labelColor=gray)](https://about.codecov.io/) (optional)
* CI/CD: [![CI](https://img.shields.io/badge/GitHub_Actions-navy?style=flat-square&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions)
* Code Style and Linting:
  [![Linter](https://img.shields.io/endpoint?style=flat-square&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff) and
  [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=flat-square&logo=pre-commit&logoColor=white&labelColor=gray)](https://pre-commit.com/)

* Type-Checking: [![Type-Checker](https://img.shields.io/badge/mypy-blue?style=flat-square)](https://mypy-lang.org/)

* Templating: [![Template Manager](https://img.shields.io/badge/Cookiecutter-bisque?style=flat-square&logo=cookiecutter&labelColor=gray)](https://www.cookiecutter.io/)

### Options

In addition to the included tools above, `snickerdoodle` includes several
options in the `cookiecutter` questionnaire that can be automatically applied
as part of the templating process:

* Badge style: [![flat
  style](https://img.shields.io/badge/flat-crimson?style=flat)](https://www.shields.io/),
  [![flat-square
  style](https://img.shields.io/badge/flat--square-orange?style=flat-square)](https://www.shields.io/),
  [![for-the-badge
  style](https://img.shields.io/badge/For--the--badge-blue?style=for-the-badge)](https://www.shields.io/),
  [![plastic
  style](https://img.shields.io/badge/plastic-purple?style=plastic)](https://www.shields.io/),
 or [![social
  style](https://img.shields.io/badge/social-red?style=social)](https://www.shields.io/)
* A repo and [initial commit](https://github.com/WithPrecedent/snickerdoodle_demo) to GitHub
* Build and deploy [documentation](https://withprecedent.github.io/snickerdoodle_demo/) to GitHub Pages
* Create a virtual environment using `uv`.

## Getting started

### Setup

If you are new to `cookiecutter` or simply want to guarantee that the created repository works as intended, follow the instructions in the [`snickerdoodle` tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/).

If you are familiar with `cookiecutter` templates, you can go about the
normal construction process. However, if you do not select the optional
automatic setup features in the questionnaire, you should follow the instructions
for manually setting up your [virtual
environment](https://withprecedent.github.io/snickerdoodle/tutorial/#Create-Virtual-Environment)
and [deploying your
documentation](https://withprecedent.github.io/snickerdoodle/tutorial/#Deploy-Documentation)
in the [`snickerdoodle`
tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/). It is
especially important to follow the document deployment process for your initial deployment - after that GitHub Actions will automatically update and redeploy the
documentation (and you need not use the manual process again).

### Usage

After your repository is created, you can start coding right away. Every push to GitHub will run any tests in the "tests" folder,
deploy documentation to GitHub Pages, and apply `ruff` for linting and
formatting. For more information about the following topics, just click on the
corresponding hyperlink.

* [Formatting and Linting](https://withprecedent.github.io/snickerdoodle/advanced/#formatting-and-linting)
* [GitHub Actions](https://withprecedent.github.io/snickerdoodle/advanced/#github-actions)
* [Publishing](https://withprecedent.github.io/snickerdoodle/advanced/#publishing)
* [Repository Layout](https://withprecedent.github.io/snickerdoodle/advanced/#repository-layout)
* [Versioning](https://withprecedent.github.io/snickerdoodle/advanced/#versioning)

## Contributing

Contributors are always welcome and should find `snickerdoodle` easy to work
with. The template is highly documented so that users and developers can adapt
or extend `snickerdoodle` to work with their projects. So, forking and creating
different template spins is encouraged. If you want to contribute directly, feel free to grab an [issue](https://github.com/WithPrecedent/snickerdoodle/issues) to work on
or make a suggested improvement. If you wish to contribute, please read the
[Contribution Guide](./contributing.md) and [Code of
Conduct](./code_of_conduct.md).

## Similar Projects

These are other `cookiecutter` templates using `uv` as their dependency manager:

* [cookiecutter-uv-hypermodern-python](https://github.com/bosd/cookiecutter-uv-hypermodern-python):
  an opinionated template that
  uses, among other tools, `sphinx`, GitHub Actions, `nox`, `mypy`, `typeguard`,
  Prettier, Click,
  and `ruff`. If you do not mind those choices and wanted a modern, maintained
  template, this is the one to use.
* [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv): uses `ruff`,
  `mypy`, `tox`, `mkdocs`, and `deptry`.
* [ultraviolet](https://github.com/chris-santiago/cookie): a basic
  template that requires Homebrew.

## Acknowledgements

I'd also like to extend a special thanks to [pawamoy](https://github.com/pawamoy) whose excellent `mkdocs` extensions and utlities are incorporated into `snickerdoodle`. Some of the scripts, documentation, configuration files, and other CI code were all adapted from pawamoy's repositories.

I would also like to thank the University of Kansas School of Law for tolerating and supporting this law professor's coding efforts, an endeavor which is well outside the typical scholarly activities in the discipline.

## License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&color=firebrick&logo=apache)](https://opensource.org/licenses/Apache-2.0)
