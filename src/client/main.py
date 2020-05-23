'''
SON client
recieve msg from cli, check it and send to server
'''

#!/usr/bin/env python3

import socket
import argparse
from random_name import gen_two_words

BUFFER_SIZE = 1024

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process some arg')
    parser.add_argument("--name", default=gen_two_words(split='_', lowercase=False))
    parser.add_argument("--server-ip")
    parser.add_argument("--server-port", type=int)
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener, socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender:

        listener.bind(('', 12345))
        listener.listen()
        print("listining, waitting for cli...")

        sender.connect((args.server_ip, args.server_port))
        print("connect to server.")

        while True:
            print("\n")
            listener_1, addr = listener.accept()
            print("cli is in.")
            with listener_1:
                data_in_string = listener_1.recv(BUFFER_SIZE).decode('utf-8')
                if data_in_string:
                    print(f"client receive {data_in_string}.")
                    if data_in_string == "exit":
                        sender.sendall(b"{args.name} {data_in_string} from cli.")
                        print(f"client exit.")
                        break
                    # check something
                    sender.sendall(b"{args.name} {data_in_string}")
                    print(f"client sent {args.name} {data_in_string} to server.")
                    sender_receive = sender.recv(BUFFER_SIZE)
                    print(f"client receive {sender_receive.decode('utf-8')} frome server.")
                    # do something
                    listener_1.sendall(sender_receive)
                    print(f"client sent {sender_receive.decode('utf-8')} to cli.")


# use telnet to test: "telnet 127.0.0.1 12345"
