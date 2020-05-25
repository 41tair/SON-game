import socket
import argparse
from threading import Thread

from actions import Actions


g_conn_pool = []
g_socket_server = []


def send_msg(client, s):
    client.sendall(s.encode('utf8'))


def init():
    """
    init server
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', default=6666, type=int)
    args = parser.parse_args()

    ADDR = (args.host, args.port)

    global g_socket_server
    g_socket_server = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    g_socket_server.bind(ADDR)
    g_socket_server.listen(5)
    print("Server is ready, waiting to connect...")


def accept_client():
    """
    Receive a new connect
    """
    while True:
        client, _ = g_socket_server.accept()
        # Add to conn pool
        g_conn_pool.append(client)
        # New thread for every client
        thread = Thread(target=message_handle, args=(client,))
        # Set deamon
        thread.setDaemon(True)
        thread.start()


def message_handle(client):
    while True:
        recv_msg = client.recv(1024).decode('utf8')
        try:
            if recv_msg == 'test 1':
                for c in g_conn_pool:
                    send_msg(c, 'this is a log')
            elif recv_msg == 'test 2':
                send_msg(client, '无效')
            elif recv_msg == 'close':
                send_msg(client, 'close the connection')
                client.close()
                g_conn_pool.remove(client)
                break
            else:
                action = Actions()
                msg = action.accept_cmd()
                send_msg(client, msg)
        except Exception as e:
            print(e)
            client.close()
            g_conn_pool.remove(client)
            break


def main():
    init()
    thread = Thread(target=accept_client)
    thread.setDaemon(True)
    thread.start()
    while True:
        cmd = input("""--------------------------
                    输入1:查看当前在线人数
                    输入2:给指定客户端发送消息
                    输入3:关闭服务端
                    """)
        if cmd == '1':
            print("--------------------------")
            print("当前在线人数：", len(g_conn_pool))
        elif cmd == '2':
            print("--------------------------", g_conn_pool)
            index, msg = input("请输入“索引,消息”的形式：").split(",")
            g_conn_pool[int(index)].sendall(msg.encode(encoding='utf8'))
        elif cmd == '3':
            exit()


if __name__ == '__main__':
    main()
