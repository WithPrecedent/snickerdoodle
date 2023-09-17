# Advanced User Guide

## Configuration File

If you use `cookiecutter` a lot (or plan to do so), I suggest [creating a
configuration
file](https://cookiecutter.readthedocs.io/en/2.3.0/advanced/user_config.html)
with some answers to the questionnaire. For example, I have included a
basic configuration file in this repository:
[`cc_config.yaml`](https://github.com/WithPrecedent/snickerdoodle/blob/main/cc_config.yaml).
You can then use the configuration file (which you should probably put in the
parent folder for your code repositories) when you call `cookiecutter` as
follows:

``` sh
cookiecutter gh:WithPrecedent/snickerdoodle --config-file cc_config.yaml
```

## Core Components

These are the tools that `snickerdoodle` incorporates and a brief explanation as
to why they were chosen:

* [`pdm`](https://pdm.fming.dev/latest/): although
  [`poetry`](https://python-poetry.org/) is more popular, its syntax [is not
  compliant](https://github.com/python-poetry/roadmap/issues/3) with [PEP
  621](https://peps.python.org/pep-0621/) and  [PEP 631](https://peps.python.org/pep-0631/). I was a long-time `poetry` user, but
  eventually ran into some packages and libraries (particularly `mkdocs`
  extensions) that would not properly install because of `poetry`'s non-standard
  `pyproject.toml` formatting. `pdm` is not yet as polished as `poetry`, but it
  is rock-solid and I have never run into dependency installation issues with
  it.
* [`mkdocs`](https://www.mkdocs.org/): similarly,
  [`sphinx`](https://www.sphinx-doc.org/en/master/) is the dominant
  documentation package, but it is not nearly as [easy to use as `mkdocs`](https://squidfunk.github.io/mkdocs-material/alternatives/), which allows
  all of your documentation to be created in Markdown and is beautiful
  out-of-the-box when using the [Material
  Theme](https://squidfunk.github.io/mkdocs-material/). I chose to prioritize
  accessibility so that you do not waste time trying to properly format and
  design your documentation.
* [`ruff`](https://github.com/astral-sh/ruff): a relatively new player in formatting, it aims to serve as a one-stop, extremely fast (it's written in `Rust`) formatting and linting package. `snickerdoodle` implements some reasonable defaults while still allowing user flexibility (e.g., it does not implement [`black`](https://github.com/psf/black) - although you can do that through `ruff`, if you would prefer). By default, the template activates the parts of `ruff` that incorporate, among other packages: `Flake8`, `Bandit`, `pydocstyle`, and `pylint`.
* [Github Actions](https://github.com/features/actions): if you store your package on Github, which `snickerdoodle` assumes, [there are strong reasons](https://resources.github.com/devops/tools/automation/actions/) to prefer Github Actions as your CI/CD tool. `snickerdoodle` includes workflows for updating, releasing, and publishing your package while also deploying the accompanying documentation.
* [GitHub Pages](https://pages.github.com/): There is a lot to be said for [Read the Docs](https://readthedocs.com) as a documentation host site. However, `mkdocs` works better on GitHub Pages and once you start using GitHub Actions, the automatic updating advantage of Read the Docs disappears. I also like that GitHub Pages is not dependent on ads placed on documentation pages for its survival. This was a close call and I might consider adding a Read the Docs option in a future version of `snickerdoodle`.

## File Structure

Your new repository will have the following structure. The files and folders
that you will ordinarily modify are highlighted and commented.

``` sh hl_lines=" 1 5 15 19 21 22 23 25 26 27 28"
├── CHANGELOG.md              # Main changelog to record changes
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docs
│   ├── advanced.md           # Add core documentation beyond the tutorial
│   ├── changelog.md
│   ├── code_of_conduct.md
│   ├── contributing.md
│   ├── credits.md
│   ├── css
│   │   ├── material.css
│   │   └── mkdocstrings.css
│   ├── index.md
│   ├── license.md
│   ├── recipes.md            # Add examples and recipes
│   ├── scripts
│   │   ├── gen_credits.py
│   │   └── gen_ref_nav.py
│   └── tutorial.md           # Add basic tutorial
├── LICENSE
├── mkdocs.yml                # Change documentation structure
├── pyproject.toml            # Add dependencies or project metadata
├── README.md                 # This will also be the docs landing page
├── src
│   └── {repository name}     # Add Python modules
│       └── __init__.py       # Update import info and version 
└── tests                     # Add other test files
    └── test_main.py          # Follow the 'test_NAME' convention
```

## Formatting and Linting

All of the formatting and linting options of the created project are implemented through `ruff` and are incorporated into the created
project's `pyproject.toml` file. So, you can adjust any [`ruff`
rules](https://beta.ruff.rs/docs/rules/) there. I have included comments in the
`pyproject.toml` file for rules that are excluded and packages that are included
so that you know which rules are enforced. `ruff` is automatically run with
each GitHub push. However, that only creates a report of problems with the
repository. To automatically fix them, I suggest using `pre-commit`. The created
repository has a `pre-commit` command to run `ruff` with the `fix` option
invoked. To use `pre-commit`, follow its [user
guide](https://pre-commit.com/#usage). If you activate `pre-commit`, it will then be automatically run on every push to GitHub.

## GitHub Actions

These are the available actions for a repository created by `snickerdoodle` that
are located in the ".github" folder and on the GitHub repository page under "Actions":

| GitHub Action | Trigger | Jobs |
| --- | --- | --- |
| `ci` | automatically on push | builds repo, runs tests, lints, formats, builds docs, and deploys docs |
| `build` | another Action | builds repo |
| `document` | another Action or manually on GitHub| builds and deploys docs |
| `lint` | another Action or manually on GitHub | lints repository with `ruff` |
| `merge` | another Action or manually on GitHub | merges `development` branch into `main` (currently untested Action) |
| `publish` | another Action or manually on GitHub | publishes repository on PyPI (must configure PyPI to accept as [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)) |

To run an Action on GitHub, go to your repository, click "Actions" and select
one of the Actions listed on the left side of the screen. Only those Actions
listed in the chart above with manual triggers can be activated via GitHub.

## Versioning

When you publish a new version, you should first manually adjust the version in the created repository's `__init__.py` file. It will then be automatically adjusted in `pyproject.toml` as well. I decided not to use automatic semantic versioning because the process thinks so many minor updates are "major" and you will [find yourself on version 12.0.0](https://hynek.me/articles/semver-will-not-save-you/) and still in alpha or beta. And, while [calendar versioning](https://calver.org/) makes sense, it is alien and confusing to users unfamiliar with it.
