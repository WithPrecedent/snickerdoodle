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

```sh
cookiecutter gh:WithPrecedent/snickerdoodle --config-file cc_config.yaml
```

## Core Components

These are the tools that `snickerdoodle` incorporates and a brief explanation as
to why they were chosen:

* [`uv`](https://docs.astral.sh/uv/): `uv` is PEP-compliant, incredibly fast,
  and is quickly becoming
  the leading Python dependency manager.
* [`mkdocs`](https://www.mkdocs.org/):
[`sphinx`](https://www.sphinx-doc.org/en/master/) is the dominant
documentation package, but it is not nearly as [easy to use as `mkdocs`](https://squidfunk.github.io/mkdocs-material/alternatives/), which allows
all of your documentation to be created in Markdown and is beautiful
out-of-the-box when using the [Material
Theme](https://squidfunk.github.io/mkdocs-material/). I chose to prioritize
accessibility so that you do not waste time trying to properly format and
design your documentation.
* [`ruff`](https://github.com/astral-sh/ruff): A relatively new player in formatting, it aims to serve as a one-stop,
extremely fast (it's written in `Rust`) formatting and linting package.
`snickerdoodle` implements some reasonable defaults while still allowing user
flexibility (i.e., it does not implement [`black`](https://github.com/psf/black)). By default, the template activates the parts of
`ruff` that incorporate, among other packages: `Flake8`, `Bandit`, `pydocstyle`, and `pylint`.
* [Github Actions](https://github.com/features/actions): If you store your package on Github, which `snickerdoodle` assumes, [there are
strong reasons](https://resources.github.com/devops/tools/automation/actions/)
to prefer Github Actions as your CI/CD tool. `snickerdoodle` includes workflows
for updating, releasing, and publishing your package while also deploying the
accompanying documentation.
* [GitHub Pages](https://pages.github.com/): There is a lot to be said for [Read the Docs](https://readthedocs.com) as a
documentation host site. However, `mkdocs` works better on GitHub Pages and once
you start using GitHub Actions, the automatic updating advantage of Read the
Docs disappears. I also like that GitHub Pages is not dependent on ads placed on
documentation pages for its survival. This was a close call and I might consider
adding a Read the Docs option in a future version of `snickerdoodle`.

## Formatting and Linting

All of the formatting and linting options of the created project are implemented
through `ruff` and are incorporated into the created
project's `pyproject.toml` file. So, you can adjust any [`ruff`
rules](https://beta.ruff.rs/docs/rules/) there. I have included comments in the
`pyproject.toml` file for rules that are excluded and packages that are included
so that you know which rules are enforced. `ruff` is automatically run with
each GitHub push.

!!! Tip

    To automatically fix problems identified by `ruff`, you should use `pre-commit`. A `pre-commit` configuration file (`.pre-commit-config.yaml`) is included in the created repository.  By default, the `pre-commit` command will run `ruff` with the `fix` option invoked, which will try to correct all of the problems that it can. To use `pre-commit`, follow its [user guide](https://pre-commit.com/#usage). If you activate `pre-commit`, it will then be automatically run on every push to GitHub.

## GitHub Actions

These are the available actions for a repository created by `snickerdoodle` that
are located in the ".github" folder and on the GitHub repository page under "Actions":

| GitHub Action | Trigger | Jobs |
| --- | --- | --- |
| `ci` | automatically on push | builds repo, runs tests, lints, formats, builds docs, and deploys docs |
| `publish` | another Action or manually on GitHub | publishes repository on PyPI (must configure PyPI to accept as [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)) |

!!! Tip

    To run an Action (other than `ci.yml`) on GitHub, go to your repository, click
    "Actions" and select one of the Actions listed on the left side of the screen.

## Publishing

`snickerdoodle` tries to make publishing your repository as simple as possible.
Out-of-the-box, it provides tools to publish a release on GitHub and PyPI.

=== "on GitHub"

    To post a release on GitHub, you just need to push a commit with a message that
    begins with the letter "v" followed by the version in [semantic
    form](https://semver.org/) (e.g. "v0.1.2"). That will trigger a job in the
    `ci.yml` Action which automatically publishes a release, using the CHANGELOG.md
    for any changes made since the last release.

=== "on PyPI"

    The best way to publish a release on PyPI is to make the `ci.yml` Action a
    [trusted
    publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/). If you
    do that, you can just run the `publish` GitHub
    Action (which can be activated directly from your GitHub repository's Actions
    page). Otherwise, you should use the [`uv publish`
    command](https://docs.astral.sh/uv/usage/publish/) from the command line
    while in the repository's root folder.

## Repository Layout

[Consistent with best
practices](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/),
`snickerdoodle` uses the "src layout" structure for the created repository. In
the diagram below, the files and folders
that you will ordinarily modify are commented.

```sh
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

## Versioning

At present, `snickerdoodle` does not support automatic semantic
versioning because the tools think so many minor updates are "major" and you
will [find yourself on version
12.0.0](https://hynek.me/articles/semver-will-not-save-you/) and still in alpha
or beta. And, while [calendar versioning](https://calver.org/) has a lot in its favor, it
is alien and confusing to users unfamiliar with it.
