#!/usr/local/bin/python3

"""
This is where you should write your AI code!
Authors: Aneri Shah(annishah), Hely Modi(helymodi), Dhruva Bhavsar(dbhavsar)
Based on skeleton code by Abhilash Kuhikar, October 2019
"""

from logic_IJK import Game_IJK
import random
import time
import math
from copy import deepcopy
import numpy as np

# Suggests next move to be played by the current player given the current game
#
# inputs:
#     game : Current state of the game 
#
# This function should analyze the current state of the game and determine the 
# best move for the current player. It should then call "yield" on that move.

INF_P = np.Inf

#Finding all the available moves for next player.
def getAvailableMoves():
    if game_clone.isGameFull():
        return False
    else:
        return ['D', 'U', 'R', 'L']


#Finding childrens for a particular node.
def getChildren(game):
    global game_clone
    game_clone = deepcopy(game)
    dirs = getAvailableMoves()
    result = []
    for d in dirs:
        temp = deepcopy(game_clone)
        temp = temp.makeMove(d)
        result.append((d, temp))
    return result






#Got idea of using this heuristic from "http://cs229.stanford.edu/proj2016/report/NieHouAn-AIPlays2048-report.pdf".
#Defining heuristic to find the best possible move.
def evaluate(game):
    utility=[
                [[2 ** 35, 2 ** 34, 2 ** 33, 2 ** 32, 2 ** 31, 2 ** 30],
                [2 ** 29, 2 ** 28, 2 ** 27, 2 ** 26, 2 ** 25, 2 ** 24],
                [2 ** 23, 2 ** 22, 2 ** 21, 2 ** 20, 2 ** 19, 2 ** 18],
                [2 ** 17, 2 ** 16, 2 ** 15, 2 ** 14, 2 ** 13, 2 ** 12],
                [2 ** 11, 2 ** 10, 2 ** 9, 2 ** 8, 2 ** 7, 2 ** 6],
                [2 ** 5, 2 ** 4, 2 ** 3, 2 ** 2, 2 ** 1, 2 ** 0]], 
                
                [[2 ** 35, 2 ** 24, 2 ** 23, 2 ** 12, 2 ** 11, 2 ** 0],
                [2 ** 34, 2 ** 25, 2 ** 22, 2 ** 13, 2 ** 10, 2 ** 1],
                [2 ** 33, 2 ** 26, 2 ** 21, 2 ** 14, 2 ** 9, 2 ** 2],
                [2 ** 32, 2 ** 27, 2 ** 20, 2 ** 15, 2 ** 8, 2 ** 3],
                [2 ** 31, 2 ** 28, 2 ** 19, 2 ** 16, 2 ** 7, 2 ** 4],
                [2 ** 30, 2 ** 29, 2 ** 18, 2 ** 17, 2 ** 6, 2 ** 5]]
            ]
    
    utility.append([item for item in reversed(utility[0])])
    utility.append([list(reversed(item)) for item in reversed(utility[0])])
    utility.append([list(reversed(item)) for item in utility[0]])

    utility.append([item for item in reversed(utility[1])])
    utility.append([list(reversed(item)) for item in reversed(utility[1])])
    utility.append([list(reversed(item)) for item in utility[1]])
    
    finalval = 0
    board = game.getGame()
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]!='':
                finalval = finalval + max(ord(board[r][c])*utility[0][r][c], ord(board[r][c])*utility[1][r][c], ord(board[r][c])*utility[2][r][c], ord(board[r][c])*utility[3][r][c])
    return (finalval, )


#Returns maximum value of the utility function.
def decision(state):
    state.depth_current = 1
    state.path = []
    return maximize(state, -INF_P, INF_P, 1)


#Referenced from "https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/"   

#Finding the maximum utility for the max player.
def maximize(game, alpha, beta, depth):
    
    if game.isGameFull() or depth > 5:
        return (None, game, evaluate(game))

    max_move_direction, max_child, max_utility = None, None, (-INF_P, )
    result = getChildren(game)

    for i in result:
        move_direction, child = i[0], i[1]
        _, state2, utility = minimize(child, alpha, beta, depth+1)
        child.utility = utility

        
        if sum(utility) > sum(max_utility):
            max_move_direction, max_child, max_utility = move_direction, child, utility

        if sum(max_utility) >= beta:
            break

        if sum(max_utility) > alpha:
            alpha = sum(max_utility)

    game.utility = max_utility
    game.alpha = alpha
    game.beta = beta

    return max_move_direction, max_child, max_utility

#Finding the smallest utility for the min player.
def minimize(state, alpha, beta, depth):
    
    if state.isGameFull() or depth > 5:
        return (None, state, evaluate(state))

    min_move_direction, min_child, min_utility = None, None, (INF_P, )
    for move_direction, child in getChildren(state):
        _, state2, utility = maximize(child, alpha, beta, depth+1)
        child.utility = utility

        if sum(utility) < sum(min_utility):
            min_move_direction, min_child, min_utility = move_direction, child, utility

        if sum(min_utility) <= alpha:
            break

        if sum(min_utility) < beta:
            beta = sum(min_utility)

    state.utility = min_utility
    state.alpha = alpha
    state.beta = beta

    return min_move_direction, min_child, min_utility


def next_move(game: Game_IJK)-> None:

    '''board: list of list of strings -> current state of the game
       current_player: int -> player who will make the next move either ('+') or -'-')
       deterministic: bool -> either True or False, indicating whether the game is deterministic or not
    '''

    board = game.getGame()
    player = game.getCurrentPlayer()
    deterministic = game.getDeterministic()

    # You'll want to put in your fancy AI code here. For right now this just 
    # returns a random move    
    direction, child, utility = decision(game)
    yield direction
#    yield random.choice(['U', 'D', 'L', 'R'])