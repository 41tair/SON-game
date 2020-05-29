from rooms import rooms


class Player:

    def __init__(self, client, room_id):
        self.client = client
        self.room_id = room_id
        self.room = rooms[room_id]

    def send_msg(self, msg):
        self.client.sendall(msg.encode())

    def init_cards(self):
        self.send_msg('cards')
        self.hand_cards = self.room.m_cards_stack.out_cards()

    def init_coins(self):
        

    def show_cards(self):
        self.client.send_msg(f"{[_ for _ in self.hand_cards]}")

    def in_cards(self):
        self.hand_cards.append('to add')
        self.show_cards()

    def out_cards(self):
        self.hand_cards.pop()
        self.show_cards()

    def put_in_bage(self):
        self.hand_cards.pop()
        self.hand_cards()

    def accept_cmd(self, *args):
        cmd = args[0]
        if cmd == 'draw':
            self.in_cards()

