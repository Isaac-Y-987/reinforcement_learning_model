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

    v = v + (20*T/(m*r**2)) * dt
    theta = theta + v * dt

    if theta <= 0:
        v *= -0.7
        #TODO play around with this value
        theta = 0
    if theta >= math.pi:
        v *= -0.7
        theta = math.pi

    new_physical_state = PhysicalState(theta, v, m, r, dt)
    return new_physical_state
