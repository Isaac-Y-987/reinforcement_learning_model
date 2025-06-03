from collections import defaultdict
from states import LearningState

choices = [-1.5, -1, -0.5, 0, 0.5, 1, 1.5]

def empty_choices():
    return {choice: 0 for choice in choices}

def one_choices():
    return {choice: 1 for choice in choices}


class LearningModel:
    def __init__(self, alpha, gamma, k):
        """
        :param alpha: learning rate (0-1]
        :param gamma: reward decay rate (0-1]
        :param k:     exploration constant [0-inf).  Higher values encourage more exploration.
        """
        self.q_by_state = defaultdict(empty_choices)    # First key is state, second key is action
        self.visit_counts = defaultdict(one_choices)    # First key is state, second key is action
        self.alpha = alpha
        self.gamma = gamma
        self.k = k

    def best_action(self, current_state: LearningState):
        """
        :param current_state: the current state of the agent
        :return: the best possible action (torque) and its corresponding q value
        """
        best_action = 0
        q_best_action = -float("inf")
        for key, value in self.q_by_state[current_state].items():
            visit_count = self.visit_counts[current_state][key]
            value = self.appreciate_novelty(value, visit_count)
            if value > q_best_action:
                q_best_action = value
                best_action = key
        return best_action, q_best_action

    def take_action(self, current_state: LearningState):
        """
        Return the best action for this state and increment the visit count for this state+action combination.
        :param current_state:
        :return:
        """
        best_action = self.best_action(current_state)[0]
        self.visit_counts[current_state][best_action] += 1
        return best_action

    def appreciate_novelty(self, value_estimate, visit_count):
        """
        Add a bonus score to the value estimate that is greater for lower visit counts.
        :param value_estimate:      raw Q score for this state-action pair
        :param visit_count:         number of times this state-action pair has been visited.
        :return:                    the value estimate plus some bonus
        """
        return value_estimate + self.k / visit_count

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
