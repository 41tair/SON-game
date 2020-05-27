class BasicCardsStack:

    def __init__(self):
        pass

    def cards_out(self):
        pass

    def cards_in(self):
        pass

    @property
    def show_cards(self):
        return 'all cards'


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
