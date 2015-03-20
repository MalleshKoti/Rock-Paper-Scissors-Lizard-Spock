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


MOVES = [
    Rock('Rock'),
    Paper('Paper'),
    Scissors('Scissors'),
    Lizard('Lizard'),
    Spock('Spock')
]

player1LastPlay = ''
player2LastPlay = ''


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
        self._firstMove = True

    def play(self):
        myLastMove = self._move
        if self._firstMove:
            self._firstMove = False
            return self._move
        if myLastMove != player1LastPlay:
            return player1LastPlay
        else:
            return player2LastPlay


class MyBot(Player):
    def __init__(self, name):
        self._name = name
        self._move = random.choice(MOVES)
        self._cheatMoves = {
            'Scissors': Spock('Spock'),
            'Paper': Scissors('Scissors'),
            'Rock': Paper('Paper'),
            'Lizard': Rock('Rock'),
            'Spock': Lizard('Lizard')
        }

    def play(self):
        # Temporarily returns a random move
        self._move = random.choice(MOVES)
        return self._move

    def cheat(self, move):
        self._move = move
        return self._cheatMoves[self._move.name()]


class Human(Player):
    def play(self):
        print (PLAYER_MOVES_STR)
        while True:
            choice = input(ENTER_MOVE_STR)

            if 1 <= int(choice) <= 5:
                self._move = MOVES[int(choice) - 1]
                return self._move

            print (INVALID_MOVE_STR)


PLAYERS1 = [
    Human('Human'),
    StupidBot('StupidBot'),
    RandomBot('RandomBot'),
    IterativeBot('IterativeBot'),
    LastPlayBot('LastPlayBot'),
    MyBot('MyBot')
]

PLAYERS2 = [
    Human('Human'),
    StupidBot('StupidBot'),
    RandomBot('RandomBot'),
    IterativeBot('IterativeBot'),
    LastPlayBot('LastPlayBot'),
    MyBot('MyBot')
]


################################################################################
#                               CONST STRINGS                                  #
################################################################################

HEADER_STR = """
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
#                                                                              #
# Please choose two players:                                                   #
#       (1) Human                                                              #
#       (2) StupidBot                                                          #
#       (3) RandomBot                                                          #
#       (4) IterativeBot                                                       #
#       (5) LastPlayBot                                                        #
#       (6) MyBot                                                              #
#                                                                              #
################################################################################
"""

SELECT_PLAYER_1_STR = '#                              Select player 1: '
SELECT_PLAYER_2_STR = '#                              Select player 2: '

INVALID_PLAYER_STR = """
################################################################################
#                                                                              #
# Invalid player. Please try again.                                            #
#                                                                              #
################################################################################
"""

PLAYER_MOVES_STR = """
################################################################################
#                                                                              #
# (1) : Rock                                                                   #
# (2) : Paper                                                                  #
# (3) : Scissors                                                               #
# (4) : Lizard                                                                 #
# (5) : Spock                                                                  #
#                                                                              #
################################################################################
"""

ENTER_MOVE_STR = '#                              Enter your move: '

INVALID_MOVE_STR = """
################################################################################
#                                                                              #
# Invalid move. Please try again.                                              #
#                                                                              #
################################################################################
"""

################################################################################
#                                    Main                                      #
################################################################################

if __name__ == '__main__':
    print (HEADER_STR)
    
    while True:
        choice1 = input(SELECT_PLAYER_1_STR)
        choice2 = input(SELECT_PLAYER_2_STR)
        if 1 <= int(choice1) <= 6 and 1 <= int(choice2) <= 6:
            break
        print (INVALID_PLAYER_STR)

    player1 = PLAYERS1[int(choice1) - 1]
    player2 = PLAYERS2[int(choice2) - 1]

    print (player1.name() + ' vs ' + player2.name() + '. Go!')

    p1Win = 0
    p2Win = 0

    for i in range(1, 6):
        print ('Round ' + str(i) + ':')
        player1Play = player1.play()
        player1LastPlay = player1Play
        player2Play = player2.play()
        player2LastPlay = player2Play
        print ('Player 1 chose ' + player1Play.name())
        print ('Player 2 chose ' + player2Play.name())
        if player1.name() == 'MyBot':
            player1Play = player1.cheat(player2Play)
            player1LastPlay = player1Play
        if player2.name() == 'MyBot':
            player2Play = player2.cheat(player1Play)
            player2LastPlay = player2Play
        roundResult = player1Play.compareTo(player2Play)
        print (roundResult[0])
        if roundResult[1] == 'Win':
            p1Win += 1
        elif roundResult[1] == 'Lose':
            p2Win += 1

    print('The score is ' + str(p1Win) + ' to ' + str(p2Win))


################################################################################
#                                    EOF                                       #
################################################################################
