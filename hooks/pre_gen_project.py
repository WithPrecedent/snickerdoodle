"""Cookiecutter hook for pre project generation."""

from typing import Pattern
import re
import requests


# Package names must be lower-case letters, numbers, or dashes, but not start
# with a dash. The regex is from PEP508:
# https://peps.python.org/pep-0508/#names
# And, without allowing periods or underscores, as reflected in packaging name
# normalization:
# https://peps.python.org/pep-0503/#normalized-names.
VALID_PACKAGE: Pattern[str] = re.compile(
    r'^([a-z0-9]|[a-z0-9][a-z0-9-]*[a-z0-9])$')
# Project names must be letters, numbers, dashes, or spaces, but not start
# with a space or dash.
VALID_PROJECT: Pattern[str] = re.compile(
    r'^([A-Z0-9]|[A-Z0-9][A-Z0-9- ]*[A-Z0-9])$', re.IGNORECASE)
# Repository names must be lower-case letters, numbers, or underscores, but
# not start with an underscore.
VALID_REPO: Pattern[str] = re.compile(
    r'^([a-z0-9]|[a-z0-9][a-z0-9_]*[a-z0-9])$')
# Checks repository url, assuming it is at GitHub.
VALID_REPO_URL: Pattern[str] = re.compile(
    r'[https://github.com|https://www.github.com][/]([a-z0-9]|' \
    r'[a-z0-9][a-z0-9_]*[a-z0-9])[/]([a-z0-9]|[a-z0-9][a-z0-9_]*[a-z0-9])')


def validate_text(text: str, regex: Pattern, error_label: str) -> None:
    """Ensures that `text` is valid.

    Args:
        text: value to check.
        regex: regular expression to check "text" against.
        error_label: text to add to error message if the check fails.

    Raises:
        ValueError: if "text" does not match "regex".

    """
    if regex.fullmatch(text) is None:
        message = f'The project name {text} is not a valid {error_label}'
        raise ValueError(message)


def validate_url_exists(url: str) -> None:
    """Ensures that 'url' exists.

    Args:
        url: repository url to check.

    Raises:
        ConnectionError: if there is an internet connection issue that prevents
            a check as to whether "url" exists.
        ValueError: if "url" does not exist.

    """
    try:
        response = requests.head(
            url,
            allow_redirects = True,
            timeout = (10, 20))
        response.raise_for_status()
    except requests.exceptions.Timeout:
        message = (
            f'{url} could not be validated because there was a problem with'
            f'the internet connection.')
        raise ConnectionError(message) #noqa: W0707
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        message = (
            f'You must first create a repository on GitHub to use the '
            f'"commit_to_github" option. {url} does not currently exist.')
        raise ValueError(message) #noqa: W0707


def main() -> None:
    """Calls validation functions."""
    validate_text(
        text = "{{ cookiecutter.project_name }}",
        regex = VALID_PROJECT,
        error_label = "project name")
    validate_text(
        text = "{{ cookiecutter.package_name }}",
        regex = VALID_PACKAGE,
        error_label = "package name")
    validate_text(
        text = "{{ cookiecutter.repo_name }}",
        regex = VALID_REPO,
        error_label = "repo name")
    validate_text(
        text = "{{ cookiecutter.url }}",
        regex = VALID_REPO_URL,
        error_label = "repository url")
    if {{ cookiecutter.commit_to_github }}:
        validate_url_exists(url = "{{ cookiecutter.url }}")


if __name__ == "__main__":
    main()
