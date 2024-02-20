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

def get_plot(x,y,y1,y2): 
    plt.switch_backend('AGG')    
    plt.rcParams["figure.figsize"] = [7.50, 4.50]
    plt.rcParams["figure.autolayout"] = True    
    ind = np.arange(len(x)) # the x locations for the groups
    width = 0.25 # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width, y, width, label='Liquid Gain', color='r')
    rects2 = ax.bar(ind , y1, width,  label='Oil Gain', color='g')
    rects3 = ax.bar(ind + width , y2, width, label='Gas Gain', color='orange')    
    ax.set_ylabel('Liquid Rates (bbls/d) / Gas Rates (1000 scf/d)')
    ax.set_title('Liquid, Oil and Gas Gains of Slickline Interventions')
    ax.set_xticks(ind,x)   
    ax.legend()    
    autolabel(ax,rects1, "center")
    autolabel(ax, rects2, "center")
    autolabel(ax, rects3, "center")    
    graph = get_graph()
    return graph

def autolabel(ax, rects, xpos='center'):
   ha = {'center': 'center', 'right': 'left', 'left': 'right'}
   offset = {'center': 0, 'right': 1, 'left': -1}
   for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(offset[xpos]*3, 3), # use 3 points offset
        textcoords="offset points", # in both directions
        ha=ha[xpos], va='bottom')

def get_plot1(dat,x1,x2,x3,y1,y2,y3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))      
    labels =[x1,x2,x3]
    values=[y1,y2,y3]
    ind=np.arange(len(values))
    fig, ax = plt.subplots()    
    pp= ax.bar(labels, values, color=['red','green', 'orange'])    
    for p in pp:
        height = p.get_height()
        ax.annotate('{}'.format(height),
        xy=(p.get_x() + p.get_width() / 2, height),
        xytext=(0, 3), # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom')
    plt.title(f"Gains of Slickline Intervention dated {dat}")  
    plt.ylabel('Rate Bbls/day / Gas Rate 1000 scf/day') 
    plt.legend(loc='upper right')
    plt.tight_layout()     
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph