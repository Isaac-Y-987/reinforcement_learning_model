"""Borrows heavily from this source: https://scipython.com/blog/the-double-pendulum/
Create a gif of a double pendulum.
"""
import main
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
import glob
from PIL import Image
from tqdm import tqdm
from constants import m, r, dt, end_time, alpha, gamma, k, r_bob


def make_frames(theta_list):
    #
    # PRODUCING FRAMES
    #

    # Create time vector
    t = np.arange(0, end_time, dt)   # vector of times

    for frame_number, theta in enumerate(theta_list):
        make_plot(theta, frame_number)


def make_plot(theta, frame_number):
    # Plot and save an image of the agent for each angle

    fig = plt.figure(figsize=(8.3333, 6.25), dpi=72)
    ax = fig.add_subplot(111)

    # Convert to Cartesian coordinates of the agent's position
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    ax.plot([0, x], [0, y], lw=2, c='k')
    # Circles representing the anchor point of the rod and the bob
    c0 = Circle((0, 0), r_bob/2, fc='k', zorder=10)
    c1 = Circle((x, y), r_bob, fc='b', ec='b', zorder=10)
    ax.add_patch(c0)
    ax.add_patch(c1)

    # Centre the image on the fixed anchor point, and ensure the axes are equal
    ax.set_xlim(-r - r_bob, r + r_bob)
    ax.set_ylim(-r - r_bob, r + r_bob)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.savefig(f"double_pendulum_outputs/frames/frame{str(frame_number).zfill(6)}.png", dpi=72)
    plt.cla()


#
# COMBINING FRAMES INTO A GIF
#
def make_gif(frame_folder, destination_folder):
    """Given a path to a frame folder, produce a gif animation at the destination folder."""
    frames = [Image.open(image) for image in glob.glob(f"{frame_folder}/*.png")]
    frame_one = frames[0]
    frame_one.save(f"{destination_folder}/out.gif", format="GIF", append_images=frames,
                   save_all=True, duration=dt*1000, loop=0)    # duration is the amount of time between frames, in milliseconds

make_gif("double_pendulum_outputs/frames", "double_pendulum_outputs/animations")
