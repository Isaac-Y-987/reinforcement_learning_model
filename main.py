from animation import make_frames, make_gif
from states import LearningState, PhysicalState
import simulation
from learning_model import LearningModel
import numpy as np
from constants import m, r, dt, end_time, alpha, gamma, k
import os
import glob
from matplotlib import pyplot as plt
from tqdm import tqdm

"""
1. set starting physical state and 2. learning state
    3. best_action
    4. take_action
    5. new_state
        6. get_learning_state
    7. reward
        8. update_q
"""

for filename in glob.glob("reinforcement_learning_output/frames/*.png"):
    os.remove(filename)
if os.path.exists("reinforcement_learning_output/animations/out.gif"):
    os.remove("reinforcement_learning_output/animations/out.gif")

theta_list = []

physical_state = PhysicalState(0,0,m, r, dt)
learning_state = physical_state.get_learning_state()
learning_model = LearningModel(alpha, gamma, k)
for time in tqdm(np.arange(0, end_time,dt)):
    action = learning_model.take_action(learning_state)
    #print(f"action = {action}")
    initial_learning_state = physical_state.get_learning_state()
    physical_state = simulation.new_state(action, physical_state)
    learning_state = physical_state.get_learning_state()
    reward = learning_state.reward()
    learning_model.update_q(initial_learning_state, reward, learning_state, action)
    theta_list.append(physical_state.theta)
    #print("theta = " + str(round(physical_state.theta, 3)))
    #print("v = " + str(round(physical_state.v,3)))

# Plot graphs
x = [xx for xx in np.arange(0, end_time, dt)]
plt.figure()
plt.plot(x, [np.pi/2 for xx in x])
plt.plot(x, theta_list)
plt.ylim(0, np.pi)
plt.show()

# Animate
# TODO: Re-enable?
make_frames(theta_list[:1_000] + theta_list[-1_000:], [ii for ii in range(1_000)] + [ii for ii in range(len(theta_list)-1_000, len(theta_list))])
make_gif("reinforcement_learning_output/frames", "reinforcement_learning_output/animations")
