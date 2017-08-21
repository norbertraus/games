class GameNode(object):
    def __init__(self, game_state, value=None):
        self.game_state = game_state
        self.value = value
        self.actions = []

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.game_state) + ": " + repr(self.value) + "\n"
        for action in self.actions:
            ret += action.__str__(level + 1)
        return ret

    def add_action(self, action):
        self.actions.append(action)

    def add_actions(self, *actions):
        for action in actions:
            self.add_action(action)

    def is_terminal(self):
        return len(self.actions) == 0


def get_test_gametree() -> GameNode:
    b_node = GameNode("B")
    b_node.add_actions(GameNode("B1", 3), GameNode("B2", 12), GameNode("B3", 8))

    c_node = GameNode("C")
    c_node.add_actions(GameNode("C1", 2), GameNode("C2", 4), GameNode("C3", 6))

    d_node = GameNode("D")
    d_node.add_actions(GameNode("D1", 14), GameNode("D2", 5), GameNode("D2", 2))

    root = GameNode("A")
    root.add_actions(b_node, c_node, d_node)

    return root
