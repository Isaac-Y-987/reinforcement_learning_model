"""Borrows heavily from this source: https://scipython.com/blog/the-double-pendulum/
Create a gif of a double pendulum.
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
import glob
from PIL import Image
from tqdm import tqdm
from constants import m, r, dt, end_time, alpha, gamma, k, r_bob


def make_frames(theta_list, frame_numbers):
    #
    # PRODUCING FRAMES AT 10 FPS
    #

    # Reduce theta_list and frame_numbers to just 10 frames per second
    reduction_modulo = round(0.1 / dt)     # 0.01 -> 10
    theta_list_reduced = [theta for ii, theta in enumerate(theta_list) if ii % reduction_modulo == 0]
    frame_numbers_reduced = [frame_number for ii, frame_number in enumerate(frame_numbers) if ii % reduction_modulo == 0]

    # Plot
    for frame_number, theta in tqdm(zip(frame_numbers_reduced, theta_list_reduced), total=len(theta_list_reduced)):
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

    # Add timestamp
    ax.text(0, -0.25, f"t = {round(frame_number * dt, 3)} s")

    # Centre the image on the fixed anchor point, and ensure the axes are equal
    ax.set_xlim(-r - r_bob, r + r_bob)
    ax.set_ylim(-r - r_bob, r + r_bob)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.savefig(f"reinforcement_learning_output/frames/frame{str(frame_number).zfill(6)}.png", dpi=72)
    plt.cla()


#
# COMBINING FRAMES INTO A GIF
#
def make_gif(frame_folder, destination_folder):
    """Given a path to a frame folder, produce a 10 fps gif animation at the destination folder."""
    frame_filepaths = glob.glob(f"{frame_folder}/*.png")
    frame_filepaths.sort()
    frames = [Image.open(image) for image in frame_filepaths]
    frames[0].save(f"{destination_folder}/out.gif", format="GIF", append_images=frames[1:],
                   save_all=True, duration=dt*1000, loop=0)    # duration is the amount of time between frames, in milliseconds
