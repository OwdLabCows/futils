# CtUtils

This is a toolset for Contexual-Targeting systems or similar systems.
This tool provides the following functions.

- to delete files belonging to a directory
- to convert objects to pickle or CSV files
- to load pickle or CSV files and convert them to objects
- to zip a directory
- to load meta infomation in exel file and convert them to Pandas DataFrame
- convert mp4 to WAV using FFmpeg

# Example

See `example.py`.

# Requirements

This tool sets run on Linux.

You have to install FFmpge and some Python packages.

## FFmpeg

You can see the information of installation on [this site](https://github.com/FFmpeg/FFmpeg/blob/master/INSTALL.md) 

## Python packages

You can install some Python packages as follows.

```sh
pip install -r ./requirements.txt
```

# For Developer

## Code convention

This code follows the PEP8 code convention.
You can use `flake8` for checking code convention. `flake8` is included in `requirements.txt`.

## Development environment

Development environment using venv as follows is recomended because of `.gitignore` setting.

```sh
python3 -m venv ./.ctutils_venv
```

