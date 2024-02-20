from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,z, y1,y2,y3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,3))
    figure, axis = plt.subplots(2, 1)
    axis[0].plot(x, y, color='red', label = 'Gas Rate')
    axis[0].plot(x, z, color='blue', label = 'GOR')
    axis[0].set_title("Gas Plot")    
    axis[0].set_xlabel('Date')
    axis[0].set_ylabel('Gas Rate scf/day') 
    axis[0].legend() 
    axis[1].plot(x, y1, color='green', label = 'oil')
    axis[1].plot(x, y2, color='cyan', label = 'water')
    axis[1].plot(x, y3, color='red', label = 'liquid')
    axis[1].set_title("Liquid Plot")   
    axis[1].set_xlabel('Date')
    axis[1].set_ylabel('Liquid Rate Bbls/day') 
    axis[1].legend()
    figure.tight_layout()
    axis[0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

    
