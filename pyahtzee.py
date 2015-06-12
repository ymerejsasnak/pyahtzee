from random import randrange


class Die:

    def __init__(self):
        self.value = None
        self.held = False

    def hold(self):
        self.held = not self.held

    def roll(self):
        if not self.held:
            self.value = randrange(6) + 1


class Dice:

    def __init__(self):
        self.dice = [Die(), Die(), Die(), Die(), Die()]

    def hold(self, which):
        self.dice[which].hold()

    def roll(self):
        for d in range(5):
            self.dice[d].roll()

    def get_dice(self):
        values = [self.dice[d].value for d in range(5)]
        holds = ['H' if self.dice[d].held else ' ' for d in range(5)]
        return values, holds


class Game:

    def __init__(self):
        self.dice = Dice()
        self.dice.roll()

    def menu(self):
        choice = ''
        while choice not in ['1', '2', '3', '4', '5', 'R']:
            choice = input('Enter number of dice to hold (1-5) or R to roll: ')

        if choice == 'R':
            self.dice.roll()
        else:
            choice = int(choice)
            self.dice.hold(choice - 1)

    def show_dice(self):
        values, holds = self.dice.get_dice()
        print()
        print('  held:      {}  {}  {}  {}  {}  '.format(*holds))
        print('  values:    {}  {}  {}  {}  {}  '.format(*values))
        print()


g = Game()
while 1:
    g.show_dice()
    g.menu()

#next: more control over flow of game...and SCORING! (good trick? use sets to check for multiples of same value?)
#then after done, add high score file that saves name and score
