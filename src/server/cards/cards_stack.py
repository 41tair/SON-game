from random import shuffle


class BasicCardsStack:

    def __init__(self):
        self.cards_stack = []

    def out_cards(self, nums):
        tmp = []
        while nums > 0:
            tmp.append(self.cards_stack.pop())
            nums -= 1
        return tmp

    def in_cards(self):
        pass

    @property
    def show_cards(self):
        return 'all cards'

    def shuffle(self):
        shuffle(self.cards_stack)


class DumpcardsStack(BasicCardsStack):

    def __init__(self):
        pass


class LeftDumpCardsStack(DumpcardsStack):

    def __init__(self):
        pass


class RightDumpCardsStack(DumpcardsStack):

    def __init__(self):
        pass


class MiddleCardsStack(BasicCardsStack):

    def __init__(self):
        pass


def generate_cards_stack():
    middle_cards_stack = MiddleCardsStack()
    left_dump_cards_stack = LeftDumpCardsStack()
    right_dump_cards_stack = RightDumpCardsStack()
    return left_dump_cards_stack, middle_cards_stack, right_dump_cards_stack
