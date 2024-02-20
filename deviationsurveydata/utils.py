from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import mpl_toolkits
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,z): 
    plt.switch_backend('AGG')  
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')    
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    ax.zaxis.label.set_color('black')
    ax.tick_params(axis='x',colors='blue')
    ax.tick_params(axis='y',colors='blue')
    ax.tick_params(axis='z',colors='blue')
    ax.set_xlabel('North')
    ax.set_ylabel('East')
    ax.set_zlabel('TVD [ft]')
    ax.plot3D(x, y, z, color='red')
    ax.set_title('Well Trajectory' , color = "blue")
    
  
    #ax.w_xaxis.set_pane_color((0.3, 0.3, 0.3, 1.0))
    #ax.w_yaxis.set_pane_color((0.3, 0.3, 0.3, 1.0))
    #ax.w_zaxis.set_pane_color((0.3, 0.3, 0.3, 1.0))
  
    
    plt.tight_layout()   
    graph = get_graph()
    return graph

