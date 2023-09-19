# Tutorial

## Requirements

To use `snickerdoodle` and the repository that it creates, you just need:

* [`python`](https://www.python.org/) 3.8 or later
* [`git`](https://git-scm.com/)
* [`cookiecutter`](https://www.cookiecutter.io/),
  [`cruft`](https://github.com/cruft/cruft), or
  [`cookieninja`](https://github.com/cookieninja-generator/cookieninja)
* [`pdm`](https://pdm.fming.dev/latest/)
* A [GitHub](https://github.com/) account

!!! tip
    To take advantage of the automatic initial commit to GitHub, you should also
    [store your Git credentials](https://docs.github.com/en/get-started/quickstart/set-up-git) on your computer.

## Create Remote Repository

Go to your GitHub Repositories page and click "+". The name of the new
repository must be the same as the "repo_name" you will use in answering the `cookiecutter`
questionnaire.

## Create Local Repository

In the parent folder of where you want your new repository, you can use `cookiecutter` (or
[`cruft`](https://github.com/cruft/cruft) or
[`cookieninja`](https://github.com/cookieninja-generator/cookieninja)) to access
the `snickerdoodle` template either directly from GitHub or by cloning it on your computer.

=== "from GitHub"

    ```sh
    cookiecutter gh:WithPrecedent/snickerdoodle
    ```

=== "from local source"

    ```sh
    # Go to folder where your cookiecutter templates are stored locally.
    git clone git@github.com:WithPrecedent/snickerdoodle.git
    # Go to folder where your code repostiories are stored locally.
    cookiecutter snickerdoodle
    ```

## Answer Questionnaire

As with any `cookiecutter`, project generation requires you to input information
in what is referred to as the "questionnaire." `snickerdoodle` attempts to make this process quick, easy, and
painless. The default options, often created from your previous answers, are
sensible so that you can just hit "return" in reponse to many requests. Or, if
you prefer, as explained in the [advanced guide](https://withprecedent.github.io/snickerdoodle/advanced/#configuration-file), you can create a configuration
file with many or all of your answers.

These are the variable for which information will be requested, how your answers
will be used, the default value (if any), and
any limitations on your answer:

| <div style="width:100px">Variable</div> | Use | Default | Limitations |
| --- | --- | --- | --- |
| `project_name` | project title on README and docs | None | alphanumeric |
| `package_name` | project title on PyPI.org | `project_name` with spaces and underscores changed to dashes | alphanumeric with no spaces or underscores |
| `repo_name` | project title on GitHub | `project_name` with spaces and dashes changed to underscores | alphanumeric with no spaces or dashes |
| `author_name` | in `pyproject.toml` and docs | None | alphanumeric |
| `author_email` | in `pyproject.toml` | None | alphanumeric |
| `github_user`  | to infer URL and in `pyproject.toml` | None | alphanumeric |
| `description`  | to infer URL and in `pyproject.toml` | None | alphanumeric |
| `version` | in `__init__.py` for project | "0.1.0" | any valid version format |
| `url` | in `pyproject.toml` | formed from `github_user` and `repo_name` | any valid GitHub url |
| `license` | content of the constructed LICENSE file and in `pyproject.toml` | Apache 2.0 | Apache 2.0, BSD, ISC, GNU General Public v3, MIT, Other |
| `badge_style` | badges in README and docs |  [![for-the-badge style](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge)](https://www.shields.io/) | [![for-the-badge style](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge)](https://www.shields.io/), [![flat style](https://img.shields.io/badge/style-flat-green?style=flat)](https://www.shields.io/), [![flat-square style](https://img.shields.io/badge/style-flat--square-orange?style=flat-square)](https://www.shields.io/), [![plastic style](https://img.shields.io/badge/style-plastic-purple?style=plastic)](https://www.shields.io/), [![social style](https://img.shields.io/badge/style-social-red?style=social)](https://www.shields.io/) |
| `commit_to_github` | whether to make an initial commit to GitHub | "n" (no commit) | Must have [GitHub credentials stored](https://docs.github.com/en/get-started/quickstart/set-up-git) |
| `create_virtual_environment` | whether to create a virtual environment in ".venv" folder | "n" (no environment created) | Must have `pdm` installed |

## Connect Remote and Local Repositories

!!! Warning

    *You do not need to complete this step if you opted to `commit_to_github` in the
    questionnaire.*

Enter the folder that you just created (which should be the `repo_name`) and
initialize git as followa:

```sh
# If your shell does not use "cd" to change directory, substitute the
# appropriate command.
cd {repo_name}
git init
git add .
# You can change the message in the last command to whatever you like
git commit -m  "Initial commit"
git remote add origin {url of your new repository}.git
# Depending on your default branch name, the last parameter might be "master"
# or whatever you have set it to. If you use an IDE that has stored your
# GitHub credentials, you might find it easier to use the IDE for pushing your
# repository instead of the command line.
git push -u origin main
```

Your first commit with the new repository should now be visible on GitHub.

## Create Virtual Environment

!!! Warning

    *You do not need to complete this step if you opted to `create_virtual_environment` in the
    questionnaire.*

To create an environment with all of your dependencies (including development dependencies), enter the following in the repository folder.

```sh
pdm install
pdm use -f .venv
```

Any time you update your dependencies, you should rerun `pdm install`. But, you do not need to enter `pdm use`, unless you have a particular need within the environment.

## Deploy Documentation

!!! Warning

    *You do not need to complete this step if you opted to `commit_to_github` and
    `create_virtual_environment` in the
    questionnaire.*

Unlike `poetry`, `pdm` does not use a shell. Instead, after you have created a virtual environment, enter the following commands to deploy your documentation.

```sh
pdm run mkdocs build
# If you use an IDE that has stored your GitHub credentials, you might find
# it easier to use the IDE for deploying your docs instead of the command
# line.
pdm run mkdocs gh-deploy --force --clean
```

It's essential to run these commands once so that the documentation branch is created. Afterwards, the documentation for the repository will be automatically updated with every push to GitHub.
