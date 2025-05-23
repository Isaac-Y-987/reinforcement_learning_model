from collections import defaultdict
from states import LearningState


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
    def best_action(self, current_state: LearningState):
        """
        :param current_state: the current state of the agent
        :return: the best possible action (torque) and its corresponding q value
        """
        best_action = 0
        q_best_action = -float("inf")
        for key, value in self.q_by_state[current_state].items():
            if value > q_best_action:
                q_best_action = value
                best_action = key
        return best_action, q_best_action

    def take_action(self, current_state: LearningState):
        return self.best_action(current_state)[0]

    def update_q(self, previous_state: LearningState, reward, current_state: LearningState, action_0):
        """
        :param previous_state: Previous state where the agent was
        :param reward: The value of reward/penalty the agent received upon entering the new state
        :param current_state: The current state of the agent
        :param action_0: The action the agent took to get from state_0 to state_1
        :return:
        :modify: q value of taking action_0 at state_0
        """
        self.q_by_state[previous_state][action_0] = (1 - self.alpha) * self.q_by_state[previous_state][action_0] + (self.alpha)*(reward + self.gamma * (self.best_action(current_state)[1]))
