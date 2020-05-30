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
        player = Player(client, self.room_id)
        self.players_pool.append(player)
        self.client_num -= 1
        if self.client_num == 0:
            self.begin()
        return player

    def init_cards_stack(self):
        self.l_cards_stack, \
            self.m_cards_stack, \
            self.r_cards_stack = generate_cards_stack()

    def begin(self):
        print('game begin')
        self.init_cards_stack()
        for p in self.players_pool:
            p.init_player()
            p.send_msg('game begin')

    def send_all_players(self, msg):
        for p in self.players_pool:
            p.send_msg(msg)


def create_room(client_num, room_id):
    room = Room(client_num, room_id)
    rooms[room_id] = room
    return room


def join_room(room_id, client):
    player = rooms[room_id].add_client(client)
    return player

def get_room_id():
    return len(rooms)+1
