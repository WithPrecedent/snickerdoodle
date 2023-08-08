# Contributing

Contributions are welcome and greatly appreciated!
Every little bit helps, and credit will always be given.

## Environment Setup

Fork and clone the repository, then:

## Development

This project uses the *src layout*, which means that the package code is located
at `./src/{{cookiecutter.repo_name}}`. It uses `MkDocs` for documentation with 
extensions that will automatically add any docstrings to the API documentation.
At a minimum, you should make sure the existing documentation is consistent with
any changes you make.

Follow this basic process:

1. Create a new branch: `git checkout -b feature-or-bugfix-name`.
2. Edit the code.
3. If you added functionality or features, update the documentation accordingly.

**Before committing:**

1. run `make format` to auto-format the code
1. run `make check` to check everything (fix any warning)
1. run `make test` to run the tests (fix any issue)
1. if you updated the documentation or the project dependencies:
    1. run `make docs`
    1. go to http://localhost:8000 and check that everything looks good
1. follow our [commit message convention](#commit-message-convention)

If you are unsure about how to fix or ignore a warning, just let the continuous 
integration fail, and we will help you during review.

Don't bother updating the changelog, we will take care of this.

## Commit message convention

Commit messages must follow our convention based on the
[Angular style](https://gist.github.com/stephenparish/9941e89d80e2bc58a153#format-of-the-commit-message)
or the [Karma convention](https://karma-runner.github.io/4.0/dev/git-commit-msg.html):

```md
<type>[(scope)]: Subject

[Body]
```

**Subject and body must be valid Markdown.**
Subject must have proper casing (uppercase for first letter
if it makes sense), but no dot at the end, and no punctuation
in general.

Scope and body are optional. Type can be:

- `build`: About packaging, building wheels, etc.
- `chore`: About packaging or repo/files management.
- `ci`: About Continuous Integration.
- `deps`: Dependencies update.
- `docs`: About documentation.
- `feat`: New feature.
- `fix`: Bug fix.
- `perf`: About performance.
- `refactor`: Changes that are not features or bug fixes.
- `style`: A change in code style/format.
- `tests`: About tests.

If you write a body, please add trailers at the end
(for example issues and PR references, or co-authors),
without relying on GitHub's flavored Markdown:

```md
Body.

Issue #10: https://github.com/namespace/project/issues/10
Related to PR namespace/other-project#15: https://github.com/namespace/other-project/pull/15
```

These "trailers" must appear at the end of the body,
without any blank lines between them. The trailer title
can contain any character except colons `:`.
We expect a full URI for each trailer, not just GitHub autolinks
(for example, full GitHub URLs for commits and issues,
not the hash or the #issue-number).

We do not enforce a line length on commit messages summary and body,
but please avoid very long summaries, and very long lines in the body,
unless they are part of code blocks that must not be wrapped.

## Pull requests guidelines

Link to any related issue in the Pull Request message.

During the review, we recommend using fixups:

```bash
# SHA is the SHA of the commit you want to fix
git commit --fixup=SHA
```

Once all the changes are approved, you can squash your commits:

```bash
git rebase -i --autosquash master
```

And force-push:

```bash
git push -f
```

If this seems all too complicated, you can push or force-push each new commit,
and we will squash them ourselves if needed, before merging.

## Style Guidelines

This package follows the [Google
Python Style Guide](https://google.github.io/styleguide/pyguide.html) with two
notable exceptions:

1. It always adds spaces around "=". This not only violates the Google guide, it violates [PEP8](https://peps.python.org/pep-0008/), the foundational Python style guide from which all other resources are derived. I defy this strong, long-standign norm because I find it more readable. My brain and eyes have trouble seeing two separate objects when an equal sign is in the middle. I imagine that I am not alone in this accessibility issue. Further, as PEP8 itself notes, required spaces around equal signs are becoming increasing common with type annotations becoming part of best practices (and, as a result, signatures to classes, functions, and methods regularly include spaces around the equal signs). I realize that this will seem alien to many coders, but it is far easier on my eyes.
2. I use some so-called "power features", primarily dunder methods, to make my interfaces easier to access and use. This is disfavored in the Google Python Style Guide because such code is often more difficult for others to read. To address that concern, I try to document and comment as to what the code is doing whenever I used any of the "power features" of Python.
