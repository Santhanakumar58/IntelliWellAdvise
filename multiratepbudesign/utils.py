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

def multirate_constant_rate_design_plot(t_finite_acting,t,q, t_end, pwf):    
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8)) 
    #plot well rate and flowing pressure profile
    #plt.figure(figsize=(17,5))
    ## output the finite-acting time into the plot
    labels = []
    labels.append("Time @ Finite-acting = {} hours".format(np.round(t_finite_acting, 2)))
    handles = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white",lw=0, alpha=0)] * 1
    ## plot rate
    plt.subplot(2,1,1)
    plt.step(t, q, color='blue')
    plt.title('Well Production Rate Profile', size=12, pad=15)
    plt.xlim(0, t_end)
    plt.ylim(ymax=max(q)+200)
    plt.xlabel('Time (hours)'); plt.ylabel('Rate (STB/D)')
    plt.legend(handles, labels, loc='upper right', fontsize=12, fancybox=True, framealpha=0.7,handlelength=0, handletextpad=0) 
    ## plot BHFP
    plt.subplot(2,1,2)
    #t = np.arange(len(pwf))
    plt.plot(t, pwf, color='red')
    plt.title('Well Bottomhole Flowing Pressure Profile', size=12, pad=15)
    plt.xlim(0, t_end)
    plt.xlabel('Time (hours)'); plt.ylabel('BHFP (psia)')
    #t.grid(True, which='both', color='black', linewidth=0.1)
    plt.tight_layout()    
    graph = get_graph()
    return graph