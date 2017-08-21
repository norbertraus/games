# alpha-beta pruning search tree algorithm

import math
from game_node import *


def alpha_beta_pruning(node):
    return _max_value(node, -math.inf, math.inf)


def _max_value(state: GameNode, alpha, beta):
    """
    find the maximum utility value from the game tree using alpha-beta pruning
    :param state: game tree state node
    :param alpha: the highest value found so far (best value for Maximizing player)
    :param beta: the lowest value found so far (best value for Maximizing player)
    :return: maximum utility value
    """
    if state.is_terminal():
        print("Terminal state '%s' with value: %d" % (state.game_state, state.value))
        return state.value

    value = -math.inf
    for action in state.actions:
        print("Expanding MIN state '%s'" % action.game_state)
        value = max(value, _min_value(action, alpha, beta))

        if value >= beta: return value
        alpha = max(value, alpha)
    return value


def _min_value(state: GameNode, alpha, beta):
    """
    find the minimum utility value from the game tree using alpha-beta pruning
    :param state: game tree state node
    :param alpha: the highest value found so far (best value for Maximizing player)
    :param beta: the lowest value found so far (best value for Maximizing player)
    :return: minumum utility value
    """
    if state.is_terminal():
        return state.value

    value = math.inf
    for action in state.actions:
        print("Expanding MAX state '%s'" % action.game_state)
        value = min(value, _max_value(action, alpha, beta))

        if value <= alpha: return value
        beta = min(value, beta)
    return value

root = get_test_gametree()

print(root)
alpha_beta_pruning(root)

# print("Alpha-Beta pruning search value of the game tree: %d" % alpha_beta_pruning(root))
