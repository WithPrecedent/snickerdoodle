"""Cookiecutter hook for post project generation."""


def main() -> None:
    """Initializes and commits repository to GitHub through shell."""
    if '{{ cookiecutter.commit_to_github }}'.lower() == 'y':
        import subprocess

        subprocess.call(['git', 'init'])
        subprocess.call(['git', 'add', '*'])
        subprocess.call(['git', 'commit', '-m', 'Initial commit'])
        subprocess.call(
            ['git', 'remote', 'add', 'origin', '{{ cookiecutter.url }}', '.git'])
        subprocess.call(['git', 'push', '-u', 'origin', 'main'])
    return


if __name__ == "__main__":
    main()
