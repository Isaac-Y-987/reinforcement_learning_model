"""
Classes to be used as standardized ways to fully describe a state.
"""

from math import pi, floor

class PhysicalState:
    """
    All information fully defining a state for physical simulation.
    """
    def __init__(self, theta: float, v: float, m:float, r: float, dt:float):
        """
        :param theta:       angle (radians)
        :param v:           angular velocity (radians per second)
        :param m:           mass (kg)
        :param r:           radius (m)
        :param dt:           timestep (s)
        """
        self.theta = theta
        self.v = v
        self.m = m
        self.r = r
        self.dt = dt
    def get_learning_state(self):
        angle = min(9, floor(self.theta/(pi/10)))
            #Assigns the angle to one of 10 sections
        if abs(self.v) >= 2*pi:
            velocity = 3
        elif abs(self.v) >= pi:
            velocity = 2
        elif abs(self.v) >= 0:
            velocity = 1
        if self.v <0:
            velocity *= -1
        #Assigns the velocity to one of 6 levels (slow, med, fast, and the same in the other direction)
        return LearningState(angle, velocity)

class LearningState:
    """
    All information that a reinforcement learning agent needs in order to represent a state.
    """
    def __init__(self, angle: int, velocity: int):
        """
        :param angle:           int in the range [0,9] inclusive.  0 represents the most clockwise position.
        :param velocity:        int in the range [-3, -1] inclusive or [1, 3].  -3 represents the fastest velocity in
                                the clockwise direction, and 3 represents the fastest velocity in the counterclockwise
                                direction.
        """
        self.angle = angle
        self.velocity = velocity

    def reward(self):
        """
        :return: the reward
        """
        reward = 4.5-abs(5-self.angle)
        return reward

    def __hash__(self):
        return hash((self.angle, self.velocity))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.angle == self.angle and other.velocity == self.velocity
