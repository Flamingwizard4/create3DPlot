#these should be imported:
import chart_studio.plotly as py
import plotly.graph_objs as go
import numpy as np
from PIL import Image

#this should be in createDataSummary or somewhere
###3D_url = create3DPlot(self.localDepthDirectory + self.totalHeightChange)

def create3DPlot(path):

    depthChange = np.load(path)
    depthChange[depthChange!=depthChange] = 0
    depthChange = np.array(Image.fromarray(depthChange).resize((224,224), resample= Image.BILINEAR))
    depthChange *= 10
    depthChange = depthChange.astype('int8')

    ''' analyzer
    for line in depthChange:
        print(line)
    '''

    data = [go.Surface(z=depthChange, colorscale='Jet')]

    layout = go.Layout(
        width=800,
        height=700,
        autosize=False,
        title='Depth Change',
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            aspectratio = dict( x=1, y=1, z=0.7 ),
            aspectmode = 'manual'
        )
    )

    fig = dict(data=data, layout=layout)

    # IPython notebook
    # py.iplot(fig, filename='pandas-3d-surface', height=700, validate=False)

    #url = py.iplot(fig, filename='3d-surface-depth-plot3')

create3DPlot('/home/jmoorman9/Downloads/totalHeightChange3.npy')
