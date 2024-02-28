# Contributing Guide

## Introduction

When contributing to this repository, **please first discuss the change you wish to make via issue, email, or any other method with the owners or contributors of this repository** before making a change 😃. Thank you !

## Versions

This package aims to support Masonite 4.X versions.

- [master](https://github.com/eaguad1337/masonite-inertia): `>= 4.X.X` for Masonite 4

## Getting Started

### Getting the code

First you should configure your local environment to be able to make changes in this package.

1. Fork the `https://github.com/eaguad1337/masonite-inertia` repo.
2. Clone that repo into your computer: `git clone http://github.com/your-username/masonite-inertia.git`.
3. Run `git pull origin master` to get the latest version.

### Installing the environment

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

### Start contributing

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

### Updating test project template

```
python masonite-package pull --directory tests/integrations
```
