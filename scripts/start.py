from argparse import ArgumentParser
import subprocess

if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--tag", "-t", default="cs455-final")
    args = arg_parser.parse_args()
    subprocess.run(["docker", "run", "--rm", "-it", args.tag])
