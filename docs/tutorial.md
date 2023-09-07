# Create Repository Tutorial

Follow these steps to ensure there are no problems with the created repository. You can try to mirror these steps using your IDE, but I cannot guarantee you will not run into problems later.

## Create Remote Repository

Go to your GitHub repositories and click "+". Name the new repository that you are creating the same as the "repo_name" you will use in answering the questionnaire. In the repository, change Settings/Actions/General/Workflow Permissions to "Read and Write Permissions." This is necessary for the repository documentation to be properly deployed.

## Create Local Repository

In the parent folder of where you want your new repository, you can use `cookiecutter` to access it directly from GitHub:

```sh
cookiecutter gh:WithPrecedent/snickerdoodle
```

Or, you can clone the repository and then apply the template:

```sh
# Go to folder where your cookiecutter templates are stored locally.
git clone git@github.com:WithPrecedent/snickerdoodle.git
# Go to folder where your code repostiories are stored locally.
cookiecutter snickerdoodle/
```

## Questionnaire

As with any `cookiecutter`, project generation requires you to input information
in what is referred to as the "questionnaire." `snickerdoodle` attempts to make this process quick, easy, and
painless. The default options, often created from your previous answers, are
sensible so that you can just hit "return" in reponse to many requests. Or, if
you prefer, as explained in the [advanced guide](https://withprecedent.github.io/snickerdoodle/advanced/#configuration-file), you can create a configuration
file with many or all of your answers.

These are the variable for which information will be requested, how your answers
will be used, the default value (if any), and
any limitations on your answer:

| Variable | Use | Default | Limitations |
| --- | --- | --- | --- |
| `project_name` | project title on README and docs | None | alphanumeric characters |
| `package_name` | project title on PyPI.org | `project_name` with spaces and underscores changed to dashes | alphanumeric characters with no spaces or underscores |
| `repo_name` | project title on GitHub | `project_name` with spaces and dashes changed to underscores | alphanumeric characters with no spaces or dashes |
| `author_name` | in `pyproject.toml` and docs | None | alphanumeric characters |
| `author_email` | in `pyproject.toml` | None | alphanumeric characters |
| `github_user`  | to infer URL and in `pyproject.toml` | None | alphanumeric characters |
| `description`  | to infer URL and in `pyproject.toml` | None | alphanumeric characters |
| `version` | in `__init__.py` for project | "0.1.0" | any valid version format |
| `url` | in `pyproject.toml` | formed from `github_user` and `repo_name` | any valid GitHub url |
| `license` | content of the constructed LICENSE file and in `pyproject.toml` | Apache Software License 2.0 | numbers 1-6 associated with these licenses: Apache Software License 2.0, BSD License, ISC License, GNU General Public License v3, MIT License, Other |
| `badge_style` | badges in README and docs |  [![for-the-badge style](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge)](https://www.shields.io/) | numbers 1-5 associated with: [![for-the-badge style](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge)](https://www.shields.io/), [![flat style](https://img.shields.io/badge/style-flat-green?style=flat)](https://www.shields.io/), [![flat-square style](https://img.shields.io/badge/style-flat--square-orange?style=flat-square)](https://www.shields.io/), [![plastic style](https://img.shields.io/badge/style-plastic-purple?style=plastic)](https://www.shields.io/), [![social style](https://img.shields.io/badge/style-social-red?style=social)](https://www.shields.io/) |

## Connect Remote and Local Repositories

Enter the folder that you just created (which should be the "repo_name") and initialize git:

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

To create an environment with all of your dependencies (including development dependencies), enter the following in the repository folder.

```sh
pdm install
pdm use -f .venv
```

Any time you update your dependencies, you should rerun `pdm install`. But, you do not need to enter `pdm use`, unless you have a particular need within the environment.

## Deploy Documentation

Unlike `poetry`, `pdm` does not use a shell. Instead, after you have created a virtual environment, enter the following commands to deploy your documentation.

```sh
pdm run mkdocs build
# If you use an IDE that has stored your GitHub credentials, you might find
# it easier to use the IDE for deploying your docs instead of the command
# line.
pdm run mkdocs gh-deploy --force --clean
```

It's essential to run these commands once so that the documentation branch is created. Afterwards, the documentation for the repository will be automatically updated with every push to GitHub.
