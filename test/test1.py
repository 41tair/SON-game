import socket  # 导入 socket 模块
 
s = socket.socket()  # 创建 socket 对象
s.connect(('127.0.0.1', 6666))
while True:
    cmd = input("cmd:")
    if cmd == 'exit':
        s.close()
        break
    else:
        s.send(cmd.encode('utf8'))
        print(s.recv(1024).decode(encoding='utf8'))
