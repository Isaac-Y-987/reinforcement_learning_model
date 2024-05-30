"""
inputs: torque, angle_i, velocity_i, mass, radius, time step
outputs: velocity_f, angle_f

Vf = Vi + T/I *t

Of = Oi + Vf*t
"""

from states import PhysicalState

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
    Vf = initial_physical_state.V + (T/(m*r^2))*t
    theta_f = initial_physical_state.theta + Vf*t
    return PhysicalState(theta_f, Vf)
