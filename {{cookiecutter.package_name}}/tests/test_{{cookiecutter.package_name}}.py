import pytest
import os


def test_main():
    os.system("python -m {{cookiecutter.package_name}}.main")
