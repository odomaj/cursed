from argparse import ArgumentParser, Namespace
from pathlib import Path
from time import sleep
import subprocess


OUTPUT_DIR = "/root/"
PCAP_FILE = "cap.pcap"
TXT_FILE = "text.txt"

PCAP_PATH = f"{OUTPUT_DIR}{PCAP_FILE}"
TXT_PATH = f"{OUTPUT_DIR}{TXT_FILE}"

TIMEOUT_BUFFER = 5


def build(tag: str) -> None:
    subprocess.run(
        [
            "docker",
            "build",
            "-t",
            tag,
            Path(__file__).parent.parent.absolute(),
        ]
    )


def start(tag: str, timeout: str) -> str:
    process: subprocess.Popen = subprocess.Popen(
        [
            "docker",
            "run",
            "--rm",
            "-td",
            "-e",
            f"TIMEOUT={timeout}",
            "-e",
            f"PCAP_PATH={PCAP_PATH}",
            "-e",
            f"TXT_PATH={TXT_PATH}",
            tag,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    # remove endline
    return stdout.decode()[:-1]


def cp_output(container_id: str, dest_dir: str) -> None:
    curr_dir = Path(__file__).parent.parent.joinpath(dest_dir)
    subprocess.run(
        [
            "docker",
            "cp",
            f"{container_id}:{PCAP_PATH}",
            curr_dir.joinpath(PCAP_FILE).absolute(),
        ]
    )
    subprocess.run(
        [
            "docker",
            "cp",
            f"{container_id}:{TXT_FILE}",
            curr_dir.joinpath(TXT_FILE).absolute(),
        ]
    )


def kill_container(container_id: str) -> None:
    subprocess.run(["docker", "stop", container_id])


if __name__ == "__main__":
    arg_parser: ArgumentParser = ArgumentParser()
    arg_parser.add_argument("--tag", "-t", default="cs455-final")
    arg_parser.add_argument("--timeout", "-s", default="90")
    arg_parser.add_argument("--dest", "-d", default="out")
    args: Namespace = arg_parser.parse_args()
    build(args.tag)
    container_id: str = start(args.tag, args.timeout)
    sleep(int(args.timeout) + TIMEOUT_BUFFER)
    cp_output(container_id, args.dest)
    kill_container(container_id)
