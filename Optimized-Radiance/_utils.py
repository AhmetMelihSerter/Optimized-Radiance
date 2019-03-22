"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2017-2018 RedFantom
"""
import contextlib
import os

platforms = {
    "win32": "win",
    "linux2": "linux"
}


@contextlib.contextmanager
def temporary_chdir(new_dir):
    old_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(old_dir)


def get_file_directory():
    """Return an absolute path to the current file directory"""
    return os.path.dirname(os.path.realpath(__file__))

