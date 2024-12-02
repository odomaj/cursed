from argparse import ArgumentParser, Namespace
from pathlib import Path
from time import sleep
import subprocess


OUTPUT_DIR = "/root/"
NET_PCAP_FILE = "net_cap.pcap"
LOC_PCAP_FILE = "loc_cap.pcap"
TXT_FILE = "text.txt"
SOL_LOG_FILE = "sol_log.txt"

NET_PCAP_PATH = f"{OUTPUT_DIR}{NET_PCAP_FILE}"
LOC_PCAP_PATH = f"{OUTPUT_DIR}{LOC_PCAP_FILE}"
TXT_PATH = f"{OUTPUT_DIR}{TXT_FILE}"
SOL_LOG_PATH = f"{OUTPUT_DIR}{SOL_LOG_FILE}"

TIMEOUT_BUFFER = 5


def build(tag: str) -> None:
    subprocess.run(
        [
            "docker",
            "build",
            "-t",
            tag,
            Path(__file__).parent.absolute(),
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
            f"NET_PCAP_PATH={NET_PCAP_PATH}",
            "-e",
            f"LOC_PCAP_PATH={LOC_PCAP_PATH}",
            "-e",
            f"TXT_PATH={TXT_PATH}",
            "-e",
            f"SOL_LOG_PATH={SOL_LOG_PATH}",
            tag,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate()
    if not stdout:
        return b""
    # remove endline
    return stdout.decode()[:-1]


def cp_output(container_id: str, dest_dir: str) -> None:
    curr_dir = Path(__file__).parent.joinpath(dest_dir)
    subprocess.run(
        [
            "docker",
            "cp",
            f"{container_id}:{NET_PCAP_PATH}",
            curr_dir.joinpath(NET_PCAP_FILE).absolute(),
        ]
    )
    subprocess.run(
        [
            "docker",
            "cp",
            f"{container_id}:{LOC_PCAP_PATH}",
            curr_dir.joinpath(LOC_PCAP_FILE).absolute(),
        ]
    )
    subprocess.run(
        [
            "docker",
            "cp",
            f"{container_id}:{TXT_PATH}",
            curr_dir.joinpath(TXT_FILE).absolute(),
        ]
    )
    subprocess.run(
        [
            "docker",
            "cp",
            f"{container_id}:{SOL_LOG_PATH}",
            curr_dir.joinpath(SOL_LOG_FILE).absolute(),
        ]
    )


def kill_container(container_id: str) -> None:
    subprocess.run(["docker", "stop", container_id])


if __name__ == "__main__":
    arg_parser: ArgumentParser = ArgumentParser()
    arg_parser.add_argument("--tag", "-t", default="cs455-final")
    arg_parser.add_argument("--timeout", "-s", default="15")
    arg_parser.add_argument("--dest", "-d", default="")
    args: Namespace = arg_parser.parse_args()
    build(args.tag)
    container_id: str = start(args.tag, args.timeout)
    sleep(int(args.timeout) + TIMEOUT_BUFFER)
    cp_output(container_id, args.dest)
    kill_container(container_id)
