from states import LearningState, PhysicalState
import simulation
from learning_model import LearningModel
import numpy as np

m = 0.1
r = 0.1
dt = 0.01
end_time = 30
alpha = 0.1
gamma = 0.995
k = 10


"""
1. set starting physical state and 2. learning state
    3. best_action
    4. take_action
    5. new_state
        6. get_learning_state
    7. reward
        8. update_q
"""

physical_state = PhysicalState(0,0,m, r, dt) # 1
learning_state = physical_state.get_learning_state() # 2
learning_model = LearningModel(alpha, gamma, k)
for time in np.arange(0, end_time,dt):
    action = learning_model.take_action(learning_state) # 3 & 4
    print(f"Action is {action}")
    initial_learning_state = physical_state.get_learning_state()
    physical_state = simulation.new_state(action, physical_state) # 5
    print(f"New physical state is {physical_state.__dict__}")
    learning_state = physical_state.get_learning_state() # 6
    print(f"New learning state is {learning_state.__dict__}")
    reward = learning_state.reward() #7
    learning_model.update_q(initial_learning_state, reward, learning_state, action) #8




