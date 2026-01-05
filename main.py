import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# world
W, H = 10.0, 10.0

# sim params
dt = 0.01  # sampling time
N = 1000  # n samples

# sensor
sigma_z = 0.15  # std dev for measurements

# states, px py vx vy
x = np.array([2.0, 1.0, 3.0, 2.0])
rng = np.random.default_rng(0)  # seed for rng

# set up Window
plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.set_aspect("equal", adjustable="box")
ax.set_title("Bouncing ball")

# draw balls
r = 0.3
# true
true_ball = Circle((x[0], x[1]), radius=r)
ax.add_patch(true_ball)

# measured
measured_ball = Circle((x[0], x[1]), radius=r)
measured_ball.set_color("red")
measured_ball.set_alpha(0.5)
ax.add_patch(measured_ball)

# filtered
filtered_ball = Circle((x[0], x[1]), radius=r)
filtered_ball.set_color("red")
filtered_ball.set_alpha(0.5)
ax.add_patch(filtered_ball)


for k in range(N):
    px, py, vx, vy = x

    # true dynamics
    px = px + vx * dt
    py = py + vy * dt

    # bounce
    if px < 0.0+r:
        px = 0.0+r
        vx = -vx
    if px > W-r:
        px = W-r
        vx = -vx
    if py < 0.0+r:
        py = 0.0+r
        vy = -vy
    if py > H-r:
        py = H-r
        vy = -vy

    #  update state
    x = np.array([px, py, vx, vy])

    # noisy measurement
    m_px = px + rng.normal(0.0, sigma_z)
    m_py = py + rng.normal(0.0, sigma_z)

    true_ball.center = (px, py)
    measured_ball.center = (m_px, m_py)

    fig.canvas.draw_idle()
    plt.pause(dt)
    current_time = k*dt
    print("t= " + str(current_time))
