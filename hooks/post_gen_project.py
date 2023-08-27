"""Cookiecutter hook for post project generation."""


def commit_to_git(url: str) -> None:
    """Initializes and commits repository to GitHub through shell.

    Args:
        url: url for GitHub repository.

    """
    import subprocess # noqa

    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['git', 'remote', 'add', 'origin', url, '.git'])
    subprocess.call(['git', 'push', '-u', 'origin', 'main'])

def main() -> None:
    """Executes post repository generation scripts."""
    if '{{ cookiecutter.commit_to_github }}'.lower() == 'y':
        commit_to_git(url = '{{ cookiecutter.url }}')


if __name__ == "__main__":
    main()
