
def send_msg(client, s):
    client.sendall(s.encode('utf8'))