import plotly.graph_objects as go
import chart_studio.plotly as py
import numpy as np
import math
import matplotlib.pyplot as plt
import mpld3

# cone: https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.Cone.html
# Scatter3d: https://plotly.github.io/plotly.py-docs/generated/plotly.graph_objects.Scatter3d.html
# mpld3: https://mpld3.github.io/quickstart.html

if __name__=="__main__":
    vec = np.array([0,0,1])
    angle = math.pi/4.0
    samples = np.linspace(0.0, angle, num = 10, endpoint=True)
    curve = np.zeros((len(samples)+1, 3))
    for iii, sample in enumerate(samples):
        curve[iii,0] = math.cos(samples[iii])
        curve[iii,1] = math.sin(samples[iii])
        curve[iii,2] = 0
    curve = curve * 0.1
    curve[-1,0] = 0.1
    curve[-1,1] = 0.07
    curve[-1,2] = 0.0
    # print(curve)
    fig = go.Figure(data=[
        # go.Cone(x=[vec[0]], y=[vec[1]], z=[vec[2]-0.1], u=[vec[0]], v=[vec[1]], w=[vec[2]/10], showlegend=False, showscale=False, sizemode='absolute', sizeref=0.15),
        go.Scatter3d(dict(name='u', x=[0,0,0.03], y=[0,0,0], z=[0,1,0.9], mode='lines', hoverinfo='skip', line=dict(width=4, showscale=False, color='red'))),
        # go.Scatter3d(dict(name='u', x=[0.05,0], y=[0,0], z=[0.9,1], mode='lines', line=dict(width=4, showscale=False, color='red'))),
        go.Scatter3d(dict(name='theta', x=curve[:,0], y=curve[:,1], z=curve[:,2], mode='lines', line=dict(width=2, showscale=False, color='blue'))),
        # go.Cone(x=[curve[-1,0]], y=[curve[-1,1]], z=[curve[-1,2]], u=[-curve[-1,0]], v=[curve[-1,1]], w=[curve[-1,2]], showlegend=False, showscale=False, sizemode='absolute', sizeref=0.05),

    ])
    fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=4, range=[-0.3,0.3],),
        yaxis = dict(nticks=4, range=[-0.3,0.3],),
        zaxis = dict(nticks=4, range=[0,1]))
    )



    fig.write_html("../alonzolopez.github.io/assets/images/blog/rotations/rot.html")

    fig2 = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([0,1])
    start = [0,0,0]
    
    # fig2_html = mpld3.fig_to_html(fig2)
    ax.quiver(start[0], start[1], start[2], vec[0], vec[1], vec[2])
    ax.view_init(15,135)
    # plt.show()
    # ax.w_xaxis.set_pane_color((229.0/256.0,236.0/256.0,246.0/256.0, 1.0))
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    # ax.set_xticks=0.5
    # ax.set_yticks=0.5
    # ax.set_zticks=0.5
    ax.xaxis.set_ticks([])
    plt.savefig("../alonzolopez.github.io/assets/images/blog/rotations/rot2.png", transparent=True)

    # mpld3.save_html(fig2, "../alonzolopez.github.io/assets/images/blog/rotations/rot2.html")
