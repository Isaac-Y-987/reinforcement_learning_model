from animation import make_frames
from states import LearningState, PhysicalState
import simulation
from learning_model import LearningModel
import numpy as np
from constants import m, r, dt, end_time, alpha, gamma, k

"""
1. set starting physical state and 2. learning state
    3. best_action
    4. take_action
    5. new_state
        6. get_learning_state
    7. reward
        8. update_q
"""

theta_list = []

physical_state = PhysicalState(0,0,m, r, dt)
learning_state = physical_state.get_learning_state()
learning_model = LearningModel(alpha, gamma, k)
for time in np.arange(0, end_time,dt):
    action = learning_model.take_action(learning_state)
    print(f"action = {action}")
    initial_learning_state = physical_state.get_learning_state()
    physical_state = simulation.new_state(action, physical_state)
    learning_state = physical_state.get_learning_state()
    reward = learning_state.reward()
    learning_model.update_q(initial_learning_state, reward, learning_state, action)
    theta_list.append(physical_state.theta)
    print("theta = " + str(round(physical_state.theta, 3)))
    print("v = " + str(round(physical_state.v,3)))

make_frames(theta_list)