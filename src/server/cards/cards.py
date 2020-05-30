from abc import ABCMeta, abstractclassmethod

class BasicCard:
    def __init__(self):
        self.name = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Apple(BasicCard):

    def __init__(self):
        self.name = 'apple'
        self.value = 2
        self.fine = 2
        self.attibute = 'goods'


class Chess(BasicCard):

    def __init__(self):
        self.name = 'chess'
        self.value = 3
        self.fine = 2
        self.attibute = 'goods'


class Bread(BasicCard):

    def __init__(self):
        self.name = 'bread'
        self.value = 3
        self.fine = 2
        self.attibute = 'goods'


class Hen(BasicCard):

    def __init__(self):
        self.name = 'hen'
        self.value = 3
        self.fine = 2
        self.attibute = 'goods'


class Metheglin(BasicCard):

    def __init__(self):
        self.name = 'metheglin'
        self.value = 7
        self.fine = 6
        self.attibute = 'contraband'


class PepperCorn(BasicCard):

    def __init__(self):
        self.name = 'pepper corn'
        self.value = 7
        self.fine = 4
        self.attibute = 'contraband'


class Silk(BasicCard):

    def __init__(self):
        self.name = 'silk'
        self.value = 8
        self.fine = 4
        self.attibute = 'silk'


class Crossbow(BasicCard):

    def __init__(self):
        self.name = 'crossbow'
        self.value = 9
        self.fine = 4
        self.attibute = 'crossbow'


class PepperCorn(BasicCard):

    def __init__(self):
        self.name = 'pepper corn'
        self.value = 3
        self.fine = 2
        self.attibute = 'contraband'


bread = Bread()
hen = Hen()
chess = Chess()
apple = Apple()
metheglin = Metheglin()
crossbow = Crossbow()
peppercorn = PepperCorn()
silk = Silk()


def get_all_cards():
    return [apple]*48+[chess]*36+[bread]*36+[hen]*24+[peppercorn]*22+[metheglin]*21+[silk]*12+[crossbow]*5

if __name__ == "__main__":
    print(get_all_cards())