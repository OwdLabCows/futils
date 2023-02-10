# FabreUtils

This repo is a forked repo from [OwdLabCows/ctutil](https://github.com/OwdLabCows/ctutils).

This tool provides the following functions.

- to delete files belonging to a directory
- to delete files or directories
- to convert objects to pickle or CSV files
- to load pickle, JSON or CSV files and convert them to objects
- to zip a directory

## Installation

You can install this package via `setup.py` after clone this repository.

via `setup.py` (after cloning)

```
python setup.py install
```

## Example

See `example.py`.


# For Developer

## Requirements

This tool sets run on Linux.

You have to install FFmpeg and some Python packages.

## Python packages

You can install some Python packages as follows.

```sh
pip install -r ./requirements.txt
```

## Code convention

This code follows the PEP8 code convention.
You can use `flake8` for checking code convention. `flake8` is included in `requirements.txt`.

## Development environment

Development environment using venv as follows is recomended because of `.gitignore` setting.

```sh
python3 -m venv ./.ctutils_venv
```

