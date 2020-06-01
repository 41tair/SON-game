
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

    def init_player(self, player_id):
        self.player_id = player_id
        self.init_cards()
        self.init_coins()

        self.show()
        self.show(show_type='coins')
        self.show(show_type='id')

    def init_cards(self):
        print(f'Room {self.room_id} init cards')
        self.hand_cards = [self.room.m_cards_stack.pop() for _ in range(6)]
        self.send_msg('cards')

    def init_coins(self):
        print(f'Room {self.room_id} init coins')
        self.coins = 50

    def show(self, show_type='hands'):
        if show_type == 'hands':
            self.send_msg(f"hands cards: {self.hand_cards}")
        elif show_type == 'stack':
            self.send_msg(
                f"""left cards statck: {self.room.l_cards_stack},
                middle cards statck: {self.room.m_cards_stack},
                rigth cards_stack: {self.room.r_cards_stack}""")
        elif show_type == 'coins':
            self.send_msg(f"your coins {self.coins}")
        elif show_type == 'id':
            self.send_msg(f"your id {self.player_id}")

    def in_cards(self, card):
        self.hand_cards.append(card)

    def out_cards(self, card_num):
        card = self.hand_cards.pop(int(card_num))
        self.show_cards()
        return card

    def put_in_bag(self, card_num):
        self.bag.append(self.hand_cards[card_num])
        self.hand_cards.pop(card_num)
        self.show_cards()

    def declear(self, msg):
        self.room.send_all_players(msg)

    def check(self):
        self.room.send_all_players(self.bag)

    def finish(self):
        self.is_sheriff = False

    def draw_cards(self, left_stack, middle_stack, right_stack):
        for _ in range(int(left_stack)):
            self.in_cards(self.room.l_cards_stack.pop())
        for _ in range(int(middle_stack)):
            self.in_cards(self.room.m_cards_stack.pop())
        for _ in range(int(right_stack)):
            self.in_cards(self.room.r_cards_stack.pop())
        self.show_cards()

    def give(self, player_num, card_num):
        card = self.out_cards(card_num)
        self.room.players_pool[player_num].in_cards(card)
        self.show_cards()
        self.room.players_pool[player_num].show_cards()

    def accept_cmd(self, option):
        cmd = option.cmd
        if cmd == 'draw':
            l, m, r = option.left_stack, \
                option.middle_stack, \
                option.right_stack
            self.draw_cards(left_stack=l, middle_stack=m, right_stack=r)
        elif cmd == 'drop':
            card_num = option.card_num
            print(card_num)
            self.out_cards(card_num)
        elif cmd == 'show':
            self.show(option.show_type)
        elif cmd == 'give':
            card_num = option.card_num
            player_num = option.player_num
            self.give(player_num, card_num)
        elif cmd == 'declear':
            msg = option.msg
            self.declear(msg)
        elif cmd == 'check':
            self.check()
        elif cmd == 'finish round':
            self.finish()
        else:
            self.send_msg('unusefull msg')
