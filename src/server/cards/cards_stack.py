from random import shuffle

from cards import get_all_cards


class CardsStack(list):

    def __init__(self):
        self.cards_stack = get_all_cards().copy()
        self.shuffle()

    def out_cards(self, nums):
        tmp = []
        while nums > 0:
            tmp.append(self.cards_stack.pop())
            nums -= 1
        return tmp

    def in_cards(self):
        pass

    def show_cards(self):
        return 'all cards'

    def shuffle(self):
        self.cards_stack = shuffle(self.cards_stack)


def generate_cards_stack():
    middle_cards_stack = get_all_cards().copy()
    shuffle(middle_cards_stack)
    left_dump_cards_stack = [middle_cards_stack.pop() for _ in range(5)]
    right_dump_cards_stack = [middle_cards_stack.pop() for _ in range(5)]
    return left_dump_cards_stack, middle_cards_stack, right_dump_cards_stack


if __name__ == "__main__":
    l, m, r = generate_cards_stack()
    print(m)
