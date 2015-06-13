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

    def reset_holds(self):
        for d in range(5):
            self.dice[d].held = False

    def roll(self):
        for d in range(5):
            self.dice[d].roll()

    def get_dice(self):
        values = [self.dice[d].value for d in range(5)]
        holds = ['H' if self.dice[d].held else ' ' for d in range(5)]
        return values, holds

    def get_scores(self):

        scores = [0] * 13  # fill with 0s to start
        values = self.get_dice()[0]
        unique = set(values)  # for testing for full house
        #for testing large straights
        #uses list/set to remove dupes for sm straight testing
        sorted_values = sorted(list(set(values)))  
        #turns sorted into string to search for sm straight
        sorted_string = ''.join(map(str, sorted_values))  


        #loop through the 6 numbered scores
        for s in range(6):
            scores[s] = values.count(s + 1) * (s + 1)

        #3 of a kind
        if values.count(values[0]) >= 3 or values.count(values[1]) >= 3 or values.count(values[2]) >= 3:
            scores[6] = sum(values)
        #4 of a kind
        if values.count(values[0]) >= 4 or values.count(values[1]) >= 4:
            scores[7] = sum(values)
        #full house (25)
        if len(unique) == 2 and values.count(unique.pop()) >= 2 and values.count(unique.pop()) >= 2:
            scores[8] = 25
        #small straight
        if '1234' in sorted_string or '2345' in sorted_string or '3456' in sorted_string:
            scores[9] = 30
        #large straight
        if sorted_values == [1, 2, 3, 4, 5] or sorted_values == [2, 3, 4, 5, 6]:
            scores[10] = 40
        #yahtzee
        if values.count(values[0]) == 5:
            scores[11] = 50
        #chance
        scores[12] = sum(values)

        return scores


class Game:

    def __init__(self):
        self.dice = Dice()
        self.dice.roll()
        self.player_scores = ['-'] * 13
        self.roll_count = 1

    def menu(self):
        options = ['1', '2', '3', '4', '5', 'R', 'S', 'Q', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
        choice = ''
        while choice not in options:
            print('Enter which dice to hold (1-5), R to roll, letter (A-M) of line to score, S to show your score, or Q to quit: ')
            print()
            choice = input().upper()

        #HOLD
        if choice == 'R' and self.roll_count < 3:
            self.dice.roll()
            self.roll_count += 1
        #SHOW PLAYER SCORE
        elif choice == 'S':
            self.show_scores('player')
        #QUIT
        elif choice == 'Q':
            quit()
        #HOLD DIE
        elif choice in ['1', '2', '3', '4', '5']:
            choice = int(choice)
            self.dice.hold(choice - 1)

        #CHOOSE SCORING SLOT (and reset roll count and dice holds, then reroll)
        elif choice in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']:
            index = ord(choice) - ord('A')
            if self.player_scores[index] == '-':
                self.player_scores[index] = self.dice.get_scores()[index]
                self.roll_count = 1
                for d in range(5):
                    self.dice.reset_holds()
                    self.dice.roll()
            else:
                input('MUST USE EMPTY SLOT')
            self.show_scores('player')


    def show_dice(self):
        values, holds = self.dice.get_dice()
        print()
        print()
        print('  held:      {}   {}   {}   {}   {}  '.format(*holds))
        print('  values:    {}   {}   {}   {}   {}  '.format(*values))
        print('            (1) (2) (3) (4) (5)')
        print()

    def show_scores(self, dice_or_player):

        if dice_or_player == 'dice':
            scores = self.dice.get_scores()
            message = 'These dice can score in the following ways:'
            for index in range(13):
                if self.player_scores[index] != '-':
                    scores[index] = '-'

        if dice_or_player == 'player':
            scores = self.player_scores
            message = 'Your current score card:'
            
        print()
        print(message)
        print()
        print("(A) Ones:   " + str(scores[0]))
        print("(B) Twos:   " + str(scores[1]))
        print("(C) Threes: " + str(scores[2]))
        print("(D) Fours:  " + str(scores[3]))
        print("(E) Fives:  " + str(scores[4]))
        print("(F) Sixes:  " + str(scores[5]))
        print()
        print("(G) 3 of a Kind:  " + str(scores[6]))
        print("(H) 4 of a Kind:  " + str(scores[7]))
        print("(I) Full House:   " + str(scores[8]))
        print("(J) Sm. Straight: " + str(scores[9]))
        print("(K) Lg. Straight: " + str(scores[10]))
        print("(L) Yahtzee:      " + str(scores[11]))
        print("(M) Chance:       " + str(scores[12]))
        print()
        if dice_or_player == 'player':
            input('(Hit enter to continue)')


g = Game()
while 1:
    print(chr(27) + "[2J") # clear screen
    g.show_dice()
    g.show_scores('dice')
    g.menu()


#NEXT: control game turns (max 3 rolls, then score), keep player score, let player choose what to score (and can score on turn 1 or 2)
#(i think this is done???)

#dice scores: change so it shows blanks or -'s where player has already scored

#then add endgame totalling, final score

#then after done, add high score file that saves name and score

#??? should scores list be dictionary instead for more readable code?

#later: use graphics or gui library ?