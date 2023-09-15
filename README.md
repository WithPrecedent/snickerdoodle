# snickerdoodle

<p align="center">
<img src="https://github.com/WithPrecedent/snickerdoodle/blob/main/docs/img/snickerdoodle.png?raw=true" alt="snickerdoodle cookie logo" style="width:250px;"/>
</p>

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&color=steelblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/snickerdoodle/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/snickerdoodle?style=for-the-badge&color=navy&label=Release&logo=github)](https://github.com/WithPrecedent/snickerdoodle/releases)
| Status | [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/badge/Stability-Beta-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&color=firebrick&logo=apache)](https://opensource.org/licenses/Apache-2.0)
| Docs | [![Hosted By](https://img.shields.io/badge/hosted_by-GitHub_Pages-blue?style=for-the-badge&color=navy&logo=github)](https://withprecedent.github.io/snickerdoodle)
| Tools | [![Documentation](https://img.shields.io/badge/MkDocs-magenta?style=for-the-badge&color=deepskyblue&logo=markdown&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) [![Linter](https://img.shields.io/endpoint?style=for-the-badge&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff) [![Dependency Manager](https://img.shields.io/badge/PDM-mediumpurple?style=for-the-badge&logo=affinity&labelColor=gray)](https://PDM.fming.dev) [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml) [![CI](https://img.shields.io/badge/GitHub_Actions-navy?style=for-the-badge&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions) [![Editor Settings](https://img.shields.io/badge/Editor_Config-paleturquoise?style=for-the-badge&logo=editorconfig&labelColor=gray)](https://editorconfig.org/) [![Template Manager](https://img.shields.io/badge/Cookiecutter-bisque?style=for-the-badge&logo=cookiecutter&labelColor=gray)](https://www.cookiecutter.io/) [![Dependency Maintainer](https://img.shields.io/badge/dependabot-navy?style=for-the-badge&logo=dependabot&logoColor=white&labelColor=gray)](https://github.com/dependabot)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/snickerdoodle?style=for-the-badge&color=steelblue&label=Downloads%20💾&logo=pypi&logoColor=yellow)](https://pypi.org/project/snickerdoodle) [![GitHub Stars](https://img.shields.io/github/stars/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Stars%20⭐&logo=github)](https://github.com/withprecedent/snickerdoodle/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Contributors%20🙋&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Issues%20📘&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Forks](https://img.shields.io/github/forks/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Forks%20🍴&logo=github)](https://github.com/withprecedent/snickerdoodle/forks)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&color=steelblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/snickerdoodle/) [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style=for-the-badge&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-snow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=Windows&labelColor=gray&color=orangered)](https://www.microsoft.com/en-us/windows?r=1)
| | |

-----

## What is snickerdoodle?

`snickerdoodle`is an easy-to-use, general-purpose cookiecutter template for
Python projects utilizing `pdm`, `mkdocs`, `ruff`, `pre-commit`, GitHub Actions,
and other modern tools. To see what a repository looks like using this template,
check out
[`snickerdoodle_demo`](https://github.com/withprecedent/snickerdoodle_demo).

## Why use snickerdoodle?

There are a lot of cookiecutter templates. However, many are difficult to use,
highly opinionated, or underdocumented. I created `snickerdoodle` because I couldn't
find another `cookiecutter` template meeting these criteria:

* **Modern**: follows best practices, using modern, actively developed tools
  (see the badges table above for the core tools used and the [Advanced User
  Guide](https://withprecedent.github.io/snickerdoodle/advanced/#core-components)
  for explanations why those tools were selected).
* **Batteries Included**: sets up a fresh repository, basic
  documentation, and a smart project configuration. It also includes options to
  automatically and securely push an initial commit to GitHub, build and deploy
  the basic documentation on GitHub Pages, and create a local virtual
  environment with `pdm`. This allows you to start coding right away.
* **Flexible**: incorporates GitHub's best resources (Actions, Pages, and
  Dependabot) without mandating the usage of any other external services
  (SonarCloud, Travis, CircleCI, Tox, etc.). `snickerdoodle` makes adding such features easy, but without
  forcing you to accept services that you do not want.
* **Low-Maintenance**: utilizing GitHub Actions, every commit to GitHub will run all
  tests, lint the code, and deploy updated documentation. Among other included Actions are
  workflows to publish your repository to PyPI and merge a development branch
  into the main branch. You might never need to use the terminal again (unless
  you want to).
* **Thoughtful**: rather than adopting a rigid, opinionated approach,
  `snickerdoodle` uses reasonable, but easy-to-change, defaults. It also
  offers some extras to make your repository look great (like the
  badges table above for which you can select your preferred badge style during
  the repository construction process) and the automatically
  generated credits page in your created repository's documentation (credit for
  that goes to [pawamoy](https://github.com/pawamoy)).
* **Well-Documented**: unlike many templates, the internal and [external
  documentation](https://withprecedent.github.io/snickerdoodle) make it easy for you to understand and modify the
  template, if you desire.
* **PEP-Compliant**: all included tools follow accepted
  [PEPs](https://peps.python.org/pep-0001/) (unfortunately, that rules out using
  `poetry`, which is [still not](https://github.com/python-poetry/roadmap/issues/3) [PEP 621](https://peps.python.org/pep-0621/) or
  [PEP 631](https://peps.python.org/pep-0631/)
  compliant, three years after they were accepted,
  [resulting in compatibility](https://github.com/python-poetry/poetry/issues/496)
  [problems because of its](https://github.com/python-poetry/poetry/issues/3332)
  [non-standard `pyproject.toml` format](https://github.com/python-poetry/poetry/issues/8415)).

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
deploy documentation, and apply `ruff` for linting and formatting. If you wish to publish your repository
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
* [cookie](https://github.com/chris-santiago/cookie): uses `mkdocs` and GitHub Actions, but also adds `conda`, Nox, `black`, and `pyright`.

And, these are other general-purpose `cookiecutter` templates that are well-maintained, modern, and well-documented:

* [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python): uses, among other tools, `sphinx`, GitHub Actions, Nox, `mypy`, `flake8`, and `poetry`. If you do not mind those choices and wanted a modern, maintained template, this is the one to use.
* [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary): a newer template that is minimal compared to most and uses, among other tools, `sphinx`, GitHub Actions, Setuptools, Tox, and Travis-CI.
* [wolt python package cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter): an interesting template that uses [`cruft`](https://github.com/cruft/cruft) instead of base `cookiecutter`. The created repository uses, among other tools, 'mkdocs', GitHub Actions, `black`, `flake8`, and `poetry`.

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
