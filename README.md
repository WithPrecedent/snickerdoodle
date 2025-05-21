# snickerdoodle

<p align="center">
<img src="https://github.com/WithPrecedent/snickerdoodle/blob/main/docs/img/snickerdoodle.png?raw=true" alt="snickerdoodle cookie logo" style="width:200px;"/>
</p>

| | |
| --- | --- |
| Status| [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&color=cornflowerblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/snickerdoodle/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/snickerdoodle?style=for-the-badge&color=forestgreen&label=GitHub&logo=github)](https://github.com/WithPrecedent/snickerdoodle/releases) [![Project Stability](https://img.shields.io/pypi/status/snickerdoodle?style=for-the-badge&logo=pypi&label=Stability&logoColor=yellow)](https://pypi.org/project/snickerdoodle/) |
| Documentation | [![Hosted By](https://img.shields.io/badge/hosted_by-GitHub_Pages-blue?style=for-the-badge&color=forestgreen&logo=github)](https://withprecedent.github.io/snickerdoodle) |
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&color=cornflowerblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/snickerdoodle/) |
| | |

## What is snickerdoodle?

`snickerdoodle` is an easy-to-use, general-purpose `cookiecutter` template for
Python projects utilizing modern tools and best practices. To see an demo repository using this template,
check out
[`snickerdoodle_demo`](https://github.com/withprecedent/snickerdoodle_demo).

## Why use snickerdoodle?

In contrast to highly-opinated templates, `snickerdoodle` has limited requirements with powerful options that users can opt into in the `cookiecutter` questionnaire.
If you want `snickerdoodle` to support other options, please make a [feature request or contribute](#contributing).

* **Requirements**:
  * Dependency Management: [![Dependency Manager](https://img.shields.io/badge/uv-mediumpurple?style=flat-square&logo=uv&labelColor=gray)](https://docs.astral.sh/uv/)
  * Linting: [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
  * Testing:
  [![Testing](https://img.shields.io/badge/pytest-cornflowerblue?style=flat-square&logo=pytest&logoolor=white&labelColor=gray)](https://docs.pytest.org/en/stable/)
  * Templater: [![cookiecutter](https://img.shields.io/badge/cookiecutter-antiquewhite?style=flat-square&logo=cookiecutter&labelColor=gray)](https://cookiecutter.readthedocs.io/en/stable/)
* **Options Supported**:
  * Automated Hooks: [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=flat-square&logo=pre-commit&logoColor=white&labelColor=gray)](https://pre-commit.com/)
  * Badge Styles:
    * [![flat style](https://img.shields.io/badge/flat-crimson?style=flat)](https://www.shields.io/)
    * [![flat-square style](https://img.shields.io/badge/flat--square-orange?style=flat-square)](https://www.shields.io/)
    * [![for-the-badge style](https://img.shields.io/badge/For--the--badge-blue?style=for-the-badge)](https://www.shields.io/)
    * [![plastic style](https://img.shields.io/badge/plastic-purple?style=plastic)](https://www.shields.io/)
    * [![social style](https://img.shields.io/badge/social-red?style=social)](https://www.shields.io/)
  * CI/CD: [![CI](https://img.shields.io/badge/GitHub_Actions-forestgreen?style=flat-square&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions)
  * Code Coverage: [![Coverage](https://img.shields.io/badge/codecov-pink?style=flat-square&logo=codecov&logoolor=white&labelColor=gray)](https://about.codecov.io/)
  * Dependency Updater: [![Dependency Maintainer](https://img.shields.io/badge/dependabot-forestgreen?style=flat-square&logo=dependabot&logoColor=white&labelColor=gray)](https://github.com/dependabot)
  * Documentation: [![Documentation Tool](https://img.shields.io/badge/MkDocs-magenta?style=flat-square&color=deepskyblue&logo=markdown&labelColor=gray)](https://www.mkdocs.org/)   on [![Documentation Host](https://img.shields.io/badge/GitHub_Pages-blue?style=flat-square&color=forestgreen&logo=github&labelColor=gray)](https://withprecedent.github.io/snickerdoodle)
  automatically built and deployed with every commit
  * Publishing:
    * [![PyPI](https://img.shields.io/badge/PyPI-yellow?style=flat-square&logo=pypi&labelColor=gray&logoColor=white)](https://github.com/features/actions)
      with [![GitHub
      Actions](https://img.shields.io/badge/GitHub_Actions-forestgreen?style=flat-square&logo=github&labelColor=gray&logoColor=white)](https://github.com/features/actions)
      using `publish.yml`
    * [![Repo Host](https://img.shields.io/badge/GitHub-blue?style=flat-square&color=forestgreen&logo=github&labelColor=gray)](https://github.com) automatically with any commit beginning with a version number (e.g., "0.2.3")
  * Repository Initialization: [![Repo Host](https://img.shields.io/badge/GitHub-blue?style=flat-square&color=forestgreen&logo=github&labelColor=gray)](https://github.com)
    with an [initial commit](https://github.com/WithPrecedent/snickerdoodle_demo)
  * Virtual Environment Creation: [![Virtural Environment Manager](https://img.shields.io/badge/uv-mediumpurple?style=flat-square&logo=uv&labelColor=gray)](https://docs.astral.sh/uv/)

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
