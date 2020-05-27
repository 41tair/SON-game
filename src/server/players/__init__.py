class Player:

    def __init__(self, client, room_id):
        self.client = client
        self.room_id = room_id

    def send_msg(self, msg):
        self.client.sendall(msg.encode())

    def route_action(self):
        pass

    def init_cards(self):
        pass

    def show_cards(self):
        pass

    def in_cards(self):
        pass

    def out_cards(self):
        pass

    def put_in_bage(self):
        pass


