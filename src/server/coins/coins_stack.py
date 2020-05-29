class Coins:

    def __init__(self):
        self.coins_stack = []

    def out_coins(self, nums):
        tmp = []
        while nums > 0:
            tmp.append(self.cards_stack.pop())
            nums -= 1
        return tmp

    def in_coins(self):
        pass

    @property
    def show_coins(self):
        return 'all coins'


def generate_coins_stack():
    return Coins()
