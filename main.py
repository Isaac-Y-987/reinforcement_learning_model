from states import LearningState, PhysicalState
import simulation
from learning_model import LearningModel
import numpy as np

m = 1
r = 1
dt = 0.01
end_time = 30
alpha = 0.1
gamma = 0.995


"""
set starting physical state and learning state
    best_action
    take_action
    new_state
        get_learning_state
    reward
        update_q
"""

physical_state_0 = PhysicalState(0,0)
learning_state_0 = physical_state_0.get_learning_state()
learning_model = LearningModel(alpha, gamma)
for time in np.arange(0, end_time,dt):
    action = learning_model.take_action(learning_state_0)
