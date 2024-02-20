from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import numpy as np
from turtle import color
from matplotlib import gridspec






def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,3))
    plt.title("Pressure Vs Y Function")  
    m, b = np.polyfit(x, y, 1)
    plt.axline(xy1=(0, b), slope=m, label=f'$y = {m:.5f}x {b:+.1f}$')     
    y1=[]
    plt.scatter(x,y, color='red')
    for i in range(len(x)):
        y1.append(m*x[i] + b)
    plt.plot(x,y1, color='g')
    plt.xticks(rotation=0)
    plt.xlabel('Pressure')
    plt.ylabel('Y Function') 
    plt.legend()
    plt.tight_layout()
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
   
    graph = get_graph()
    return graph


def get_Multiplot(x,y,x1,y1, Pb):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,5))
    plt.subplot(1, 2, 1)
    m, b = np.polyfit(x, y, 1)
    m= round(m,5)
    b= round(b,5)
    plt.axline(xy1=(0, b), slope=m, label=f'$y = {m:.5f}x {b:+.1f}$')     
    y01=[]
    for i in range(len(x)):
        y01.append(m*x[i] + b)
    plt.subplot(1,2,1)    
    plt.scatter(x,y, color='g')
    plt.plot(x, y01, color='b')
    plt.tight_layout(pad=5)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title(" Y Function", color='b', fontname="cursive", fontweight="bold")      
    plt.xticks( color='g') 
    plt.yticks( color='g')       
    plt.xlabel('Pressure', color='g',fontweight="bold")       
    plt.ylabel('Y Function', color='g',fontweight="bold")  
    plt.grid(color = 'brown', linestyle = '--', linewidth = 0.5)  
    plt.text(100,2, f'$Y = {m}x+ {b}$', fontsize=10, color="r")
     
    
    plt.subplot(1,2,2)    
    plt.tight_layout(pad=5)
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    plt.title("Relative volume showing Pb", color='b', fontname="cursive", fontweight="bold")      
    plt.xticks( color='g') 
    plt.yticks( color='g')       
    plt.xlabel('Pressure', color='g',fontweight="bold")       
    plt.ylabel('Relative Volume', color='g',fontweight="bold") 
    
    m, b = np.polyfit(x1, y1,1)
    m= round(m,5)
    b= round(b,5)
    plt.axline(xy1=(0, b), slope=m, label=f'$y = {m:.5f}x {b:+.1f}$')     
    y01=[]
    x01=[]
    for i in range(len(y1)):
        if y1[i] <=1.0:
            y01.append(m*x1[i] + b)
            x01.append(x1[i])
    m, b = np.polyfit(x01, y01, 1)
    m= round(m,5)
    b= round(b,5)
    plt.axline(xy1=(0, b), slope=m, label=f'$y = {m:.5f}x {b:+.1f}$')   
    plt.scatter(x01, y01, color='b', s=15)
    y02=[]
    for i in range(len(x01)):
        y02.append(m*x01[i] + b)
    plt.plot(x01, y02, color ="r" )
    print(y02)
    plt.text(Pb+500,0.998, "%d" "(psi)"%Pb, ha="center", color="r")    
    plt.text(1000,0.97, f'$Y = {m}x+ {b}$', fontsize=10, color="r")
    
   # figure, axis = plt.subplots(1,2)    
   # fig = plt.figure()
   # fig.set_figheight(7)
   # fig.set_figwidth(13)
   # spec = gridspec.GridSpec(ncols=2, nrows=2,
   #                      width_ratios=[1, 1], wspace=0.5,
   #                      hspace=0.5, height_ratios=[1, 1])
   # ax0 = fig.add_subplot(spec[0])
   # m, b = np.polyfit(x, y, 1)
   # ax0.axline(xy1=(0, b), slope=m, label=f'$y = {m:.5f}x {b:+.1f}$')     
   # y01=[]
   # for i in range(len(x)):
   #     y01.append(m*x[i] + b)
   # plt.plot(x,y, color='g')
   # ax0.scatter(x, y01, color='b')
   # ax0.plot(x, y01, color='black')
   # plt.tight_layout()
   # plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
   # plt.title(" Y Function", color='b', fontname="cursive", fontweight="bold")      
   # plt.xticks( color='g') 
   # plt.yticks( color='g')       
   # plt.xlabel('Pressure', color='g',fontweight="bold")       
   # plt.ylabel('Y Function', color='g',fontweight="bold")       
   #
   # gradient = np.linspace(0, 1, 100).reshape(1, -1)
   # plt.imshow(gradient , extent=[0,10000, 0,5], aspect='auto', cmap='autumn')  
   # 
   # ax1 = fig.add_subplot(spec[1])
   # ax1.scatter(x1, y1, color='b', s=15)
   # ax1.scatter(Pb, 1, color ="g", s=20, label="Pb" )
   # plt.tight_layout()
   # plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
   # plt.title("Relative Volume plot showing Pb", color='b', fontname="cursive", fontweight="bold")            
   # plt.xticks( color='g') 
   # plt.yticks( color='g')     
   # plt.xlabel('Pressure', color='g', fontweight="bold")     
   # plt.ylabel('Relative Volume', color='g', fontweight="bold")     
   # gradient = np.linspace(0, 1, 100).reshape(1, -1)    
   # ax1.text(Pb,1+0.5, "%d" "(psi)"%Pb, ha="center")
   # plt.imshow(gradient , extent=[0, 10000, 0, 4.5], aspect='auto', cmap='autumn')   
   #    
   # plt.tight_layout()
    plt.grid(color = 'brown', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph
