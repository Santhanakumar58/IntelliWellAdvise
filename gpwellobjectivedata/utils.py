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

def get_plot1(x,y,y1):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    fig, ax = plt.subplots()    
    ax.plot(x, y,color="red", marker="")   
    ax.set_xlabel("year", fontsize = 6)    
    ax.set_ylabel("Gas Rate mmscfd",color="red",fontsize=6)
    ax2=ax.twinx() 
    ax2.plot(x, y1,color="green",marker="")
    ax2.set_ylabel("Condensate Rate bbls/day",color="green",fontsize=6)
    ax.set_title("Gas and Condensate Production Plot", fontsize = 8)  
    fig.tight_layout()
    graph = get_graph()
    return graph


def get_plot2(x,z,y2):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    fig, ax = plt.subplots()    
    ax.plot(x, z,color="green", marker="")   
    ax.set_xlabel("year", fontsize = 6)    
    ax.set_ylabel("Condensate Production bbls/mmscf",color="green",fontsize=6)
    ax2=ax.twinx() 
    ax2.plot(x, y2,color="cyan",marker="")
    ax2.set_ylabel("Water Production bbls/d",color="cyan",fontsize=6)
    ax.set_title("Condensate and Water Production Plot", fontsize = 8)   
    fig.tight_layout()
    graph = get_graph()
    return graph




    
