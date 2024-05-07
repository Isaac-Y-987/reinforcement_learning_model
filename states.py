"""
Classes to be used as standardized ways to fully describe a state.
"""


class PhysicalState:
    """
    All information fully defining a state for physical simulation.
    """
    def __init__(self, theta: float, v: float):
        """
        :param theta:       angle (radians)
        :param v:           angular velocity (radians per second)
        """
        self.theta = theta
        self.v = v


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
