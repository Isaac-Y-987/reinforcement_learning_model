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

def new_state(T, initial_physical_state):
    """
    :param T: torque
    :param initial_physical_state:
    :return: final_physical_state
    """
    theta = initial_physical_state.theta
    V = initial_physical_state.V
    m = initial_physical_state.m
    r = initial_physical_state.r
    t = initial_physical_state.t

    if theta <= 0:
        V *= -0.7
        theta = 0
    if theta >= math.pi:
        V *= -0.7
        theta = math.pi
    Vf = V + (T/(m*r^2))*t
    theta_f = theta + Vf*t
    return PhysicalState(theta_f, Vf, m, r, t)
