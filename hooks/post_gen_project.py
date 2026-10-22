"""Cookiecutter hook for post project generation."""

import os
import pathlib
import shutil
import subprocess
import tempfile

_TRUES: tuple[bool | str, ...] = ('y', 'Y', True, 'true', 'True')
_PATHS_TO_REMOVE: list[str] = [
    '{% if cookiecutter.github_actions not in ("y", "Y", True, "true", "True") %}.github/workflows{% endif %}',
    '{% if cookiecutter.dependabot not in ("y", "Y", True, "true", "True") %}.github/dependabot.yml{% endif %}',
    '{% if cookiecutter.pre_commit not in ("y", "Y", True, "true", "True") %}.pre-commit-config.yaml{% endif %}',
    '{% if cookiecutter.mkdocs not in ("y", "Y", True, "true", "True") %}docs{% endif %}',
    '{% if cookiecutter.mkdocs not in ("y", "Y", True, "true", "True") %}mkdocs.yml{% endif %}',
    '{% if cookiecutter.pypi not in ("y", "Y", True, "true", "True") %}.github/workflows/publish.yml{% endif %}',
    '{% if cookiecutter.code_coverage not in ("y", "Y", True, "true", "True") %}codecov.yml{% endif %}',
    '{% if cookiecutter.code_coverage not in ("y", "Y", True, "true", "True") %}.github/workflows/validate_codecov.yml{% endif %}']

os.environ['DISABLE_MKDOCS_2_WARNING'] = 'true'

def delete_file(path: str | pathlib.Path) -> None:
    """Deletes file from disk.

    Args:
        path: path to file.

    """
    path = pathlib.Path(path) if isinstance(path, str) else path
    path.unlink(missing_ok = True)
    return

def delete_folder(path: str | pathlib.Path) -> None:
    """Deletes folder from disk.

    Args:
        path: path to folder.

    """
    shutil.rmtree(path, ignore_errors = True)
    return

def delete_path(path: str | pathlib.Path) -> None:
    """Deletes path to file or folder.

    Args:
        path: path to folder or file to delete.

    """
    path = pathlib.Path(path) if isinstance(path, str) else path
    if path.is_dir():
        delete_folder(path)
    else:
        delete_file(path)
    return

def execute_commands(
    commands: list[list[str]],
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
    return

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
    environment_commands = [['uv', 'sync']]
    execute_commands(commands = environment_commands, folder = folder)
    return

def lock_dependencies(folder: str | pathlib.Path) -> None:
    """Creates 'uv.lock' using `subprocess` so that installs are reproducible.

    Setting the 'SNICKERDOODLE_SKIP_LOCK' environment variable skips this step,
    which keeps the `snickerdoodle` tests from resolving dependencies for every
    project that they create.

    Args:
        folder: path of repository folder.

    """
    if os.environ.get('SNICKERDOODLE_SKIP_LOCK'):
        return
    if shutil.which('uv') is None:
        print(  # noqa: T201
            'Cannot create uv.lock because uv is not installed. Run "uv lock" '
            'after installing uv.')
    else:
        execute_commands(commands = [['uv', 'lock']], folder = folder)
    return

def is_cruft_render(folder: str | pathlib.Path) -> bool:
    """Returns whether `cruft` is rendering the template to compare it.

    `cruft update`, `cruft check`, and `cruft diff` render the template into a
    new temporary folder (such as '/tmp/tmpabc123/project') and run this hook
    there. `cruft` adds the '_commit' key to the context, which a normal
    `cookiecutter` run does not have. `cruft create` also adds '_commit', but
    it renders into the folder chosen by the user.

    Args:
        folder: path of repository folder.

    Returns:
        Whether `folder` is a temporary copy rendered by `cruft`.

    """
    if "{{ cookiecutter.get('_commit', '') }}" == '':
        return False
    temp = pathlib.Path(tempfile.gettempdir()).resolve()
    parent = pathlib.Path(folder).resolve().parent
    return parent.parent == temp and parent.name.startswith('tmp')

def commit_to_git(url: str, folder: str | pathlib.Path) -> None:
    """Initializes and commits repository.

    Args:
        url: url for GitHub repository with '.git' extension.
        folder: path of repository folder.

    """
    git_commands = [
        ['git', 'init', '-b', 'main'],
        ['git', 'add', '.'],
        ['git', 'commit', '-m', 'Initial commit'],
        ['git', 'remote', 'add', 'origin', url],
        ['git', 'push', '--set-upstream', 'origin', 'main']]
    execute_commands(commands = git_commands, folder = folder)

def build_and_deploy_docs(folder: str | pathlib.Path) -> None:
    """Builds and deploys docs using `subprocess` and `mkdocs`.

    Args:
        folder: path of repository folder.

    """
    docs_commands = [
        ['uv', 'run', 'mkdocs', 'build'],
        ['uv', 'run', 'mkdocs', 'gh-deploy', '--force', '--clean']]
    execute_commands(commands = docs_commands, folder = folder)

def cleanup_files() -> None:
    """Deletes files and paths for unselected options."""
    for path in _PATHS_TO_REMOVE:
        if path != '':
            delete_path(path)
    return

# def reindent_cookiecutter_json():
#     """Indent .cookiecutter.json using two spaces.

#     The jsonify extension distributed with Cookiecutter uses an indentation
#     width of four spaces. This conflicts with the default indentation width of
#     Prettier for JSON files. Prettier is run as a pre-commit hook in CI.

#     Thanks to cookiecutter-uv-hypermodern-python for this code and suggestion.
#     https://github.com/bosd/cookiecutter-uv-hypermodern-python/

#     """
#     path = pathlib.Path('cookiecutter.json')

#     with path.open() as io:
#         data = json.load(io)

#     with path.open(mode = 'w') as io:
#         json.dump(data, io, sort_keys= True, indent = 2)
#         io.write('\n')

def main() -> None:
    """Executes post repository generation scripts."""
    folder = pathlib.Path.cwd()
    # Files for unselected options are removed first so that they are not
    # committed to GitHub.
    cleanup_files()
    # A copy rendered by `cruft` is only compared with the project and then
    # deleted, so it should not create environments or push to GitHub.
    if is_cruft_render(folder = folder):
        return
    # `uv sync` also creates 'uv.lock'.
    if "{{ cookiecutter.virtual_environment }}".lower() in _TRUES:
        create_virtual_environment(folder = folder)
    else:
        lock_dependencies(folder = folder)
    if "{{ cookiecutter.commit_to_github }}".lower() in _TRUES:
        git_url = ''.join(['{{ cookiecutter.url }}', '.git'])
        commit_to_git(url = git_url, folder = folder)
        if "{{ cookiecutter.mkdocs }}".lower() in _TRUES:
            if "{{ cookiecutter.virtual_environment }}".lower() in _TRUES:
                build_and_deploy_docs(folder = folder)
            else:
                print(  # noqa: T201
                    'Cannot deploy documentation without creating a virtual '
                    'environment')
    # reindent_cookiecutter_json()

if __name__ == "__main__":
    main()
