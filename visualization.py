import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def setup_window(W,H,r):
    # set up Window
    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title("Bouncing ball")

    true_ball = Circle((t_x, t_y), radius=r)
    ax.add_patch(true_ball)

    # measured
    measured_ball = Circle((m_x, m_y), radius=r)
    measured_ball.set_color("red")
    measured_ball.set_alpha(0.5)
    ax.add_patch(measured_ball)

    # estimated
    estimated_ball = Circle((e_x, e_y), radius=r)
    estimated_ball.set_color("red")
    estimated_ball.set_alpha(0.5)
    ax.add_patch(estimated_ball)
    return ax





def draw(ax, dt, t_x, t_y, m_x, m_y, e_x, e_y):
    # true
    true_ball.center = (t_x, t_y)
    measured_ball.center = (m_x, m_y)
    estimated_ball.center = (e_x, e_y)

    fig.canvas.draw_idle()
    plt.pause(dt)

