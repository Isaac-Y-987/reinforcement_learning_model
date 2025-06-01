from states import LearningState, PhysicalState
import simulation
from learning_model import LearningModel
import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

m = 0.1
r = 0.1
dt = 0.01
end_time = 30000
alpha = 0.1
gamma = 0.995
k = 1000


"""
1. set starting physical state and 2. learning state
    3. best_action
    4. take_action
    5. new_state
        6. get_learning_state
    7. reward
        8. update_q
"""

# Run simulation
all_timestamps = np.arange(0, end_time,dt)
all_thetas = []
all_rewards = []
physical_state = PhysicalState(0,0,m, r, dt) # 1
learning_state = physical_state.get_learning_state() # 2
learning_model = LearningModel(alpha, gamma, k)
for time in tqdm(all_timestamps):
    action = learning_model.take_action(learning_state) # 3 & 4
    #print(f"Action is {action}")
    initial_learning_state = physical_state.get_learning_state()
    physical_state = simulation.new_state(action, physical_state) # 5
    #print(f"New physical state is {physical_state.__dict__}")
    all_thetas.append(physical_state.theta)
    learning_state = physical_state.get_learning_state() # 6
    #print(f"New learning state is {learning_state.__dict__}")
    reward = learning_state.reward() #7
    all_rewards.append(reward)
    learning_model.update_q(initial_learning_state, reward, learning_state, action) #8

# Plot sectors
x = [float(xx) for xx in np.arange(0, np.pi, 0.001)]
y = [PhysicalState(theta=xx, v=1, m=m, r=r, dt=dt).get_learning_state().angle for xx in x]
theoretical_rewards = [PhysicalState(theta=xx, v=1, m=m, r=r, dt=dt).get_learning_state().reward() for xx in x]
plt.figure()
plt.plot(x, y)
plt.plot(x, theoretical_rewards)
plt.legend(["angle", "reward"])
plt.show()

# Plot results
fig, axs = plt.subplots(2)
axs[0].plot(all_timestamps, all_thetas)
axs[0].plot(all_timestamps, [np.pi/2]*len(all_timestamps))
axs[0].set_xlabel("time (s)")
axs[0].set_ylabel("angle (rad)")
axs[1].plot(all_timestamps, all_rewards)
axs[1].set_xlabel("time (s)")
axs[1].set_ylabel("reward")
plt.show()
