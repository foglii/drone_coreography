import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter

def animate_trajectories(trajectories, out_name='animation.mp4', fps=30,
                         xlim=None, ylim=None, zlim=None):
    """
    Animate multiple moving points in 3D based on coordinate lists.

    Parameters:
        trajectories : list of lists
            Each element is a list of (x, y, z, dt) tuples for one point.
        out_name : str
            Output MP4 filename.
        fps : int
            Frames per second.
        xlim : tuple, optional
            Limits for the x-axis.
        ylim : tuple, optional
            Limits for the y-axis.
        zlim : tuple, optional
            Limits for the z-axis.
    """

    # Convert to arrays and compute absolute times
    processed = []
    for traj in trajectories:
        traj = np.array(traj)
        times = np.cumsum(traj[:, 3])  # cumulative time
        processed.append((traj[:, :3], times))

    total_time = max(t[-1] for _, t in processed)
    n_frames = int(total_time * fps)

    # Prepare figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect([1, 1, 1])

    # Define limits based on all data (can be overridden by xlim/ylim/zlim args)
    all_points = np.concatenate([p for p, _ in processed])
    computed_xlim = (all_points[:, 0].min() - 1, all_points[:, 0].max() + 1)
    computed_ylim = (all_points[:, 1].min() - 1, all_points[:, 1].max() + 1)
    computed_zlim = (all_points[:, 2].min() - 1, all_points[:, 2].max() + 1)

    if xlim is None:
        xlim = computed_xlim
    if ylim is None:
        ylim = computed_ylim
    if zlim is None:
        zlim = computed_zlim

    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_zlim(*zlim)

    # Create scatter objects and labels
    scatters = []
    for i, (points, _) in enumerate(processed, start=1):
        scat = ax.scatter([], [], [], s=50, label=f"List {i}")
        scatters.append(scat)

    # Add legend once
    ax.legend(loc='upper right')

    def interpolate_position(points, times, t):
        if t <= times[0]:
            return points[0]
        if t >= times[-1]:
            return points[-1]
        i = np.searchsorted(times, t)
        t0, t1 = times[i - 1], times[i]
        p0, p1 = points[i - 1], points[i]
        alpha = (t - t0) / (t1 - t0)
        return p0 + alpha * (p1 - p0)

    def update(frame):
        t = frame / fps
        for scat, (points, times) in zip(scatters, processed):
            pos = interpolate_position(points, times, t)
            scat._offsets3d = ([pos[0]], [pos[1]], [pos[2]])
        ax.set_title(f"t = {t:.2f}s")
        return scatters


    anim = FuncAnimation(fig, update, frames=n_frames, interval=1000/fps, blit=False)
    # write mp4 using ffmpeg; ensure ffmpeg is installed.
    # use yuv420p pixel format for maximum player compatibility
    writer = FFMpegWriter(fps=fps, codec='libx264',
                         extra_args=['-pix_fmt', 'yuv420p', '-preset', 'medium'])
    anim.save(out_name, writer=writer)
    plt.close(fig)
    print(f"Saved animation to {out_name}")

