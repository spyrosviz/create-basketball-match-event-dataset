import numpy as np

'''Draw FIBA basketball court in feet dimensions, with lower left corner being the origin (0,0)'''

def plot_basketball_court(fig,scaling_factor=1, court_color='orange', line_color='black',
                        half_court = False,line_width = 2,opacity = 0.2):

    scale = scaling_factor

    # Set axes properties
    fig.update_layout(width=920, height=500,margin=dict(l=50, r=50, t=50, b=50),paper_bgcolor="lightblue")
    fig.update_xaxes(range=[0 * scale, 92 * scale], showgrid=False,showticklabels=False)
    fig.update_yaxes(range=[0 * scale, 50 * scale], showgrid=False, scaleanchor="x", scaleratio=1,showticklabels=False)

    if half_court == False:

        # Draw outer lines
        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=0 * scale, x1=91.86 * scale, y0=0 * scale, y1=49.21 * scale,
                      line=dict(color=line_color, width=line_width),
                      fillcolor=court_color,opacity=opacity)

        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=0 * scale, x1=91.86 * scale, y0=0 * scale, y1=49.21 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw half line
        fig.add_shape(type="line",
                      x0=91.86 / 2 * scale, y0=0 * scale, x1=91.86 / 2 * scale, y1=49.21 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw circle of half line
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=40.025 * scale, y0=18.7 * scale, x1=51.835 * scale, y1=30.51 * scale,
                      line=dict(color=line_color, width=line_width))

        # DRAW LEFT COURT

        # Draw basket ring
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=4.45 * scale, y0=23.855 * scale, x1=5.95 * scale, y1=25.355 * scale,
                      line_color='red')

        # Draw basket board
        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=4 * scale, x1=4 * scale, y0=21.6525 * scale, y1=27.5575 * scale,
                      line=dict(color='green', width=6))

        # Draw No charge semi circle, radius 1.25m and small lines 0.375m
        fig.add_shape(type="path",
                      path=ellipse_arc(x_center=5.2 * scale, y_center=49.21 / 2 * scale, a=4.1 * scale,
                                       b=4.1 * scale,
                                       start_angle=-0.5 * np.pi, end_angle=0.5 * np.pi),
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      x0=3.93 * scale, y0=28.705 * scale, x1=5.25 * scale, y1=28.705 * scale,
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      x0=3.93 * scale, y0=20.505 * scale, x1=5.25 * scale, y1=20.505 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw free throw outer lines
        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=0 * scale, x1=19 * scale, y0=16.605 * scale, y1=32.605 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw three points area (y=3 y=46.21)
        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=0 * scale, x1=9.514 * scale, y0=2.9 * scale, y1=2.9 * scale,
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=0 * scale, x1=9.514 * scale, y0=46.31 * scale, y1=46.31 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw three points arc
        fig.add_shape(type="path",
                      path=ellipse_arc(x_center=5.2 * scale, y_center=49.21 / 2 * scale, a=22.14 * scale,
                                       b=22.14 * scale,
                                       start_angle=-0.44 * np.pi, end_angle=0.44 * np.pi),
                      line=dict(color=line_color, width=line_width))

        # Draw free throw circle
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=13.095 * scale, y0=18.7 * scale, x1=24.905 * scale, y1=30.51 * scale,
                      line=dict(color=line_color, width=line_width))

        # DRAW RIGHT COURT

        # Draw basket ring
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=85.91 * scale, y0=23.855 * scale, x1=87.41 * scale, y1=25.355 * scale,
                      line_color='red')

        # Draw basket board
        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=87.86 * scale, x1=87.86 * scale, y0=21.6525 * scale, y1=27.5575 * scale,
                      line=dict(color='green', width=6))

        # Draw no charge semi circle
        fig.add_shape(type="path",
                      path=ellipse_arc(x_center=86.66 * scale, y_center=49.21 / 2 * scale, a=4.1 * scale,
                                       b=4.1 * scale,
                                       start_angle=0.5 * np.pi, end_angle=1.5 * np.pi),
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      x0=86.61 * scale, y0=28.705 * scale, x1=87.93 * scale, y1=28.705 * scale,
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      x0=86.61 * scale, y0=20.505 * scale, x1=87.93 * scale, y1=20.505 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw free throw outer lines
        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=72.86 * scale, x1=91.86 * scale, y0=16.605 * scale, y1=32.605 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw three points area
        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=82.346 * scale, x1=91.86 * scale, y0=2.9 * scale, y1=2.9 * scale,
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=82.346 * scale, x1=91.86 * scale, y0=46.31 * scale, y1=46.31 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw three points arc
        fig.add_shape(type="path",
                      path=ellipse_arc(x_center=86.66 * scale, y_center=49.21 / 2 * scale, a=22.14 * scale,
                                       b=22.14 * scale,
                                       start_angle=0.56 * np.pi, end_angle=1.44 * np.pi),
                      line=dict(color=line_color, width=line_width))

        # Draw free throw circle
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=66.955 * scale, y0=18.7 * scale, x1=78.765 * scale, y1=30.51 * scale,
                      line=dict(color=line_color, width=line_width))

    if half_court == True:

        # Draw outer lines
        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=0 * scale, x1=91.86 / 2 * scale, y0=0 * scale, y1=49.21 * scale,
                      line=dict(color=line_color, width=line_width),
                      fillcolor=court_color,opacity=opacity)

        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=0 * scale, x1=91.86 * scale, y0=0 * scale, y1=49.21 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw half line
        fig.add_shape(type="line",
                      x0=91.86 / 2 * scale, y0=0 * scale, x1=91.86 / 2 * scale, y1=49.21 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw circle of half line
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=40.025 * scale, y0=18.7 * scale, x1=51.835 * scale, y1=30.51 * scale,
                      line=dict(color=line_color, width=line_width))

        # DRAW LEFT COURT

        # Draw basket ring
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=4.45 * scale, y0=23.855 * scale, x1=5.95 * scale, y1=25.355 * scale,
                      line_color='red')

        # Draw basket board
        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=4 * scale, x1=4 * scale, y0=21.6525 * scale, y1=27.5575 * scale,
                      line=dict(color='green', width=6))

        # Draw No charge semi circle, radius 1.25m and small lines 0.375m
        fig.add_shape(type="path",
                      path=ellipse_arc(x_center=5.2 * scale, y_center=49.21 / 2 * scale, a=4.1 * scale,
                                       b=4.1 * scale,
                                       start_angle=-0.5 * np.pi, end_angle=0.5 * np.pi),
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      x0=3.93 * scale, y0=28.705 * scale, x1=5.25 * scale, y1=28.705 * scale,
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      x0=3.93 * scale, y0=20.505 * scale, x1=5.25 * scale, y1=20.505 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw free throw outer lines
        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=0 * scale, x1=19 * scale, y0=16.605 * scale, y1=32.605 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw three points area
        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=0 * scale, x1=9.514 * scale, y0=2.9 * scale, y1=2.9 * scale,
                      line=dict(color=line_color, width=line_width))

        fig.add_shape(type="line",
                      xref="x", yref="y",
                      x0=0 * scale, x1=9.514 * scale, y0=46.31 * scale, y1=46.31 * scale,
                      line=dict(color=line_color, width=line_width))

        # Draw three points arc
        fig.add_shape(type="path",
                      path=ellipse_arc(x_center=5.2 * scale, y_center=49.21 / 2 * scale, a=22.14 * scale,
                                       b=22.14 * scale,
                                       start_angle=-0.44 * np.pi, end_angle=0.44 * np.pi),
                      line=dict(color=line_color, width=line_width))

        # Draw free throw circle
        fig.add_shape(type="circle",
                      xref="x", yref="y",
                      x0=13.095 * scale, y0=18.7 * scale, x1=24.905 * scale, y1=30.51 * scale,
                      line=dict(color=line_color, width=line_width))

    return fig

# Function to draw arc in plotly From: https://community.plot.ly/t/arc-shape-with-path/7205/5
def ellipse_arc(x_center=0.0, y_center=0.0, a=10.5, b=10.5, start_angle=0.0, end_angle=2 * np.pi, N=200, closed=False):
    t = np.linspace(start_angle, end_angle, N)
    x = x_center + a * np.cos(t)
    y = y_center + b * np.sin(t)
    path = f'M {x[0]}, {y[0]}'
    for k in range(1, len(t)):
        path += f'L{x[k]}, {y[k]}'
    if closed:
        path += ' Z'
    return path
