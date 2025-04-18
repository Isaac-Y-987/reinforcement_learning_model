from matplotlib import pyplot as plt
from math import sin, cos
from PIL import Image
from states import PhysicalState
def plot(state: PhysicalState) -> Image:
    """plots one frame of the physical states of the agent"""
    