from argparse import ArgumentParser
from pathlib import Path
from subprocess import run

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--tag", "-t", default="cs455-final")
    args = arg_parser.parse_args()
    run(
        [
            "docker",
            "build",
            "-t",
            args.tag,
            Path(__file__).parent.parent.absolute(),
        ]
    )
