from collections import defaultdict
import states


def empty_choices():
    choices = {-3: 0, -2: 0, -1: 0, 0: 0, 1: 0, 2: 0, 3: 0}
    return choices


class LearningModel:
    def __init__(self, alpha, gamma):
        """
        :param alpha: learning rate (0-1]
        :param gamma: reward decay rate (0-1]
        """
        self.q_by_state = defaultdict(empty_choices)
        self.alpha = alpha
        self.gamma = gamma

    def update_q(self, state_0, reward, state_1, action_0):
        q_best_action = -float("inf")
        for value in self.q_by_state[state_1].values:
            if value > q_best_action:
                q_best_action = value
        self.q_by_state[state_0][action_0] = (1 - self.alpha) * self.q_by_state[state_0][action_0] + (self.alpha)(reward + self.gamma * (q_best_action))

