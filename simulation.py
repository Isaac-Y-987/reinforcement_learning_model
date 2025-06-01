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
    v = initial_physical_state.v
    m = initial_physical_state.m
    r = initial_physical_state.r
    dt = initial_physical_state.dt

    Vf = v + (T/(m*r^2)) * dt
    theta_f = theta + Vf * dt
    if theta_f <= 0:
        v *= -0.7
        #TODO play around with this value
        theta_f = 0
    if theta_f >= math.pi:
        v *= -0.7
        theta_f = math.pi
    new_physical_state = PhysicalState(theta_f, Vf, m, r, dt)
    return new_physical_state
