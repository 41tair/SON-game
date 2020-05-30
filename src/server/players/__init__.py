
class Player:

    def __init__(self, client, room_id):
        from rooms import rooms
        self.client = client
        self.room_id = room_id
        self.room = rooms[room_id]
        self.bag = None
        self.is_sheriff = False

    def send_msg(self, msg):
        self.client.sendall(msg.encode())

    def init_player(self):
        self.init_cards()
        self.init_coins()

    def init_cards(self):
        print(f'Room {self.room_id} init cards')
        self.hand_cards = [self.room.m_cards_stack.pop() for _ in range(6)]
        self.send_msg('cards')

    def init_coins(self):
        print(f'Room {self.room_id} init coins')
        self.own_coinds = 50

    def show_cards(self, show_type='hands'):
        if show_type == 'hands':
            self.send_msg(f"hands cards: {self.hand_cards}")
        elif show_type == 'stack':
            self.send_msg(
                f"""left cards statck: {self.room.l_cards_stack},middle cards statck: {self.room.m_cards_stack},rigth cards_stack: {self.room.r_cards_stack}""")

    def in_cards(self, card):
        self.hand_cards.append(card)
        self.show_cards()

    def out_cards(self, card):
        self.hand_cards.remove(card)
        self.show_cards()

    def put_in_bag(self, card):
        self.bag.append(card)
        self.hand_cards.remove(card)
        self.show_cards()

    def declear(self, msg):
        self.room.send_all_players(msg)

    def check(self):
        self.room.send_all_players(self.bag)

    def finish(self):
        self.is_sheriff = False

    def draw_cards(self, left_stack, middle_stack, right_stack):
        for _ in range(int(left_stack))]: self.in_cards(self.room.l_cards_stack.pop())
        for _ in range(int(middle_stack))]: self.in_cards(self.room.m_cards_stack.pop())
        for _ in range(int(right_stack))]: self.in_cards(self.room.r_cards_stack.pop())
        self.show_cards()

    def accept_cmd(self, option):
        cmd = option.cmd
        if cmd == 'draw':
            l, m, r = option.left_stack, option.middle_stack, option.right_stack
            self.draw_cards(left_stack=l, middle_stack=m, right_stack=r)
        elif cmd == 'drop':
            self.out_cards(cards)
        elif cmd == 'show':
            self.show_cards(option.show_type)
        elif cmd == 'give':
            self.out_cards()
            self.room.players_pool[0].in_cards()
        elif cmd == 'declear':
            self.declear()
        elif cmd == 'check':
            self.check()
        elif cmd == 'finish round':
            self.finish()
        else:
            self.send_msg('unusefull msg')
