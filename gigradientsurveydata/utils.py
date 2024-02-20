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

def get_plot(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))
    plt.title("Gradient Survey Plot")
    plt.plot(x,y, color='blue', label = 'Pressure)')
    plt.plot(z,y, color='red', label = 'Temperature')
    # plt.fill_between(x, y, label = 'Gas Rate')
    # plt.fill_between(x, z, label = 'Gas Oil Ratio')
    plt.xticks(rotation=45)
    plt.xlabel('Pressure / Temperature')
    plt.ylabel('Gauge Depth (ft)') 
    plt.legend()
    plt.tight_layout()
    plt.gca().invert_yaxis()   
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph
