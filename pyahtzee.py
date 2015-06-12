from random import randrange


class Die:

    def __init__(self):
        self.value = None
        self.hold = False

    def hold(self):
        self.hold = True

    def roll(self):
        if not self.hold:
            self.value = randrange(6) + 1


class Dice:

    def __init__(self):
        self.dice = [Die(), Die(), Die(), Die(), Die()]
        self.score = 0

    def hold(self, which):
        self.dice[which].hold()

    def roll(self):
        for d in range(5):
            self.dice[d].roll()

    def show(self):
        values = tuple([self.dice[d].value for d in range(5)])
        print("  {}  {}  {}  {}  {}  ".format(*values))




