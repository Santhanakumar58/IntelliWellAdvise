from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.patches as mpl_patches 

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def multiratetestplot(t,p, x,y, c, m, k,s, time_arr):    
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))      
      # output calculated results to plot
    labels1 = []
    labels1.append("Calc. Permeability = {} md".format(np.round(k, 3)))
    labels1.append("Calc. Skin Factor = {}".format(np.round(s, 3)))
    handles1 = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", 
                                  lw=0, alpha=0)] * 2

    # " Plot Analysis "

     
    plt.subplot(2,1,1)
    plt.plot(time_arr, p, '.-', color='blue')
    plt.xlim(0, max(t))
    plt.title('Multi-Rate Test Pressure Profile', size=12, pad=10, color="blue")
    plt.xlabel(r'Time (hours)', size=10); plt.ylabel(r'Pressure (psi)', size=10)
    plt.grid(True, which='both', color='black', linewidth=0.1)
    plt.axvspan(0, max(t)+100, color='orange', alpha=0.1)

    plt.subplot(2,1,2)
    plt.plot(x, y, '.', color='blue')
    plt.xlim(0, max(x))
    plt.title('Drawdown Plot for Multi-Rate Flow', size=12, pad=10, color="blue")
    plt.xlabel(r'$F_p$', size=10); plt.ylabel(r'$\frac{p_i-p_{wf}}{q_n}$ (psi-D/STB)', size=10)
    plt.axvspan(0, max(t)+100, color='green', alpha=0.1)

    # plot regression line
    y_fit = m * np.array(x) + c
    plt.plot(x, y_fit, color='red', linewidth=0.5)

    plt.legend(handles1, labels1, loc='best', fontsize='medium', 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0) 
    plt.grid(True, which='both', color='black', linewidth=0.1)
    plt.tight_layout()    
    graph = get_graph()
    return graph
