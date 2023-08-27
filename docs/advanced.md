# Advanced Usage

## Questionnaire

The questionnaire is derived from the `cookiecutter.json` file, if you wish to implement different questions.

There are couple distinctions between questions worth mentioning:

* "project_name" refers to the title for the project that you would like to appear on the top of the README file and docs. Capital letters, dashes, and spaces are allowed in the "project_name".
* "package_name" means the name used to store the package at [PyPi](https://pypi.org). Dashes (but not capital letters, underscores or spaces) are allowed in the "package_name." The default option will be the "project_name" with any spaces or underscores converted to dashes and all uppercase letters changed to lowercase.
* "repo_name" is the end of the URL for the repository. Underscores (but not capital letters or spaces) are allowed in the "repo_name." The default option will be the "project_name" with any spaces converted to underscores and all uppercase letters changed to lowercase.

So, if you have a "project_name" of "MeowMeow Beans", the "package_name" would be "meowmeow_beans" and the "repo_name" would be "meowmeow-beans." For single word, lowercase packages, there are no differences between the three names. Unless you have a really good reason, you should simply accept the defaults for the "package_name" and "repo_name."

## Core Components

These are the tools that `snickerdoodle` incorporates:

* [`pdm`](https://pdm.fming.dev/latest/): although [Poetry](https://python-poetry.org/) is more popular, its syntax [is not compliant](https://github.com/python-poetry/roadmap/issues/3) with [PEP 621](https://peps.python.org/pep-0621/). I was a long-time `Poetry` user, but eventually ran into some packages and libraries (particularly `mkdocs` extensions) that would not properly install because of `Poetry`'s non-standard `pyproject.toml` formatting. `pdm` is not yet as polished as `Poetry`, but it is rock-solid and I have never run into dependency installation issues with it.
* [`mkdocs`](https://www.mkdocs.org/): similarly, `sphinx` is the dominant documentation package, but it is not nearly as accessible as `mkdocs`, which allows all of your documentation to be created in Markdown and is beautiful out-of-the-box when using the [Material Theme](https://squidfunk.github.io/mkdocs-material/).
* [`ruff`](https://github.com/astral-sh/ruff): a relatively new player in formatting, it aims to serve as a one-stop, extremely fast (it's written in `Rust`) formatting and linting package. `snickerdoodle` implements some reasonable defaults while still allowing user flexibility (e.g., it does not implement [`black`](https://github.com/psf/black) - although you can do that through `ruff`, if you would prefer). By default, the template activates the parts of `ruff` that incorporate, among other packages: `Flake8`, `Bandit`, `pydocstyle`, and `pylint`.
* [Github Actions](https://github.com/features/actions): if you store your package on Github, which `snickerdoodle` assumes, [there are strong reasons](https://resources.github.com/devops/tools/automation/actions/) to prefer Github Actions as your CI/CD tool. `snickerdoodle` includes workflows for updating, releasing, and publishing your package while also deploying the accompanying documentation.
* [GitHub Pages](https://pages.github.com/): There is a lot to be said for [Read the Docs](https://readthedocs.com) as a documentation host site. However, `mkdocs` works better on GitHub Pages and once you start using GitHub Actions, the automatic updating advantage of Read the Docs disappears. I also like that GitHub Pages is not dependent on ads placed on documentation pages for its survival. This was a close call and I might consider adding a Read the Docs option in a future version of `snickerdoodle`.

## Badges

`snickerdoodle` provides a large number of badges. You should feel free to delete any you do not need from the `README.md` file. That will also remove the badges in the front page of your documentation.

By default, the template uses the badge style called "for-the-badge." If you would prefer the standard [Shields.io dynamic badges](https://shields.io) instead of the "for-the-badge" style used in `snickerdoodle`, perform a find and replace in the `readme.md` file to replace "?style=for-the-badge&" with "?" and "?style=for-the-badge" with "". I might make this an option in the `cookiecutter` construction in a future update.

## Versioning

When you publish a new version, you should first manually adjust the version in the created repository's `__init__.py` file. It will then be automatically adjusted in `pyproject.toml` as well. I decided not to use automatic semantic versioning because the process thinks so many minor updates are "major" and you will [find yourself on version 12.0.0](https://hynek.me/articles/semver-will-not-save-you/) and still in alpha or beta. And, while [calendar versioning](https://calver.org/) makes sense, it is alien and confusing to users unfamiliar with it.

## Formatting and Linting

All of the formatting and linting options (of the created project, not the template) are implemented through `ruff` and are incorporated into the created project's `pyproject.toml` file. So, you can adjust any [`ruff` rules](https://beta.ruff.rs/docs/rules/) there. `ruff` is automatically run with each GitHub push. However, that only creates a report of problems with the repository. To automatically fix them, I suggest using `pre-commit`. The created repository has a `pre-commit` command to run `ruff` with the `fix` option invoked.
