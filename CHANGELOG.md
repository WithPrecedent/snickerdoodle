# Changelog

All notable changes to this project will be documented in this file.

<!-- insertion marker -->

## 0.1.13

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
