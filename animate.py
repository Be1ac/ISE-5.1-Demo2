import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Plotly Animation Demo", layout="wide")

st.title("3 Basic Plotly Animations in Streamlit")

# 1. Update your choice list at the top of the file
animation_choice = st.selectbox(
    "Choose an animation",
    [
        "Rotating 3D Helix",
        "Moving Sine Wave",
        "Bouncing Ball",
        "Expanding 3D Ripple",  # Add this!
    ],
)

num_frames = 60


def rotating_3d_helix():
    t = np.linspace(0, 8 * np.pi, 200)
    x = np.cos(t)
    y = np.sin(t)
    z = np.linspace(-2, 2, 200)

    frames = []
    for i in range(num_frames):
        angle = 2 * np.pi * i / num_frames
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=x_rot,
                        y=y_rot,
                        z=z,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Rotating 3D Helix",
        scene=dict(
            xaxis=dict(range=[-1.5, 1.5]),
            yaxis=dict(range=[-1.5, 1.5]),
            zaxis=dict(range=[-2.5, 2.5]),
            aspectmode="cube",
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def moving_sine_wave():
    x = np.linspace(0, 4 * np.pi, 300)

    frames = []
    for i in range(num_frames):
        phase = 2 * np.pi * i / num_frames
        y = np.sin(x + phase)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=x,
                        y=y,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=np.sin(x),
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Moving Sine Wave",
        xaxis=dict(range=[0, 4 * np.pi]),
        yaxis=dict(range=[-1.5, 1.5]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def bouncing_ball():
    x_positions = np.linspace(0, 10, num_frames)
    y_positions = np.abs(np.sin(np.linspace(0, 3 * np.pi, num_frames))) * 5

    frames = []
    for i in range(num_frames):
        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=[x_positions[i]],
                        y=[y_positions[i]],
                        mode="markers",
                        marker=dict(size=20),
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=[x_positions[0]],
                y=[y_positions[0]],
                mode="markers",
                marker=dict(size=20),
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Bouncing Ball",
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 6]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 60, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig
# 2. Add this function to your script
def expanding_3d_ripple():
    # Setup coordinates: a grid from -5 to 5
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    x_grid, y_grid = np.meshgrid(x, y)
    
    # Pre-calculate the distance from center (radius) for the ripple effect
    r = np.sqrt(x_grid**2 + y_grid**2)

    frames = []
    for i in range(num_frames):
        # The 'phase' shifts the sine wave over time to create movement
        phase = 2 * np.pi * i / num_frames
        # Z is the height. We use sin(r - phase) to make the waves move outward
        z = np.sin(r - phase)

        frames.append(
            go.Frame(
                data=[go.Surface(z=z, x=x, y=y)],
                name=str(i)
            )
        )

    # Initial state of the plot
    fig = go.Figure(
        data=[go.Surface(z=np.sin(r), x=x, y=y)],
        frames=frames
    )

    fig.update_layout(
        title="Expanding 3D Ripple",
        scene=dict(
            zaxis=dict(range=[-1, 1]),
            aspectmode="manual",
            aspectratio=dict(x=1, y=1, z=0.5) # Flattens the view for better visibility
        ),
        updatemenus=[{
            "type": "buttons",
            "buttons": [
                {"label": "Play", "method": "animate", "args": [None, {"frame": {"duration": 40}}]},
                {"label": "Pause", "method": "animate", "args": [[None], {"mode": "immediate"}]}
            ]
        }]
    )
    return fig

# 3. Update your logic at the bottom
if animation_choice == "Rotating 3D Helix":
    fig = rotating_3d_helix()
elif animation_choice == "Moving Sine Wave":
    fig = moving_sine_wave()
elif animation_choice == "Expanding 3D Ripple":
    fig = expanding_3d_ripple()
else:
    fig = bouncing_ball()

st.plotly_chart(fig, use_container_width=True)