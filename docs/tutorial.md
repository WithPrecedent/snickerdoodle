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

As with any `cookiecutter`, project generation requires you to answer several questions. `snickerdoodle` attempts to make this process quick, easy, and painless. The default options, often created from your previous answers, are sensible so that you can just hit "return" in reponse to most questions.

If you use `cookiecutter` a lot (or plan to do so), I suggest [creating a configuration file](https://cookiecutter.readthedocs.io/en/2.3.0/advanced/user_config.html) with some answers to the questionnaire. For example, I have included my configuration file in this repository: [`cc_config.yaml`](https://github.com/WithPrecedent/snickerdoodle/blob/main/cc_config.yaml). You can then use the configuration file (which you should probably put in the parent folder for your coder repositories) when you call `cookiecutter` as follows:

```sh
cookiecutter gh:WithPrecedent/snickerdoodle --config-file cc_config.yaml
```

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
