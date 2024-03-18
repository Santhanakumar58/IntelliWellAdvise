import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np



def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_fanning(NRE, F):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(12, 4)) 
    plt.plot(NRE, F, color = "green")
    plt.xlabel('Reynolds No')
    plt.ylabel('Friction Factor')
    plt.legend(loc="upper right")    
    plt.title("Fanning Friction Factor - Chen")
    plt.tight_layout()
    graph = get_graph()
    return graph

# Plotting the Beggs and Brill and Hagedorn and Brown  plots
def get_plot(pipline_range, pressures, pressures1, holdups, holdups1):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(12, 4))    
    plt.subplot(1,2,2)   

    plt.subplot(1,2,1)
    plt.plot(pipline_range, pressures,  label='BB', color = "r")
    plt.plot(pipline_range, pressures1,  label='HB', color = "green")
    plt.xlabel('Length')
    plt.ylabel('Pressure')
    plt.legend(loc="upper right")    
    plt.title("Tubing Performance Curve")

    plt.subplot(1,2,2)
    plt.plot(pipline_range, holdups,  label='BB', color = "r")
    plt.plot(pipline_range, holdups1,  label='HB', color = "green")
    plt.xlabel('Length')
    plt.ylabel('Liquid Holdup')
    plt.legend(loc="upper right")    
    plt.title("Holdup Curve")
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_Dummy_plot(PressList,DepthList ):
    plt.title("Tubing Performance Curve")
    plt.plot(PressList, DepthList)
    plt.ylabel('Depth')
    plt.xlabel('Pressure')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    graph = get_graph()
    return graph

