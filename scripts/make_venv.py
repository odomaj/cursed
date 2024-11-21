"""makes a virtual environment venv in the root directory of the repo
and installs all dependencies in the requirements.txt file at the root
directory of the repo"""

import subprocess
import sys
from pathlib import Path


def make_venv() -> None:
    """builds a virtual environment in the root directory of the repo named
    venv"""
    subprocess.run(
        [
            "python",
            "-m",
            "venv",
            Path(__file__).parent.parent.joinpath("venv").absolute(),
        ]
    )


def clean_venv() -> None:
    """cleans the virtual environment in the root directory of the repo named
    venv"""
    subprocess.run(
        [
            Path(__file__)
            .parent.parent.joinpath("venv/Scripts/python")
            .absolute(),
            "-m",
            "pip",
            "freeze",
            "|",
            "xargs",
            "pip",
            "uninstall",
            "-y",
        ]
    )


def install_packages() -> None:
    """uses pip to install all of the dependencies specified in the
    requirements.txt of the root directory in the virtual environment venv"""
    subprocess.run(
        [
            Path(__file__)
            .parent.parent.joinpath("venv/Scripts/python")
            .absolute(),
            "-m",
            "pip",
            "--timeout",
            "1000",
            "install",
            "-r",
            Path(__file__)
            .parent.parent.joinpath("requirements.txt")
            .absolute(),
        ]
    )


def update_pip() -> None:
    """updates pip in the virtual environment in the root directory of the
    repo named venv"""
    subprocess.run(
        [
            Path(__file__)
            .parent.parent.joinpath("venv/Scripts/python")
            .absolute(),
            "-m",
            "pip",
            "install",
            "--upgrade",
            "pip",
        ]
    )


if __name__ == "__main__":
    if (
        sys.version_info[0] != 3
        or sys.version_info[1] != 10
        or sys.version_info[2] != 12
    ):
        print("[WARNING] python 3.10.12 is recommended")

    # check if the current running version of python is sourced from venv
    if (
        Path(sys.executable).parent.parent.parent.absolute()
        == Path(__file__).parent.parent.absolute()
    ):
        update_pip()
        clean_venv()
        install_packages()
    else:
        make_venv()
        update_pip()
        install_packages()
