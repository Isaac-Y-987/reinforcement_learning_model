"""
inputs: torque, angle_i, velocity_i, mass, radius, time step
outputs: velocity_f, angle_f

Vf = Vi + T/I *t

Of = Oi + Vf*t
"""

#TODO Add gravity
#TODO Add floor

m = 1
r = 1
t = 0.01
def new_state(T, theta_i, Vi):
    """
    :param T: torque
    :param theta_i: initial angle
    :param Vi: initial velocity
    :return: Vf, theta_f
    """
    Vf = Vi + (T/(m*r^2))*t
    theta_f = theta_i + Vf*t
    return Vf, theta_f
