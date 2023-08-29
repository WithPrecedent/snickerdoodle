"""Cookiecutter hook for post project generation."""


# def commit_to_git(url: str) -> None:
#     """Initializes and commits repository to GitHub through shell.

#     Args:
#         url: url for GitHub repository.

#     """
#     import os  # noqa
#     import subprocess # noqa

#     current_folder = os.getcwd()
#     os.chdir(('/'.join([current_folder, '{{cookiecutter.repo_name}}'])))
#     subprocess.call(['git', 'init'])
#     subprocess.call(['git', 'add', '*'])
#     subprocess.call(['git', 'commit', '-m', 'Initial commit'])
#     subprocess.call(['git', 'remote', 'add', 'origin', url, '.git'])
#     subprocess.call(['git', 'push', '-u', 'origin', 'main'])
#     os.chdir(current_folder)

# def main() -> None:
#     """Executes post repository generation scripts."""
#     if {{ cookiecutter.commit_to_github }}:
#         commit_to_git(url = '{{ cookiecutter.url }}')


# if __name__ == "__main__":
#     main()
