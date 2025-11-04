import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.animation import PillowWriter

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
def colored_line_between_pts(x, y, c, ax, **lc_kwargs):
    """
    Plot a line with a color specified between (x, y) points by a third value.

    It does this by creating a collection of line segments between each pair of
    neighboring points. The color of each segment is determined by the
    made up of two straight lines each connecting the current (x, y) point to the
    midpoints of the lines connecting the current point with its two neighbors.
    This creates a smooth line with no gaps between the line segments.

    Parameters
    ----------
    x, y : array-like
        The horizontal and vertical coordinates of the data points.
    c : array-like
        The color values, which should have a size one less than that of x and y.
    ax : Axes
        Axis object on which to plot the colored line.
    **lc_kwargs
        Any additional arguments to pass to matplotlib.collections.LineCollection
        constructor. This should not include the array keyword argument because
        that is set to the color argument. If provided, it will be overridden.

    Returns
    -------
    matplotlib.collections.LineCollection
        The generated line collection representing the colored line.
    """

    # Create a set of line segments so that we can color them individually
    # This creates the points as an N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be (numlines) x (points per line) x 2 (for x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(list(segments), **lc_kwargs)

    # Set the values used for colormapping
    lc.set_array(c)

    return ax.add_collection(lc)

fig, axs = plt.subplots(1, 2)
fig.set_figwidth(10)

A = 1
FREQ = 10

t = np.arange(0, 1, 0.001)
x_t = A * np.cos(2 * FREQ * np.pi * t)

axs[0].set_xlabel('Timp (esantioane)')
axs[0].set_ylabel('Amplitudine')
axs[0].plot(t, x_t)
axs[0].axhline(0, color='black', lw=0.5)
axs[0].axvline(0, color='black', lw=0.5)

z_t = x_t * np.exp(-2j * np.pi * A * t)

axs[1].set_xlabel('Real')
axs[1].set_ylabel('Imaginar')
axs[1].plot(np.real(z_t), np.imag(z_t))
axs[1].axhline(0, color='black', lw=0.5)
axs[1].axvline(0, color='black', lw=0.5)

axs[1].set_aspect('equal', adjustable='box')

# plt.show()
plt.savefig('ex2_a.pdf', format='pdf')

fig, axs = plt.subplots(2, 2)
fig.set_figwidth(10)
fig.set_figheight(10)
axs_idx = 0
for omega in [1, 2, 7, 10]:
    z_t = x_t * np.exp(-2j * np.pi * omega * t)
    axs[axs_idx // 2, axs_idx % 2].set_title(f'$\\omega$ = {omega}')
    axs[axs_idx // 2, axs_idx % 2].set_xlabel('Real')
    axs[axs_idx // 2, axs_idx % 2].set_ylabel('Imaginar')
    axs[axs_idx // 2, axs_idx % 2].set_xlim(-1, 1)
    axs[axs_idx // 2, axs_idx % 2].set_ylim(-1, 1)
    axs[axs_idx // 2, axs_idx % 2].set_aspect('equal', adjustable='box')
    axs[axs_idx // 2, axs_idx % 2].axhline(0, color='black', lw=0.5)
    axs[axs_idx // 2, axs_idx % 2].axvline(0, color='black', lw=0.5)

    distance = np.abs(z_t)
    line = colored_line_between_pts(np.real(z_t), np.imag(z_t), distance, axs[axs_idx // 2, axs_idx % 2], cmap='viridis', lw=2)
    fig.colorbar(line, ax=axs[axs_idx // 2, axs_idx % 2], label='Amplitudine')

    axs_idx += 1

# plt.show()
plt.savefig('ex2_b.pdf', format='pdf')

import matplotlib.animation as animation

fig, ax = plt.subplots()

A = 1
FREQ = 10

t = np.arange(0, 1, 0.001)
x_t = A * np.cos(2 * FREQ * np.pi * t)
z_t = x_t * np.exp(-2j * np.pi * A * t)

ax.set_xlabel('Real')
ax.set_ylabel('Imaginar')
ax.axhline(0, color='black', lw=0.5)
ax.axvline(0, color='black', lw=0.5)

ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

# trail line and a separate red head marker
trail_line, = ax.plot([], [], lw=2)
head_point, = ax.plot([], [], 'o', color='red', markersize=6, zorder=5)

def update(frame):
    trail_line.set_data(np.real(z_t[:frame]), np.imag(z_t[:frame]))
    # update head (current drawn point) — avoid negative index at frame==0
    if frame > 0:
        z = z_t[frame - 1]
        head_point.set_data([np.real(z)], [np.imag(z)])
    else:
        head_point.set_data([], [])
    return [trail_line, head_point]

ani = animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=10, blit=True)

writer = PillowWriter(fps=100)
ani.save('ex2_animation_2.gif', writer=writer)