import click
import socket


@click.command()
@click.option("--test", default=1)
def test(test):
    send2client(12345, f"test {test}")


def send2client(port, message: str):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", port))
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(data)


if __name__ == '__main__':
    test()
