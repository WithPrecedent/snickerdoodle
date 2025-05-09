"""Cookiecutter hook for post project generation."""

import json
import pathlib
import subprocess

_TRUES: tuple[bool | str] = ('y', True, 'true')


def execute_commands(
    commands: list[str],
    folder: str | pathlib.Path) -> None:
    """Executes all 'commands' using `subprocess.run`.

    Args:
        commands: tuple of a list of str commands.
        folder: path of repository folder.

    """
    # 'shell' must be set to False to use `subprocess` securely. Do NOT change
    # 'shell' to True.
    for command in commands:
        subprocess.run(  # noqa: S603
            command,
            cwd = folder,
            check = False,
            shell = False)

def execute_command_with_output(command: list[str]) -> str:
    """Returns text output from `command`.

    Args:
        command: command to execute in the form of a list of strings.

    Raises:
        RuntimeError: if the command returns a code below zero.

    Returns:
        The `str` output of the command process.

    """
    # 'shell' must be set to False to use `subprocess` securely. Do NOT change
    # 'shell' to True.
    process = subprocess.run(  # noqa: S603
        command,
        text = True,
        capture_output = True,
        check = True)
    if process.returncode < 0:
        error = f'Execution failed: {process.returncode}"-"{process.stderr}'
        raise RuntimeError(error)
    return process.stdout

def create_virtual_environment(folder: str | pathlib.Path) -> None:
    """Creates a virtual environment at '.venv' using `subprocess`.

    Args:
        folder: path of repository folder.

    """
    environment_commands = (
        ['uv', 'sync'])
    execute_commands(commands = environment_commands, folder = folder)

def get_github_login() -> tuple[str, str]:
    """get_github_login _summary_

    Returns:
        Returns user_name and token for GitHub login

    """
    command = ['echo', 'url=https://github.com', '|', 'git', 'credential', 'fill']
    output = execute_command_with_output(command)
    for line in output.splitlines():
        if "username=" in line:
            user_name = line.split("=")[-1].strip()
        if "password=" in line:
            password = line.split("=")[-1].strip()
            break
    if not password or not user_name:
        print('Could not obtain GitHub username and token from Credential Manager')
    return user_name, password

def commit_to_git(url: str, folder: str | pathlib.Path) -> None:
    """Initializes and commits repository using `subprocess`.

    Args:
        url: url for GitHub repository with '.git' extension.
        folder: path of repository folder.

    """
    name, password = get_github_login()
    repo = "{{ cookiecutter.repo_name }}"
    public = 'public' if "{{ cookiecutter.repo_name }}".lower() in _TRUES else "private"
    git_commands = (
        ['echo', password, '|', 'gh', 'auth', 'login', '--with-token'],
        ['git', 'ls-remote', '-h', url, '&>', '/dev/null'],
        ['git', 'init'],
        # ['git', 'checkout', '-b', 'main'],
        ['git', 'add', '.'],
        ['git', 'commit', '-m', '"Initial commit"'],
        ['git', 'branch', '-M', 'main'],
        ['gh', 'repo', 'create', repo, f'--{public}', '--push', '--source=.'])
        # ['git', 'remote', 'add', 'origin', url],
        # ['git', 'push', '-u', 'origin', 'main'])
    execute_commands(commands = git_commands, folder = folder)

def build_and_deploy_docs(folder: str | pathlib.Path) -> None:
    """Builds and deploys docs using `subprocess` and `mkdocs`.

    Args:
        folder: path of repository folder.

    """
    docs_commands = (
        ['uv', 'run', 'mkdocs', 'build'],
        ['uv', 'run', 'mkdocs', 'gh-deploy', '--force', '--clean'])
    execute_commands(commands = docs_commands, folder = folder)

def reindent_cookiecutter_json():
    """Indent .cookiecutter.json using two spaces.

    The jsonify extension distributed with Cookiecutter uses an indentation
    width of four spaces. This conflicts with the default indentation width of
    Prettier for JSON files. Prettier is run as a pre-commit hook in CI.

    Thanks to cookiecutter-uv-hypermodern-python for this code and suggestion.
    https://github.com/bosd/cookiecutter-uv-hypermodern-python/

    """
    path = pathlib.Path(".cookiecutter.json")

    with path.open() as io:
        data = json.load(io)

    with path.open(mode="w") as io:
        json.dump(data, io, sort_keys= True, indent = 2)
        io.write("\n")

def main() -> None:
    """Executes post repository generation scripts."""
    folder = pathlib.Path.cwd()
    if "{{ cookiecutter.create_virtual_environment }}".lower() in _TRUES:
        create_virtual_environment(folder = folder)
    if "{{ cookiecutter.commit_to_github }}".lower() in _TRUES:
        git_url = ''.join(['{{ cookiecutter.url }}', '.git'])
        commit_to_git(url = git_url, folder = folder)
        if "{{ cookiecutter.create_virtual_environment }}".lower() in _TRUES:
            build_and_deploy_docs(folder = folder)
        else:
            print(
                'Cannot deploy documentation without creating a virtual '
                'environment')
    reindent_cookiecutter_json()

if __name__ == "__main__":
    main()
