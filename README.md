# snickerdoodle

<p align="center">
<img src="https://github.com/WithPrecedent/snickerdoodle/blob/main/docs/img/snickerdoodle.png?raw=true" alt="snickerdoodle cookie logo" style="width:250px;"/>
</p>

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/snickerdoodle.svg?style=for-the-badge&color=steelblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/snickerdoodle/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/snickerdoodle?style=for-the-badge&color=navy&label=Release&logo=github)](https://github.com/WithPrecedent/snickerdoodle/releases)
| Status | [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/badge/Stability-Beta-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge&color=firebrick&logo=apache)](https://opensource.org/licenses/Apache-2.0)
| Docs | [![Hosted By](https://img.shields.io/badge/hosted_by-GitHub_Pages-blue?style=for-the-badge&color=navy&logo=github)](https://withprecedent.github.io/snickerdoodle)
| Tools | [![Documentation](https://img.shields.io/badge/MkDocs-magenta?style=for-the-badge&color=deepskyblue&logo=markdown&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) [![Dependency Manager](https://img.shields.io/badge/PDM-mediumpurple?style=for-the-badge&logo=affinity&labelColor=gray)](https://PDM.fming.dev) [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml) [![CI](https://img.shields.io/badge/GitHub_Actions-navy?style=for-the-badge&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions) [![Editor Settings](https://img.shields.io/badge/Editor_Config-paleturquoise?style=for-the-badge&logo=editorconfig&labelColor=gray)](https://editorconfig.org/) [![Template Manager](https://img.shields.io/badge/Cookiecutter-bisque?style=for-the-badge&logo=cookiecutter&labelColor=gray)](https://www.cookiecutter.io/)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/snickerdoodle?style=for-the-badge&color=steelblue&label=Downloads&logo=pypi&logoColor=yellow)](https://pypi.org/project/snickerdoodle) [![GitHub Stars](https://img.shields.io/github/stars/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Stars&logo=github)](https://github.com/withprecedent/snickerdoodle/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Contributors&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Issues&logo=github)](https://github.com/withprecedent/snickerdoodle/graphs/contributors) [![GitHub Forks](https://img.shields.io/github/forks/withprecedent/snickerdoodle?style=for-the-badge&color=navy&label=Forks&logo=github)](https://github.com/withprecedent/snickerdoodle/forks)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/snickerdoodle?style=for-the-badge&color=steelblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/snickerdoodle/) [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style=for-the-badge&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-snow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=Windows&labelColor=gray&color=orangered)](https://www.microsoft.com/en-us/windows?r=1)
| | |

-----

## What is snickerdoodle?

`snickerdoodle`is an easy-to-use, general-purpose cookiecutter template for Python projects utilizing `pdm`, `mkdocs`, GitHub Actions, `ruff`, and other modern tools. To see what a repository looks like using the template, you can check out [`snickerdoodle_demo`](https://github.com/withprecedent/snickerdoodle_demo).

## Why use snickerdoodle?

There are an enormous number of cookiecutter templates. However, many are difficult to use, inflexible, and/or underdocumented. I created `snickerdoodle` because I couldn't find another `cookiecutter` template meeting these criteria:

* **Modern**: follows best practices, using modern, actively developed tools.
* **No Required Services**: beyond GitHub, you can use whatever code coverage or analysis tools you like.
* **PEP-Compliant**: all of the tools follow all finalized
  [PEPs](https://peps.python.org/pep-0001/) (unfortunately, that rules out `poetry`, which,
  three years after the PEP adoption, is still not [PEP
  621](https://peps.python.org/pep-0621/) compliant).
* **Thoughtful**: rather than adopting a rigid, opinionated approach,
  `snickerdoodle` uses reasonable, but easy-to-change, defaults. It also
  offers some extras to make your repository look great (like the
  badges table above, which will include several other badges in your created
  project and you can select your preferred badge style) and the automatically
  generated credits page in your created repository's documentation (credit for
  that goes
to [pawamoy](https://github.com/pawamoy)).
* **Well-Documented**: unlike many templates, the internal and [external
  documentation](https://withprecedent.github.io/snickerdoodle) make it easy for you to understand, and, thus, modify the
  template.

To meet those goals, `snickerdoodle` uses [`pdm`](https://pdm.fming.dev/latest/), a modern dependency manager (that follows PEP 621 syntax), GitHub Actions for CI/CD, and `mkdocs`  on GitHub Pages for documentation. The only other dependency for the template is, obviuosly, `cookiecutter`.

## Getting started

### Requirements

To use `snickerdoodle` and the repository that it creates, you need [`python`](https://www.python.org/), [`git`](https://git-scm.com/), [`cookiecutter`](https://www.cookiecutter.io/) (or [`cruft`](https://github.com/cruft/cruft)), and [`pdm`](https://pdm.fming.dev/latest/) installed on your system. You also need a GitHub account. If you have not already, set up your [GitHub credentials](https://docs.github.com/en/get-started/quickstart/set-up-git) on your computer.

### Setup

If you are new to `cookiecutter` or simply want to guarantee that the created repository works as intended, follow the instructions in the [`snickerdoodle` tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/).

If you are familiar with creating cookiecutter templates, you can go about the
normal template construction process with a two important additions. First, after you
create the remote repository on GitHub, change "Settings/Actions/General/Workflow
Permissions" to "Read and Write Permissions." This is necessary for the
repository documentation to be properly deployed. Second, follow the instructions
for setting up your [virtual
environment](https://withprecedent.github.io/snickerdoodle/tutorial/#Create-Virtual-Environment)
and [deploying your
documentation](https://withprecedent.github.io/snickerdoodle/tutorial/#Deploy-Documentation)
in the [`snickerdoodle`
tutorial](https://withprecedent.github.io/snickerdoodle/tutorial/). It is
especially important to follow the document deployment process for your initial deployment - after that GitHub Actions will automatically update and redeploy the
documentation (and you need not use the manual process again).

## Usage

After your repository is created, you can start setting the dependencies in
`pyproject.toml`. Every push to GitHub will run any tests in the "tests" folder,
deploy documentation, and apply `ruff`. If you wish to publish your repository
to [PyPI](https://pypi.org), I recommend using the [`pdm publish`
command](https://pdm.fming.dev/latest/usage/publish/) or the `publish` GitHub
Action, if you set up PyPI to recognize the Action as a [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/).

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

These are other templates using `pdm` as their dependency manager:

* [cookiecutter-docker-python-pdm](https://github.com/mnako/cookiecutter-docker-python-pdm): uses Docker and `black`.
* [cookie](https://github.com/chris-santiago/cookie): uses `mkdocs` and GitHub Actions, but also adds `conda`, Nox, `black`, and `pyright`.

And, these are other general-purpose templates that are well-maintained, modern, and well-documented:

* [cookiecutter-hypermodern-python](https://github.com/cjolowicz/cookiecutter-hypermodern-python): uses, among other tools, `sphinx`, GitHub Actions, Nox, `mypy`, `flake8`, and `poetry`. If you do not mind those choices and wanted a modern, maintained template, this is the one to use.
* [cookiecutter-pylibrary](https://github.com/ionelmc/cookiecutter-pylibrary): a newer template that is minimal compared to most and uses, among other tools, `sphinx`, GitHub Actions, Setuptools, Tox, and Travis-CI.
* [wolt python package cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter): an interesting template that uses [`cruft`](https://github.com/cruft/cruft) instead of base `cookiecutter`. The created repository uses, among other tools, 'mkdocs', GitHub Actions, `black`, `flake8`, and `poetry`.

## Acknowledgements

I'd also like to extend a special thanks to [pawamoy](https://github.com/pawamoy) whose excellent pdm and mkdocs extensions and utlities are incorporated into `snickerdoodle`. Some of the scripts, documentation, configuration files, and other CI code were all adapted from pawamoy's repositories.

I would also like to thank the University of Kansas School of Law for tolerating and supporting this law professor's coding efforts, an endeavor which is well outside the typical scholarly activities in the discipline.
