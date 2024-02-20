from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from matplotlib.ticker import NullFormatter
from matplotlib.dates import YearLocator, DateFormatter
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

def get_plot(x,y,z, y1,y2,y3,y4):
    plt.switch_backend('AGG')
    plt.figure(figsize=(20,20))
    figure, axis = plt.subplots(2, 2)
    figure.set_size_inches(12, 8)
    axis[0,1].plot(x, y, color='red', label = 'Gas Rate')    
    axis[0,1].set_title("Gas Rate")
    axis[0,1].set_xlabel('Date')
    axis[0,1].set_ylabel('Gas Rate 1000 scf/day')     
    axis[0,1].xaxis.set_major_locator(YearLocator())
    axis[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    for label in axis[0,1].get_xticklabels():
        label.set_rotation(90)    

    axis[0,0].plot(x, y1, color='green', label = 'oil')
    axis[0,0].plot(x, y2, color='cyan', label = 'water')
    axis[0,0].plot(x, y3, color='red', label = 'liquid')
    axis[0,0].set_title("Liquid Rates") 
    axis[0,0].set_xlabel('Date')
    axis[0,0].set_ylabel('Liquid Rate Bbls/day')    
    axis[0,0].legend()  
    axis[0,0].xaxis.set_major_locator(YearLocator())
    axis[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    for label in axis[0,0].get_xticklabels():
        label.set_rotation(90) 

    axis[1,1].plot(x, z, color='red', label = 'GOR')   
    axis[1,1].set_title("Gas Oil Ratio") 
    axis[1,1].set_xlabel('Date')
    axis[1,1].set_ylabel('GOR scf/bbl')   
    axis[1,1].xaxis.set_major_locator(YearLocator())
    axis[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    for label in axis[1,1].get_xticklabels():
        label.set_rotation(90) 
    
    axis[1,0].plot(x, y4, color='green', label = 'Water Cut %')   
    axis[1,0].set_title("Water Cut") 
    axis[1,0].set_xlabel('Date')
    axis[1,0].set_ylabel('Water Cut %')     
    axis[1,0].xaxis.set_major_locator(YearLocator())
    axis[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    for label in axis[1,0].get_xticklabels():
        label.set_rotation(90) 

    figure.tight_layout()
    axis[0,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[0,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[1,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[1,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph



    