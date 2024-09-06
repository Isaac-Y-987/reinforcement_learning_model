"""
inputs: torque, angle_i, velocity_i, mass, radius, time step
outputs: velocity_f, angle_f

Vf = Vi + T/I *t

Of = Oi + Vf*t
"""

from states import PhysicalState
import math
#TODO Add gravity
#TODO Add floor

m = 1
r = 1
t = 0.01
def new_state(T, initial_physical_state):
    """
    :param T: torque
    :param initial_physical_state:
    :return: final_physical_state
    """
    if initial_physical_state.theta <= 0:
        initial_physical_state.V *= -0.7
        initial_physical_state.theta = 0
    if initial_physical_state.theta >= math.pi:
        initial_physical_state.V *= -0.7
        initial_physical_state.theta = math.pi
    Vf = initial_physical_state.V + (T/(m*r^2))*t
    theta_f = initial_physical_state.theta + Vf*t
    return PhysicalState(theta_f, Vf)
