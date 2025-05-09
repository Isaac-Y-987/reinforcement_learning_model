"""
inputs: torque, angle_i, velocity_i, mass, radius, time step
outputs: velocity_f, angle_f

Vf = Vi + T/I *t

Of = Oi + Vf*t
"""

from states import PhysicalState
import math
#TODO Add gravity

def new_state(T, initial_physical_state: PhysicalState):
    """
    :param T: torque
    :param initial_physical_state:
    :return: final_physical_state
    """
    theta = initial_physical_state.theta
    V = initial_physical_state.V
    m = initial_physical_state.m
    r = initial_physical_state.r
    dt = initial_physical_state.dt

    if theta <= 0:
        V *= -0.7
        #TODO play around with this value
        theta = 0
    if theta >= math.pi:
        V *= -0.7
        theta = math.pi
    Vf = V + (T/(m*r^2)) * dt
    theta_f = theta + Vf * dt
    return PhysicalState(theta_f, Vf, m, r, dt)
