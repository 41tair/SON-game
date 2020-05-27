import socket
from threading import Thread

s = socket.socket()  # 创建 socket 对象
s.connect(('127.0.0.1', 6666))


def all_time_recv():
    while True:
        msg = s.recv(1024).decode()
        print(msg)


while True:
    thread = Thread(target=all_time_recv, args=())
    thread.setDaemon(True)
    thread.start()
    cmd = input("cmd:")
    if cmd == 'close':
        s.send(cmd.encode('utf8'))
        s.close()
        break
    else:
        s.send(cmd.encode('utf8'))
        print(s.recv(1024).decode(encoding='utf8'))
