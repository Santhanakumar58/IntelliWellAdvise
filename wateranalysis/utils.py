import pandas as pd
import numpy as np
import os, math 
import base64
from io import BytesIO
import matplotlib.pyplot as plt 
import imageio
 

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def coordinates(Ca, Mg, Cl,SO4, Label):
    xcation = 40+360 - (Ca+Mg/2)*3.6
    ycation = 40+(math.sqrt(3) * Mg/2)*3.6
    xanion = 40+360 +100 + (Cl+SO4/2)*3.6
    yanion = 40+(SO4*math.sqrt(3)/2)*3.6
    xdiam = 0.5*(xcation + xanion +(yanion-ycation)/math.sqrt(3))
    ydiam = 0.5*(yanion + ycation + math.sqrt(3) * (xanion-xcation))    
    c= np.random.rand(3,1).ravel()
    listgraph=[]
    listgraph.append(plt.scatter(xcation, ycation, zorder=1, color=c, s=60, edgecolors ='#4b4b6b',label=Label))
    listgraph.append(plt.scatter(xanion, yanion, zorder=1, color=c, s=60, edgecolors ='#6b4b5b'))
    listgraph.append(plt.scatter(xdiam, ydiam, zorder=1, color=c, s=60, edgecolors ='#9b4b4b'))
    
    return listgraph




def get_plot(df):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,6))
    img = imageio.v2.imread(r"C:\Users\santh\Downloads\Piperdiagram.png")
    plt.imshow(np.flipud(img), zorder=0)
    for index, row in df.iterrows():
        coordinates(row['Ca_norm'], row['Mg_norm'],row['Cl_norm'], row['SO4_norm'], row['Well_Name'])    
    plt.ylim(0,830)
    plt.xlim(0,900)
    plt.axis('off')
    plt.legend(loc='upper right', prop={'size':10}, frameon = False, scatterpoints=1)
    plt.title("Piper Diagram")

    graph = get_graph()
    return graph


def stiff_diagram(Nak, Ca, Mg, SO4, HCO3, Cl):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,6))
    x=[-Nak, -Ca, -Mg, SO4, HCO3, Cl, -Nak]
    y = [6,4,2, 2, 4, 6, 6]     
    plt.plot(x, y)
    maxx=max(x)+50
    plt.text(-Nak-15, 5.75, 'Na + K', va='bottom', ha='left')
    plt.text(-Ca , 4.5, 'Ca', va='center', ha='left')
    plt.text(-Mg, 2.5, 'Mg', va='center', ha='left')
    plt.text(SO4, 2.5, 'SO4', va='center', ha='right')
    plt.text(HCO3, 4.5, 'HCO3 +CO3', va='center', ha='right')
    plt.text(Cl, 6, 'Cl', va='bottom', ha='right')
    plt.ylim(0,8)
    gradient = np.linspace(0, 1, 100).reshape(1, -1)
    plt.imshow(gradient , extent=[-maxx, maxx, 0,8], aspect='auto', cmap='autumn')  
    plt.title("Stiff Diagram for the latest Water Analysis")
    plt.fill(x, y, "g")
    graph = get_graph()
    return graph
