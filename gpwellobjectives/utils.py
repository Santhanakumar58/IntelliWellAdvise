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


def get_plot1(x,y,y1):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,6))
    fig, ax = plt.subplots()    
    ax.plot(x, y,color="red", marker="")   
    ax.set_xlabel("year", fontsize = 10)    
    ax.set_ylabel("Gas Rate mmscfd",color="red",fontsize=10)
    ax2=ax.twinx() 
    ax2.plot(x, y1,color="green",marker="")
    ax2.set_ylabel("Condensate Rate bbls/day",color="green",fontsize=10)
    ax.set_title("Gas and Condensate Production Plot", fontsize = 12)   
    fig.tight_layout()
    graph = get_graph()
    return graph


def get_plot2(x,z,y2):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,6))
    fig, ax = plt.subplots()    
    ax.plot(x, z,color="green", marker="")   
    ax.set_xlabel("year", fontsize = 10)    
    ax.set_ylabel("Condensate Production bbls/mmscf",color="green",fontsize=10)
    ax2=ax.twinx() 
    ax2.plot(x, y2,color="cyan",marker="")
    ax2.set_ylabel("Water Production bbls/d",color="cyan",fontsize=10)
    ax.set_title("Condensate and Water Production Plot", fontsize = 12)   
    fig.tight_layout()
    graph = get_graph()
    return graph


## Not Used


def get_plot(x,y,z, y1,y2,y3,y4):
    plt.switch_backend('AGG')
    plt.figure(figsize=(20,20))
    figure, axis = plt.subplots(2, 1)
    figure.set_size_inches(12, 8)
    axis[0,0].plot(x, y, color='red', label = 'Gas Rate')    
    axis[0,0].set_title("Gas Rate")
    axis[0,0].set_xlabel('Date')
    axis[0,0].set_ylabel('Gas Rate mmscf/day')     
    axis[0,0].xaxis.set_major_locator(YearLocator())
    axis[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    for label in axis[0,0].get_xticklabels():
        label.set_rotation(90)   

    #axis[0,1].plot(x, y1, color='green', label = 'Condensate')
    #axis[0,1].plot(x, y2, color='cyan', label = 'water')
    #axis[0,1].plot(x, y3, color='red', label = 'Condensate + Water')
    #axis[0,1].set_title("Liquid Rates") 
    #axis[0,1].set_xlabel('Date')
    #axis[0,1].set_ylabel('Rate Bbls/day')    
    #axis[0,1].legend()  
    #axis[0,1].xaxis.set_major_locator(YearLocator())
    #axis[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    #for label in axis[0,1].get_xticklabels():
    #    label.set_rotation(90) 

    axis[1,1].plot(x, z, color='red', label = 'CGR')   
    axis[1,1].set_title("Condensate Gas Ratio") 
    axis[1,1].set_xlabel('Date')
    axis[1,1].set_ylabel('CGR bbl/mmscf')   
    axis[1,1].xaxis.set_major_locator(YearLocator())
    axis[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    for label in axis[1,1].get_xticklabels():
        label.set_rotation(90) 
    
    # axis[1,0].plot(x, y4, color='green', label = 'Water Cut %')   
    # axis[1,0].set_title("Water Cut") 
    # axis[1,0].set_xlabel('Date')
    # axis[1,0].set_ylabel('Water Cut %')     
    # axis[1,0].xaxis.set_major_locator(YearLocator())
    # axis[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    # for label in axis[1,0].get_xticklabels():
        # label.set_rotation(90) 

    figure.tight_layout()
    axis[0,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    # axis[0,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[1,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    # [1,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def get_plot22(x,y1,y2,y3):
    #plt.switch_backend('AGG')
    plt.figure(figsize=(10,6))
    #plt.style.use('_mpl-gallery')
    y = np.vstack([y2,y1,y3])
    # plot
    fig, ax = plt.subplots()   
    ax.scatter(x, y2, color="cyan") 
    ax.plot(x, y1, color="red") 
    ax.plot(x, y3, color="green")    
    ax.legend(loc='upper left', reverse=True)
    ax.set_title('Liquid Production Plot', fontsize=10)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Liquids rate bbls/d', fontsize=10)  
   
    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    #fig.tight_layout()
    graph = get_graph()
    return graph

def get_plot3(x,y,z,y1,y2,y3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(15,10))

    fig, ax = plt.subplots()    
    ax.plot(x, z,color="green", marker="")   
    ax.set_xlabel("year", fontsize = 10)    
    ax.set_ylabel("Condensate Production bbls/mmscf",color="green",fontsize=10)
    ax2=ax.twinx() 
    ax2.plot(x, y2,color="cyan",marker="")
    ax2.set_ylabel("Water Production bbls/d",color="cyan",fontsize=10)
    ax.set_title("Condensate and Water Production Plot", fontsize = 12)  


    # plt.subplot(2,1,1)
    # plt.plot(x,y, color="red")
    # plt.title("Gas Production Rate", fontsize=14)
    # plt.xlabel("Year", fontsize=14)
    # plt.ylabel("Gas Rate mmscfd", fontsize=14)

    plt.subplot(2,1,2)
    plt.plot(x, y1, color='green', label = 'Condensate')
    plt.plot(x, y2, color='cyan', label = 'water')
    plt.plot(x, y3, color='red', label = 'Condensate + Water')
    plt.title("Liquid Production Rates")
    plt.xlabel("Year")
    plt.ylabel("Liquid Rate bbls/d")

    graph = get_graph()
    return graph