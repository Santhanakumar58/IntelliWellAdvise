from turtle import color
import matplotlib.pyplot  as plt
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

def get_pieplot(y, label):
    plt.switch_backend('AGG')    
    plt.rcParams["figure.figsize"] = [6, 6]
    plt.rcParams["figure.autolayout"] = True    
    plt.pie(y, labels = label, startangle =90, shadow = True, radius =1, autopct = '%1.1f%%') 
    plt.title('Drilling Operation Time Distribution')   
    graph = get_graph()
    return graph