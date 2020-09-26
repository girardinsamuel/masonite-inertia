# Contributing Guide

## Introduction

When contributing to this repository, **please first discuss the change you wish to make via issue, email, or any other method with the owners or contributors of this repository** before making a change 😃 . Thank you !

## Getting Started

### Get the code

First you should configure your local environment to be able to make changes in this package.

1. Fork the `https://github.com/girardinsamuel/masonite-inertia` repo.
2. Clone that repo into your computer: `git clone http://github.com/your-username/masonite-inertia.git`.
3. Checkout the current release branch \(example: `master`\).
4. Run `git pull origin master` to get the current release version.

### Install the environment

1. You should create a Python virtual environment with `Python >= 3.6`.
2. Then install the dependencies and setup the project, in root directory with:

```
make init
```

**Note:**

- The package will be locally installed in your venv (with `pip install .`). Meaning that you will be
  able to import it from the project contained in the package as if you installed it from PyPi.
- When making changes to your packages you will need to uninstall the package and reinstall it with
  `pip uninstall masonite-inertia && pip install .`

### Contribute

- From there simply create:
  - a feature branch `feat/my-new-feature`
  - a fix branch `fix/my-new-fix`
- Push to your origin repository:
  - `git push origin feat/my-new-feature`
- Open a pull request (PR) and follow the PR process below

1. You should open an issue before making any pull requests. Not all features will be added to the package and some may be better off as another third party package. It wouldn't be good if you worked on a feature for several days and the pull request gets rejected for reasons that could have been discussed in an issue for several minutes.
2. Ensure any changes are well commented and any configuration files that are added have a flagpole comment on the variables it's setting.
3. Update the README.md if installation/configuration or usage has changed.
4. It's better to add unit tests for the changes you made.
5. The PR must pass Github CI checks. The PR can be merged in once you have a successful review from a maintainer.
6. The version will be bumped by the maintainer when merging, so don't edit package version in the PR.

### Testing

- To add unit tests add tests under `tests/` directory, please read about [Masonite
  testing](https://docs.masoniteproject.com/useful-features/testing) in the official
  documentation

- To test your package locally in a project, a default Masonite project is available
  at root. Just run `python craft serve` and navigate to `localhost:8000/` and
  you will see `Hello Package World` in your browser.

## Dev Guidelines

### Package development

You should read guidelines on package creation in the [Official Documentation](https://docs.masoniteproject.com/advanced/creating-packages)

### Comments

Comments are a vital part of any repository and should be used where needed. It is important not to overcomment something. If you find you need to constantly add comments, you're code may be too complex. Code should be self documenting \(with clearly defined variable and method names\)

#### Types of comments to use

There are 3 main type of comments you should use when developing for Masonite:

**Module Docstrings**

All modules should have a docstring at the top of every module file and should look something like:

```python
""" This is a module to add support for Billing users """
from masonite.request import Request
...
```

**Method and Function Docstrings**

All methods and functions should also contain a docstring with a brief description of what the module does

For example:

```python
def some_function(self):
    """
    This is a function that does x action.
    Then give an exmaple of when to use it
    """
    ... code ...
```

**Code Comments**

If you're code MUST be complex enough that future developers will not understand it, add a `#` comment above it

For normal code this will look something like:

```python
# This code performs a complex task that may not be understood later on
# You can add a second line like this
complex_code = 'value'

perform_some_complex_task()
```

**Flagpole Comments**

Flag pole comments are a fantastic way to give developers an inside to what is really happening and for now should only be reserved for configuration files. A flag pole comment gets its name from how the comment looks

```text
"""
|--------------------------------------------------------------------------
| A Heading of The Setting Being Set
|--------------------------------------------------------------------------
|
| A quick description
|
"""

SETTING = "some value"
```

It's important to note that there should have exactly 75 `-` above and below the header and have a trailing `|` at the bottom of the comment.
