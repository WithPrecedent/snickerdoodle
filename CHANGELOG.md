# Changelog

All notable changes to this project will be documented in this file.

<!-- insertion marker -->

## Unreleased

* Added support for Python 3.15 in `snickerdoodle` and the created project (its classifiers and `ci` Action test matrix)

## 0.4.3

* Replaced the deprecated `gh-action-auto-release` Action (Node.js 20 and `set-output`) with the GitHub CLI in the `create_github_release` job of `snickerdoodle` and the created project
* Fixed GitHub releases using the top of CHANGELOG.md instead of the released version's entry as their notes

## 0.4.2

* Made the tests run in `snickerdoodle`'s own `ci` Action on Linux, macOS, and Windows, and made releases wait for them
* Fixed the created project's `ci` Action testing every Python version in its matrix with Python 3.11 (`uv run` recreated the environment from ".python-version")
* Added `cruft` support: the created project skips files that belong to it during `cruft update`, and the post-generation hook no longer creates environments or pushes to GitHub from the temporary copies that `cruft` renders
* Created `uv.lock` when the project is created
* Read the created project's version from `__version__` in `__init__.py` instead of repeating it in `pyproject.toml`
* Used SPDX license expressions (PEP 639) in the created project's `pyproject.toml`
* Added a coverage report page to the created project's documentation when `code_coverage` and `mkdocs` are selected
* Ran the created project's `pre-commit` hooks once instead of in every test job, and only ran its `ci` Action on pushes to `main` and pull requests
* Only created GitHub releases from `main` after the tests and linters pass
* Showed only the README badges for the selected options and fixed broken README links in the created project
* Fixed the created project's CHANGELOG version, CONTRIBUTING setup section, and `.editorconfig` file patterns
* Used GitHub links for the documentation and changelog URLs and left out the PyPI link when `mkdocs` or `pypi` is not selected
* Fixed the `pre-commit` hooks for `snickerdoodle` itself
* Added instructions for updating a created project with `cruft` and for turning on GitHub Pages

## 0.4.1

* Added Codecov uploads to the created project's `ci.yml` (authenticated with OIDC, so no `CODECOV_TOKEN` secret is needed) and a Codecov coverage badge to the created README
* Made the created project's starter test import the package so that its coverage is measured
* Excluded `if __name__ == '__main__':` blocks from coverage in the created project and kept `coverage`'s default exclusions
* Fixed the created project's `dependabot.yml` so that it updates the `uv` dependencies and GitHub Actions in the repository root
* Fixed the misnamed `.python-version` file in the created project and stopped ignoring it
* Fixed missing final newlines and whitespace-only lines in the created project
* Added a "Code Coverage" section to the advanced guide and corrected the questionnaire table, trusted publisher, release commit, and repository layout documentation

## 0.4.0

* Dropped support for Python 3.9 and 3.10 in `snickerdoodle` and Python 3.10 in the created project (Python 3.11 or later is now required)
* Changed the development status of `snickerdoodle` to "Production/Stable"
* Removed `ruff format` from the created project's `pre-commit` hooks to keep spaces around "=" in keyword arguments
* Made `ruff` prefer single quotes and ignore boolean default positional arguments (`FBT002`) in the created project
* Relaxed `pydoclint` checks of type hints, class attributes, and raised exceptions in the created project
* Excluded `uv.lock` from the large file check in the created project
* Added tests that generate projects with each questionnaire option
* Fixed unselected optional files being committed to GitHub before they were removed
* Rejected repository names that start with a number or are Python keywords
* Fixed the `pip install` and PyPI links to use the package name
* Fixed the LICENSE link in the created README and a blank first line in the BSD license

## 0.3.3

* Updated GitHub Actions and fixed bugs in generated templates

## 0.3.2

* Addressed old questions bug

## 0.3.1

* Updated various developmental tools and GitHub Actions

## 0.3.0

* Updated project description

## 0.2.5

* Fixed Node 20 issue

## 0.2.4

* Updated Google Actions
* Failed build due to Node 20 error

## 0.2.3

* Replaced `pdm` with `uv` for dependency management
* Added support for Python 3.13 and 3.14

## 0.2.2

* Fixed mkdocs extension bug in GitHub Actions

## 0.2.1

* Updated badge logos to incorporate changes at Simple Badges

## 0.2.0

* Removed extra actions
* Updated `ruff` options to reflect newer version options
* Fixed `ruff` bug in `ci.yaml` due to newer versions of `ruff`

## 0.1.15

* Fixed issues with publish Action
* Changed required Python version to 3.10 (in preparation for other changes)

## 0.1.14

* Corrected misnumbered previous version

## 0.1.13

* Updated GitHub Actions to newer versions

## 0.1.12

* Removed merge.yml Actions (it was creating a `cookiecutter` error and is not
  used by the package)
* Added Python 3.12 to pyproject.toml

## 0.1.11

* Fixed intermittent bug with mkdocs finding the created module

## 0.1.10

* Added more `ruff` rules and exclusions
* Fixed broken type annotation bug in `post_gen_project`

## 0.1.9

* Streamlined GitHub Actions in the template and created repository
* Updated documentation to incorporate changes to Actions
* Changed extensions in `mkdocs.yml` to better reflect anticipated usage
* Added definition lists and admonitions to the template documentation to better
  convey usage instructions
* Changed "Stability" badge to pull status directly from PyPI

## v0.1.8

* Fixed version detection regex in `release.yml`

## 0.1.7

* Added Action (`release.yml`) to template and create repository which creates a
  new GitHub release
* Updated and reorganized documentation

## 0.1.6

* Added dependabot to both the template and the created repository
* Added option to initialize and commit to GitHub (including building and
  deploying initial documentation to GitPages)
* Added option to create a virtual environment with `pdm`

## 0.1.5

* Changed badge colors to more closely match colors of the associated tool or brand
* Fixed capitalization in badges for consistency with different badge styles and
  associated tool or brand's normal capitalization
* Fixed remaining bugs due to differences in `project_name`, `package_name`, and
  `repo_name` in `cookiecutter` templating

## 0.1.4

* Added documentation for included GitHub Actions
* Fixed bugs in all Actions except `merge.yml`, which is untested
* Streamlined `README.md`

## 0.1.3

* Fixed bug when cookiecutter.project_name has a space in it

## 0.1.2

* Added badges style option to questionnaire
* Added tutorial section regarding the questionnaire
* Reordered badges table
* Minor stylistic and formatting changes

## 0.1.1

* Added pre-commit to template and created repository
* Added manual GitHub Actions
* Added full tutorial user guide to documentation
* Minor stylistic and formatting changes

## 0.1.0

* Initial commit
