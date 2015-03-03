################################################################################
#                                                                              #
#                    Rock, Paper, Scissors, Lizard, Spock                      #
#                                                                              #
################################################################################
#          _________  _________  _____  _________  _______ ____                #
#         /\        \/         \/     \/         \/       \    \               #
#         \ \   \    \\    \    \\     \\    \    \\       \    \              #
#          \ \        \\         \\     \\         \\       \    \             #
#           \ \     ---\\      ---\\     \\         \\            \            #
#            \ \        \\    \    \\     \\    \    \\    \       \           #
#             \ \   \    \\    \    \\     \\    \    \\    \       \          #
#              \ \________\_____\____\______\_____\____\_____\_______\         #
#               \/________/_____/____/______/_____/____/_____/_______/         #
#                                                                              #
################################################################################
#                                                                              #
# A Python programming project for CPTS 305                                    #
#                                                                              #
# Montana State University                                                     #
# Author: Brian Maher                                                          #
#                                                                              #
################################################################################

# import pygame
import random
from random import randint

################################################################################
#                                  Classes                                     #
################################################################################
# Elements                                                                     #
################################################################################

class Element:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def compareTo(self, element):
        raise NotImplementedError('Not yet implemented')


class Rock(Element):
    def compareTo(self, element):
        if element.name() == 'Rock':
            return 'Rock equals Rock', 'Tie'
        elif element.name() == 'Lizard':
            return 'Rock crushes Lizard', 'Win'
        elif element.name() == 'Scissors':
            return 'Rock crushes Scissors', 'Win'
        elif element.name() == 'Paper':
            return 'Paper covers Rock', 'Lose'
        elif element.name() == 'Spock':
            return 'Spock vaporizes Rock', 'Lose'


class Paper(Element):
    def compareTo(self, element):
        if element.name() == 'Paper':
            return 'Paper equals Paper', 'Tie'
        elif element.name() == 'Rock':
            return 'Paper covers Rock', 'Win'
        elif element.name() == 'Spock':
            return 'Paper disproves Spock', 'Win'
        elif element.name() == 'Scissors':
            return 'Scissors cut Paper', 'Lose'
        elif element.name() == 'Lizard':
            return 'Lizard eats Paper', 'Lose'


class Scissors(Element):
    def compareTo(self, element):
        if element.name() == 'Scissors':
            return 'Scissors equals Scissors', 'Tie'
        elif element.name() == 'Paper':
            return 'Scissors cut Paper', 'Win'
        elif element.name() == 'Lizard':
            return 'Scissors decapitate Lizard', 'Win'
        elif element.name() == 'Spock':
            return 'Spock smashes Scissors', 'Lose'
        elif element.name() == 'Rock':
            return 'Rock crushes Scissors', 'Lose'


class Lizard(Element):
    def compareTo(self, element):
        if element.name() == 'Lizard':
            return 'Lizard equals Lizard', 'Tie'
        elif element.name() == 'Spock':
            return 'Lizard poisons Spock', 'Win'
        elif element.name() == 'Paper':
            return 'Lizard eats Paper', 'Win'
        elif element.name() == 'Rock':
            return 'Rock crushes Lizard', 'Lose'
        elif element.name() == 'Scissors':
            return 'Scissors decapitate Lizard', 'Lose'


class Spock(Element):
    def compareTo(self, element):
        if element.name() == 'Spock':
            return 'Spock equals Spock', 'Tie'
        elif element.name() == 'Scissors':
            return 'Spock smashes Scissors', 'Win'
        elif element.name() == 'Rock':
            return 'Spock vaporizes Rock', 'Win'
        elif element.name() == 'Lizard':
            return 'Lizard poisons Spock', 'Lose'
        elif element.name() == 'Paper':
            return 'Paper disproves Spock', 'Lose'


################################################################################
# Players                                                                      #
################################################################################

class Player:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def play(self):
        NotImplementedError('Not yet implemented')


class StupidBot(Player):
    def __init__(self, name):
        self._name = name
        self._move = random.choice(MOVES)

    def play(self):
        return self._move


class RandomBot(Player):
    def play(self):
        self._move = random.choice(MOVES)
        return self._move


class IterativeBot(Player):
    def __init__(self, name):
        self._name = name
        self._choice = randint(0, 4)

    def play(self):
        self._move = MOVES[self._choice % 5]
        self._choice += 1
        return self._move


class LastPlayBot(Player):
    def __init__(self, name):
        self._name = name
        self._move = random.choice(MOVES)

    def play(self):
        lastMove = self._move
        # TODO: Reset lastMove somehow
        return move


class Human(Player):
    def play(self):
        print PLAYER_MOVES
        # TODO: Get user input
        # TODO: Select correct move


################################################################################
#                                  Globals                                     #
################################################################################

HEADER = """
################################################################################
#                                                                              #
#                    Rock, Paper, Scissors, Lizard, Spock                      #
#                                                                              #
################################################################################
#          _________  _________  _____  _________  _______ ____                #
#         /\        \/         \/     \/         \/       \    \               #
#         \ \   \    \     \    \      \     \    \        \    \              #
#          \ \        \          \      \          \        \    \             #
#           \ \     ---\       ---\      \          \             \            #
#            \ \        \     \    \      \     \    \     \       \           #
#             \ \   \    \     \    \      \     \    \     \       \          #
#              \ \________\_____\____\______\_____\____\_____\_______\         #
#               \/________/_____/____/______/_____/____/_____/_______/         #
#                                                                              #
################################################################################
#                                                                              #
# A Python programming project for CPTS 305                                    #
#                                                                              #
# Montana State University                                                     #
# Author: Brian Maher                                                          #
#                                                                              #
################################################################################
"""

PLAYER_MOVES = """
#                                                                              #
# (1) : Rock                                                                   #
# (2) : Paper                                                                  #
# (3) : Scissors                                                               #
# (4) : Lizard                                                                 #
# (5) : Spock                                                                  #
#                                                                              #
################################################################################
# Enter you move: """

MOVES = [
    Rock('Rock'),
    Paper('Paper'),
    Scissors('Scissors'),
    Lizard('Lizard'),
    Spock('Spock')
]

################################################################################
#                                    Main                                      #
################################################################################

if __name__ == '__main__':
    print HEADER
    bot = IterativeBot('IterativeBot')
    print Paper('Paper').compareTo(bot.play())


################################################################################
#                                    EOF                                       #
################################################################################
