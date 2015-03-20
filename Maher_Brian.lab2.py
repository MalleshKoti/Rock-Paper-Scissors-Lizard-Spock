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
# Python Version 3.4                                                           #
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

# Element super class
class Element:
    # Constructor, sets the Element's name
    def __init__(self, name):
        self._name = name

    # Name getter, returns the Element's name
    def name(self):
        return self._name

    # Compares this element to the element passed in. This method is used for
    # determining a winner during the game of RPSLS. All child classes of this
    # Element super class implement this function with this same algorithm and
    # should require no additional explaination.
    def compareTo(self, element):
        raise NotImplementedError('Not yet implemented')


# Rock Element
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


# Paper Element
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


# Scissors Element
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


# Lizard Element
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


# Spock Element
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


# List of all available moves as a type of singleton accessor. There's no need
# to create multiple instances of each element, so every Player will have access
# to this list instead.
MOVES = [
    Rock('Rock'),
    Paper('Paper'),
    Scissors('Scissors'),
    Lizard('Lizard'),
    Spock('Spock')
]

# Stored last plays for each player, used by LastPlayBot for selecting plays
player1LastPlay = ''
player2LastPlay = ''


################################################################################
# Players                                                                      #
################################################################################

# Player superclass
class Player:
    # Constructor, sets the player's name
    def __init__(self, name):
        self._name = name

    # Name getter, returns the player's name
    def name(self):
        return self._name

    # This method is called on all Player types and child types. Each child
    # implements this method differently, each algorith will be described within
    # their respective subclasses.
    def play(self):
        NotImplementedError('Not yet implemented')


# StudpidBot Player
class StupidBot(Player):
    # Constructor, sets name and first move as to any random move
    def __init__(self, name):
        self._name = name
        self._move = random.choice(MOVES)

    # After deciding which move he will make first, he repeats the same move for
    # the remainder of the game.
    def play(self):
        return self._move


# RandomBot Player
class RandomBot(Player):
    # Randomly selects his move every time play is called.
    def play(self):
        self._move = random.choice(MOVES)
        return self._move


# IterativeBot player
class IterativeBot(Player):
    # Constructor, sets first move to any random available move
    def __init__(self, name):
        self._name = name
        self._choice = randint(0, 4)

    # Proceeds to iterate (incrememnt counter) for every availble move, by the
    # end of the game, this player will have selected every move once.
    def play(self):
        # By using modulus 5, we can continue to iterate the counter past the
        # end of the array and move it back to the next element in the array
        # by taking its modulus.
        self._move = MOVES[self._choice % 5]
        # Increment iterator
        self._choice += 1
        return self._move


# LastPlayBot Player
class LastPlayBot(Player):
    # Begins by setting a random move as well as a flag to let the bot know that
    # this is his first move, so just return it when play is called.
    def __init__(self, name):
        self._name = name
        self._move = random.choice(MOVES)
        # first move flag
        self._firstMove = True

    # If this is the first move, return it. Otherwise check if my move is
    # different than the first players move, if it is, then I'm not the first
    # player, so store his move. These conditions set out to determine this
    # bot's player number.
    def play(self):
        # set my last move to compare
        myLastMove = self._move
        # return first move if the flag is set, then unset the flag
        if self._firstMove:
            self._firstMove = False
            return self._move
        # If this player's move is different than p1's move, save that one.
        if myLastMove != player1LastPlay:
            self._move = player1LastPlay
        else:
            self._move = player2LastPlay
        return self._move


# MyBot Player
class MyBot(Player):
    # Setup the first move randomly (just so the compiler doesn't scream at us)
    def __init__(self, name):
        self._name = name
        self._move = random.choice(MOVES)
        # Setup a cheater's dictionary. The keys are the other player's move,
        # the values (right side) are what we should pick given the other
        # player's move so that we always win.
        self._cheatMoves = {
            'Scissors': Spock('Spock'),
            'Paper': Scissors('Scissors'),
            'Rock': Paper('Paper'),
            'Lizard': Rock('Rock'),
            'Spock': Lizard('Lizard')
        }

    # Temporarily returns a random move, this move will be thrown away when
    # we start cheating ;)
    def play(self):
        # Temporarily returns a random move
        self._move = random.choice(MOVES)
        return self._move

    # Cheat the game! Lets just always return the opposite of the other player's
    # move!
    def cheat(self, move):
        self._move = move
        return self._cheatMoves[self._move.name()]


# Human Player
class Human(Player):
    # Asks the player for a move and as long as that move is a valid move,
    # returns the move.
    def play(self):
        print (PLAYER_MOVES_STR)
        while True:
            choice = input(ENTER_MOVE_STR)

            if 1 <= int(choice) <= 5:
                self._move = MOVES[int(choice) - 1]
                return self._move

            print (INVALID_MOVE_STR)


# The bots list is separated in order to create two distinct istances for each
# player.

# All possible bots for player 1
PLAYERS1 = [
    Human('Human'),
    StupidBot('StupidBot'),
    RandomBot('RandomBot'),
    IterativeBot('IterativeBot'),
    LastPlayBot('LastPlayBot'),
    MyBot('MyBot')
]

# All possible bots for player 2
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
# Python Version 3.4                                                           #
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
    # Print the header
    print (HEADER_STR)
    
    # Get input selection for which players to use for player1 and player2 as
    # long as the input is valid.
    while True:
        choice1 = input(SELECT_PLAYER_1_STR)
        choice2 = input(SELECT_PLAYER_2_STR)
        if 1 <= int(choice1) <= 6 and 1 <= int(choice2) <= 6:
            break
        print (INVALID_PLAYER_STR)

    # Get the player's respective player objects from their respective lists.
    player1 = PLAYERS1[int(choice1) - 1]
    player2 = PLAYERS2[int(choice2) - 1]

    # Display who the two players are
    print ('\n' + player1.name() + ' vs ' + player2.name() + '. Go!')

    # Win counters
    p1Win = 0
    p2Win = 0

    # Play 5 games
    for i in range(1, 6):
        # Print the current round
        print ('\nRound ' + str(i) + ':')
        
        # Make player moves
        player1Play = player1.play()
        player1LastPlay = player1Play
        player2Play = player2.play()
        player2LastPlay = player2Play
        
        # If the players are MyBot, then they get to cheat ;) If both bots are
        # MyBot, player 2 will always win since it cheats after player 1 cheats.
        if player1.name() == 'MyBot':
            player1Play = player1.cheat(player2Play)
            player1LastPlay = player1Play
        if player2.name() == 'MyBot':
            player2Play = player2.cheat(player1Play)
            player2LastPlay = player2Play

        # Display player moves
        print ('Player 1 chose ' + player1Play.name())
        print ('Player 2 chose ' + player2Play.name())
        
        # Display result of round
        roundResult = player1Play.compareTo(player2Play)
        print (roundResult[0])
        
        # Increment win counters for the winner
        if roundResult[1] == 'Win':
            p1Win += 1
        elif roundResult[1] == 'Lose':
            p2Win += 1

    # Print the winner of all rounds
    print('\nThe score is ' + str(p1Win) + ' to ' + str(p2Win) + '\n')


################################################################################
#                                    EOF                                       #
################################################################################
