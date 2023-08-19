# Contributing

Contributions are welcome and greatly appreciated!
Every little bit helps, and credit will always be given.
Environment Setup

## Development

Follow this basic process:

1. Fork and clone the repositor.
2. Create a new branch: `git checkout -b feature-or-bugfix-name`.
3. Edit the code.
4. If you added functionality or features, update the documentation accordingly.

If you are unsure about how to fix or ignore a warning, just let the continuous
integration fail, and we will help you during review.

Don't bother updating the changelog, we will take care of this.

## Pull requests guidelines

Link to any related issue in the Pull Request message.

During the review, we recommend using fixups:

```bash
# SHA is the SHA of the commit you want to fix
git commit --fixup=SHA
```

Once all the changes are approved, you can squash your commits:

```bash
git rebase -i --autosquash main
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
