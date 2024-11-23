from pathlib import Path
import socket
import datetime
import sys

LOG_FILE = sys.argv[1]


def init_log() -> None:
    with open(LOG_FILE, "w") as f:
        f.write(f"[LOG GENERATED AT f{datetime.datetime.now()}]\n")


def log(message: str) -> None:
    with open(LOG_FILE, "a") as f:
        f.write(f"{message}\n")


def action5() -> None:
    log("****STARTING ACTION 5****")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(("127.0.0.1", 42001))
        server_socket.listen(1)
    except Exception as e:
        log(f"Caught {e}\n****ENDING ACTION 5 EARLY****")
        try:
            server_socket.close()
        except:
            pass
        return
    client_socket, client_address = server_socket.accept()
    message: str = "Testing Action 5"
    try:
        instructions: str = client_socket.recv(1024).decode()
        log(instructions)
        log(f"sending: {message}")
        client_socket.sendall(message.encode())
        response: str = client_socket.recv(1024).decode()
        log(f"received: {response}")
    except Exception as e:
        log(f"Caught {e}\n****ENDING ACTION 5 EARLY****")
    server_socket.close()


def action6() -> None:
    log("****STARTING ACTION 6****")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect(("0.0.0.0", 1234))
            instructions: str = s.recv(1024).decode()
            log(instructions)
            message: str = "google.com"
            log(f"sending: {message}")
            s.sendall(message.encode())
            response: str = s.recv(1024).decode()
            log(f"received: {response}")
        except Exception as e:
            log(f"Caught {e}\n****ENDING ACTION 6 EARLY****")


if __name__ == "__main__":
    init_log()
    action5()
    action6()
    log(f"[LOG CLOSED AT f{datetime.datetime.now()}]\n")
