# minmax game tree search algorithm
import math
from game_node import *


def minmax(state: GameNode, maximizer=True):
    if state.is_terminal():
        print("Terminal state '%s' with value: %d" % (state.game_state, state.value))
        return state.value

    if maximizer:
        max_value = -math.inf
        for action in state.actions:
            print("Expanding MAX state '%s'" % action.game_state)
            max_value = max(max_value, minmax(action, maximizer=False))

        return max_value
    else:
        min_value = math.inf
        for action in state.actions:
            print("Expanding MIN state '%s'" % action.game_state)
            min_value = min(min_value, minmax(action, maximizer=True))

        return min_value


root = get_test_gametree()

print(root)
print("Minmax value of the game tree: %d" % minmax(root))
