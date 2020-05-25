from utils import send_msg


rooms = {}


class Room:

    __rooms = {}

    def __init__(self, client_num, room_id=None):
        self.__dict__ = self.__rooms
        self.room_id = room_id
        self.client_num = int(client_num)
        self.clients_pool = []

    def __str__(self):
        return 'There are {self.__dict__}'

    def add_client(self, client):
        self.clients_pool.append(client)
        self.client_num -= 1
        if self.client_num == 0:
            self.begin()

    def begin(self):
        print('game begin')
        for c in self.clients_pool:
            send_msg(c, 'game begin')


def create_room(client_num, room_id):
    rooms[room_id] = Room(client_num, room_id)


def join_room(room_id, client):
    rooms[room_id].add_client(client)
