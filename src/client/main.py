
#!/usr/bin/python


'''
SON client
recieve msg from cli, check it and send to server
'''

import socket
import argparse
import threading
import time
from random_name import gen_two_words

BUFFER_SIZE = 1024
CODEC_TYPE = 'utf-8'

class client(object):
    '''
    pass on message between cli and server
    '''

    def __init__(self,
                 name: str,
                 cli_port: int,
                 server_ip: str,
                 server_port: int):

        self.name = name
        self.msg_to_player('hello')

        self.cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cli_socket.bind(('', cli_port))
        self.cli_socket.listen()
        self.cli_msg_handler = threading.Thread(target=self.handle_cli_msg, name='cli_msg_handler')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.settimeout(0.1)
        self.server_socket.connect((server_ip, server_port))
        self.server_broadcast_listener = threading.Thread(target=self.listen_server_broadcast, name='server_msg_handler')

        self.server_port_lock = threading.Lock()

        self.cli_msg_handler.start()
        self.server_broadcast_listener.start()


    def msg_to_player(self, msg: str):
        print(f'{self.name}, {msg}')

    def show_log(self, log: str):
        print(f'client log: {log}')

    def handle_cli_msg(self):
        while True:
            cli_socket1, _ = self.cli_socket.accept()
            cli_msg = cli_socket1.recv(BUFFER_SIZE).decode(CODEC_TYPE)
            print(f'receive {cli_msg}')
            # check
            with self.server_port_lock:
                self.server_socket.sendall(cli_msg.encode(CODEC_TYPE))
                server_msg = self.server_socket.recv(BUFFER_SIZE).decode(CODEC_TYPE)
            cli_socket1.sendall(server_msg.encode(CODEC_TYPE))
            cli_socket1.close()


    def listen_server_broadcast(self):
        while True:
            time.sleep(0.9)
            msg = None
            with self.server_port_lock:
                try:
                    msg = self.server_socket.recv(BUFFER_SIZE).decode(CODEC_TYPE)
                except Exception as e:
                    pass
            if msg: self.show_log(f'receive message from server: {msg}')

    def __del__(self):
        self.server_socket.close()
        self.cli_socket.close()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some arg')
    parser.add_argument("--name", default=gen_two_words(split='_', lowercase=False))
    parser.add_argument("--server-ip", default='127.0.0.1')
    parser.add_argument("--server-port", default=6666, type=int)
    parser.add_argument("--cli-port", default=12345, type=int)
    args = parser.parse_args()

    C = client(
        name=args.name,
        cli_port=args.cli_port,
        server_ip=args.server_ip,
        server_port=args.server_port)

# use telnet to test: "telnet 127.0.0.1 12345"
