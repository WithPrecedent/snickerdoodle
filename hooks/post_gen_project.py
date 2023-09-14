"""Cookiecutter hook for post project generation."""


import pathlib
import subprocess

_TRUES: tuple[bool | str] = ('y', True, 'true')


def execute_commands(
    commands: tuple(list[str]),
    folder: str | pathlib.Path) -> None:
    """Executes all 'commands' using `subprocess.run`.

    Args:
        commands: tuple of a list of str commands.
        folder: path of repository folder.

    """
    # 'shell' must be set to False to use `subprocess` securely. Do NOT change
    # 'shell' to True.
    kwargs = {"cwd": folder, 'check': True, 'shell': False}
    for command in commands:
        subprocess.run(command, **kwargs)


def create_virtual_environment(folder: str | pathlib.Path) -> None:
    """Creates a virtual environment at '.venv' using `subprocess` and `pdm`.

    Args:
        folder: path of repository folder.
    """
    environment_commands = (
        ['pdm', 'install'],
        ['pdm', 'use', '-f', '.venv'])
    execute_commands(commands = environment_commands, folder = folder)


def commit_to_git_subprocess(url: str, folder: str | pathlib.Path) -> None:
    """Initializes and commits repository using `subprocess`.

    Args:
        url: url for GitHub repository with '.git' extension.
        folder: path of repository folder.

    """
    git_commands = (
        ['git', 'init'],
        ['git', 'add', '.'],
        ['git', 'commit', '-m', 'Initial commit'],
        ['git', 'remote', 'add', 'origin', url],
        ['git', 'push', '-u', 'origin', 'main'])
    execute_commands(commands = git_commands, folder = folder)


def build_and_deploy_docs(folder: str | pathlib.Path) -> None:
    """Builds and deploys docs using `subprocess`, `pdm`, and `mkdocs`.

    Args:
        folder: path of repository folder.

    """
    docs_commands = (
        ['pdm', 'run', 'mkdocs', 'build'],
        ['pdm', 'run', 'mkdocs', 'gh-deploy', '--force', '--clean'])
    execute_commands(commands = docs_commands, folder = folder)


def main() -> None:
    """Executes post repository generation scripts."""
    folder = pathlib.Path.cwd()
    repo_url = '{{ cookiecutter.url }}'
    git_url = ''.join([repo_url, '.git'])
    if "{{ cookiecutter.create_virtual_environment }}".lower() in _TRUES:
        create_virtual_environment(folder = folder)
    if "{{ cookiecutter.commit_to_github }}".lower() in _TRUES:
        commit_to_git_subprocess(url = git_url, folder = folder)
        if "{{ cookiecutter.create_virtual_environment }}".lower() in _TRUES:
            build_and_deploy_docs(folder = folder)
        else:
            print(
                'Cannot deploy documentation without creating a virtual '
                'environment')


if __name__ == "__main__":
    main()
