from cards.cards_stack import generate_cards_stack

from players import Player


rooms = {}


class Room:

    __rooms = {}

    def __init__(self, client_num, room_id=None):
        self.__dict__ = self.__rooms
        self.room_id = room_id
        self.client_num = int(client_num)
        self.players_pool = []

    def __str__(self):
        return f'There are {self.__dict__}'

    def add_client(self, client):
        self.players_pool.append(Player(client, self.room_id))
        self.client_num -= 1
        if self.client_num == 0:
            self.begin()

    def init_cards_stack(self):
        self.l_cards_stack, \
            self.m_cards_stack, \
            self.r_cards_stack = generate_cards_stack()

    def begin(self):
        print('game begin')
        self.init_cards_stack()
        for p in self.players_pool:
            p.send_msg('game begin')
            p.init_cards()


def create_room(client_num, room_id):
    rooms[room_id] = Room(client_num, room_id)


def join_room(room_id, client):
    rooms[room_id].add_client(client)
