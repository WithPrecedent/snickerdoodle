# snickerdoodle

<p align="center">
<img src="https://github.com/WithPrecedent/snickerdoodle/blob/main/docs/img/snickerdoodle.png?raw=true" alt="snickerdoodle cookie logo" style="width:250px;"/>
</p>

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&color=steelblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/snickerdoodle/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/snickerdoodle?style=for-the-badge&color=navy&label=GitHub&logo=github)](https://github.com/WithPrecedent/snickerdoodle/releases)
| Status | [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/badge/Stability-Beta-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) 
| Documentation | [![Hosted By](https://img.shields.io/badge/hosted_by-GitHub_Pages-blue?style=for-the-badge&color=navy&logo=github)](https://withprecedent.github.io/snickerdoodle)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&color=steelblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/snickerdoodle/) [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style=for-the-badge&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-snow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=Windows&labelColor=gray&color=orangered)](https://www.microsoft.com/en-us/windows?r=1)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/snickerdoodle?style=for-the-badge&color=steelblue&label=Downloads%20💾&logo=pypi&logoColor=yellow)](https://pypi.org/project/snickerdoodle) [![GitHub Stars](https://img.shields.io/github/stars/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Stars%20⭐&logo=github)](https://github.com/withprecedent/snickerdoodle/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Contributors%20🙋&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Issues%20📘&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Forks](https://img.shields.io/github/forks/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Forks%20🍴&logo=github)](https://github.com/withprecedent/snickerdoodle/forks) |
| | |

## What is snickerdoodle?

`snickerdoodle`is an easy-to-use, general-purpose cookiecutter template for
Python projects utilizing modern tools and best practices. To see an example repository using this template,
check out
[`snickerdoodle_demo`](https://github.com/withprecedent/snickerdoodle_demo).
  
## Why use snickerdoodle?

There are a lot of cookiecutter templates. However, many are difficult to use,
overly opinionated, or underdocumented. I created `snickerdoodle` because I
couldn't
find another `cookiecutter` template meeting these criteria:

* **Modern**: follows best practices, using modern, actively developed tools
* **Batteries Included**: allows you to start coding immediately
* **Flexible**: no required usage of any external services
  (SonarCloud, Travis, CircleCI, Tox, etc.)
* **Low-Maintenance**: every commit automatically deploys the documentation as
  well as
  lints, formats, and tests the repository
  
* **Well-Documented**: the
  [documentation](https://withprecedent.github.io/snickerdoodle) includes
  complete guides for basic and advanced users
* **PEP-Compliant**: all included tools follow accepted
  [PEPs](https://peps.python.org/pep-0001/) (unfortunately, that ruled out using
  `poetry`, which is [still not](https://github.com/python-poetry/roadmap/issues/3) [PEP 621](https://peps.python.org/pep-0621/) or
  [PEP 631](https://peps.python.org/pep-0631/)
  compliant, three years after they were accepted,
  [resulting in compatibility](https://github.com/python-poetry/poetry/issues/496)
  [problems because of its](https://github.com/python-poetry/poetry/issues/3332)
  [non-standard `pyproject.toml` format](https://github.com/python-poetry/poetry/issues/8415)).

### Tools

`snickerdoodle` includes modern, stable tools for package construction and
management that do not require any external services or costs:
* Dependency Management: [![Dependency Manager](https://img.shields.io/badge/PDM-mediumpurple?style=flat-square&logo=affinity&labelColor=gray)](https://PDM.fming.dev) and [![Dependency Maintainer](https://img.shields.io/badge/dependabot-navy?style=flat-square&logo=dependabot&logoColor=white&labelColor=gray)](https://github.com/dependabot)
* Documentation:
  [![Documentation Tool](https://img.shields.io/badge/MkDocs-magenta?style=flat-square&color=deepskyblue&logo=markdown&labelColor=gray)](https://www.mkdocs.org/)
  with [![Documentation Theme](https://img.shields.io/badge/Material-magenta?style=flat-square&color=deepskyblue&logo=material-design&logoColor=white&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) theme
  on [![Documentation Host](https://img.shields.io/badge/GitHub_Pages-blue?style=flat-square&color=navy&logo=github&labelColor=gray)](https://withprecedent.github.io/snickerdoodle)
* Testing: [![Testing](https://img.shields.io/badge/pytest-steelblue?style=flat-square&logo=pytest&logoolor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml)
* CI/CD: [![CI](https://img.shields.io/badge/GitHub_Actions-navy?style=flat-square&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions)
* Code Style:
  [![Linter](https://img.shields.io/endpoint?style=flat-square&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff),
  [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=flat-square&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml),
  and [![Editor Settings](https://img.shields.io/badge/Editor_Config-paleturquoise?style=flat-square&logo=editorconfig&labelColor=gray)](https://editorconfig.org/)
* Templating: [![Template Manager](https://img.shields.io/badge/Cookiecutter-bisque?style=flat-square&logo=cookiecutter&labelColor=gray)](https://www.cookiecutter.io/)

### Options

In addition to the included tools above, `snickerdoodle` includes several
options in the `cookiecutter` questionnaire that can be automatically applied
as part of the templating process:
* Badge Style: [![flat
  style](https://img.shields.io/badge/flat-crimson?style=flat)](https://www.shields.io/),
  [![flat-square
  style](https://img.shields.io/badge/flat--square-orange?style=flat-square)](https://www.shields.io/),
  [![for-the-badge
  style](https://img.shields.io/badge/For--the--badge-blue?style=for-the-badge)](https://www.shields.io/),
  [![plastic
  style](https://img.shields.io/badge/plastic-purple?style=plastic)](https://www.shields.io/),
 or [![social
  style](https://img.shields.io/badge/social-red?style=social)](https://www.shields.io/)
* Push an [Initial Commit](https://github.com/WithPrecedent/snickerdoodle_demo) to GitHub
* Build and Deploy [Basic Documentation](https://withprecedent.github.io/snickerdoodle_demo/) to GitHub Pages
* Create a Virtual Environment in the Repository's ".venv" Folder

## Getting started

### Requirements

To use `snickerdoodle` and the repository that it creates, you just need:
* [`python`](https://www.python.org/) 3.8 or later
* [`git`](https://git-scm.com/)
* [`cookiecutter`](https://www.cookiecutter.io/),
  [`cruft`](https://github.com/cruft/cruft), or
  [`cookieninja`](https://github.com/cookieninja-generator/cookieninja)
* [`pdm`](https://pdm.fming.dev/latest/)
* A [GitHub](https://github.com/) account
  
To take advantage of the automatic initial commit to GitHub,
you should also [store your credentials](https://docs.github.com/en/get-started/quickstart/set-up-git) on
your computer.

### Setup

If you are new to `cookiecutter` or simply want to guarantee that the created repository works as intended, follow the instructions in the [`snickerdoodle` tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/).

If you are familiar with creating `cookiecutter` templates, you can go about the
normal template construction process with a two important additions.

First,
after you create the remote repository on GitHub, change
"Settings/Actions/General/Workflow Permissions" to "Read and Write Permissions."
This is necessary for the repository documentation to be properly deployed.  

Second, if you do not select the optional
automatic setup features, you should follow the instructions
for manually setting up your [virtual
environment](https://withprecedent.github.io/snickerdoodle/tutorial/#Create-Virtual-Environment)
and [deploying your
documentation](https://withprecedent.github.io/snickerdoodle/tutorial/#Deploy-Documentation)
in the [`snickerdoodle`
tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/). It is
especially important to follow the document deployment process for your initial deployment - after that GitHub Actions will automatically update and redeploy the
documentation (and you need not use the manual process again).

## Usage

After your repository is created, you can start coding right away. Every push to GitHub will run any tests in the "tests" folder,
deploy documentation to GitHub Pages, and apply `ruff` for linting and formatting. If you wish to publish your repository
to [PyPI](https://pypi.org), I recommend using the [`pdm publish`
command](https://pdm.fming.dev/latest/usage/publish/) or the `publish` GitHub
Action (with can be activated directly from your GitHub repository's Actions
page), if you set up PyPI to recognize the Action as a [trusted
publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).

For
other questions or issues, consult the [Advanced User
  Guide](https://withprecedent.github.io/snickerdoodle/advanced/) in the
  `snickerdoodle` documentation.

## Contributing

Contributors are always welcome and should find `snickerdoodle` easy to work
with. The template is highly documented so that users and developers can adapt
or extend`snickerdoodle` to work with their projects. So, forking and creating
different template spins is encouraged. If you want to contribute directly to
the project, feel free to grab an [issue](https://github.com/WithPrecedent/snickerdoodle/issues) to work on
or make a suggested improvement. If you wish to contribute, please read the
[Contribution Guide](./contributing.md) and [Code of
Conduct](./code_of_conduct.md).

## Similar Projects

These are other `cookiecutter` templates using `pdm` as their dependency manager:

* [cookiecutter-docker-python-pdm](https://github.com/mnako/cookiecutter-docker-python-pdm): uses Docker and `black`.
* [cookie](https://github.com/chris-santiago/cookie): uses `mkdocs` and GitHub Actions, but also adds `conda`, `nox`, `black`, and `pyright`.

And, these are other general-purpose `cookiecutter` templates that are well-maintained, modern, and well-documented:

* [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python): uses, among other tools, `sphinx`, GitHub Actions, `nox`, `mypy`, `flake8`, and `poetry`. If you do not mind those choices and wanted a modern, maintained template, this is the one to use.
* [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary): a newer template that is minimal compared to most and uses, among other tools, `sphinx`, GitHub Actions, `setuptools`, Tox, and Travis-CI.
* [wolt python package cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter): an interesting template that uses [`cruft`](https://github.com/cruft/cruft) instead of base `cookiecutter`. The created repository uses, among other tools, `mkdocs`, GitHub Actions, `black`, `flake8`, and `poetry`.

If you are interested in going beyond `cookiecutter` (or its forks),
[`copier`](https://github.com/copier-org/copier) is a powerful, newer templating package
and there is a great template that incorporates
several of the tools used in `snickerdoodle`:

* [copier-pdm](https://github.com/pdm-project/copier-pdm): includes, among other
 tools, `pdm`,
  `mkdocs`, and `ruff`.

## Acknowledgements

I'd also like to extend a special thanks to [pawamoy](https://github.com/pawamoy) whose excellent `pdm` and `mkdocs` extensions and utlities are incorporated into `snickerdoodle`. Some of the scripts, documentation, configuration files, and other CI code were all adapted from pawamoy's repositories.

I would also like to thank the University of Kansas School of Law for tolerating and supporting this law professor's coding efforts, an endeavor which is well outside the typical scholarly activities in the discipline.

## License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&color=firebrick&logo=apache)](https://opensource.org/licenses/Apache-2.0)
