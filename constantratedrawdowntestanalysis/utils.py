from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
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

def get_plot(t,p,m1,c1,m2,c2,s,k,re, your_guess):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))    
    # normal plot BHFP vs time
    plt.subplot(2,1,1)
    plt.plot(t, p, '.', color='blue')

    ## plot the regression line
    y_fit = m2 * t + c2
    plt.plot(t, y_fit, color='red', linewidth=1)

    ## plot the separate MTR and LTR region
    plt.axvspan(0, t[your_guess], color='orange', alpha=0.1)
    plt.axvspan(t[your_guess], max(t), color='green', alpha=0.1)

    plt.title('Constant Rate Drawdown Test Plot (BHFP vs Time)', size=12, pad=10, color="blue")
    plt.xlabel('Time (hours)', size=10); plt.ylabel('Pressure (psia)', size=10)
    plt.xlim(0,max(t))

    # output all results to plot
    labels2 = []
    labels2.append("End Time of MTR = {} hours".format(np.round(t[your_guess], 3)))
    handles2 = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", 
                                  lw=0, alpha=0)] * 1                                    

    plt.legend(handles2, labels2, loc='best', fontsize='medium', 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0)
    plt.grid(True, which='both', color='black', linewidth=0.1)

  # semilog plot BHFP vs time
    plt.subplot(2,1,2)
    plt.semilogx(t, p, '.', color='blue')

  ## plot the regression line
    y_fit = m1 * np.log(t) + c1
    plt.plot(t, y_fit, color='red', linewidth=1)

  ## plot the separate MTR and LTR region
    plt.axvspan(0, t[your_guess], color='orange', alpha=0.1)
    plt.axvspan(t[your_guess], max(t), color='green', alpha=0.1)  

    plt.title('Semilog Plot of Constant Rate Drawdown Test(BHFP vs Time)', size=12, pad=10, color="blue")
    plt.xlabel('Time (hours)', size=12); plt.ylabel('Pressure (psia)', size=12)
    plt.xlim(xmax=max(t))

  # output all results into the plot
    labels1 = []
    labels1.append("Calc. Permeability = {} md".format(np.round(k, 3)))
    labels1.append("Calc. Skin Factor = {}".format(np.round(s, 3)))
    labels1.append("Calc. Reservoir Size = {} ft".format(np.round(re, 3)))  
    handles1 = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", 
                                  lw=0, alpha=0)] * 3 

    plt.legend(handles1, labels1, loc='best', fontsize='large', 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0) 
  
    plt.grid(True, which='both', color='black', linewidth=0.1)
    plt.tight_layout() 
    graph = get_graph()
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


def constant_Pressure_plot(t, q, pwf, pi, Bo, mu_oil, h, poro, ct, rw, k,s,m,c):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,8))  
    labels1 = []
    labels1.append("Calc. Permeability = {} md".format(np.round(k, 3)))
    labels1.append("Calc. Skin Factor = {}".format(np.round(s, 3)))
    handles1 = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white",lw=0, alpha=0)] * 2

    # normal plot of q vs t
    plt.subplot(2,1,1)
    plt.plot(t, q, '.', color='blue')
    plt.title('Constant Pressure Test Rate vs Time', size=12, pad=10, color="blue")
    plt.xlabel('Time (hour)', size=12); plt.ylabel(r'Rate (STB/D)', size=12)  
    plt.xlim(0, max(t))
    plt.axvspan(0, max(t)+100, color='orange', alpha=0.1)

    plt.grid(True, which='both', color='blue', linewidth=0.1)

    # plot semilog plot of 1/q vs t
    plt.subplot(2,1,2)
    plt.semilogx(t, 1/q, '.', color='blue')
    plt.title('Semilog Plot of Reciprocal Rate vs Time', size=12, pad=10, color="blue")
    plt.xlabel('Time (hour)', size=12); plt.ylabel(r'$\frac{1}{q}$ (D/STB)', size=12)
    plt.xlim(xmin=1)
    plt.axvspan(0, max(t)+100, color='green', alpha=0.1)
    #plt.axvspan(t[your_guess], max(t), color='green', alpha=0.3)

    # plot regression line
    y_fit = m * np.log10(t) + c
    plt.plot(t, y_fit, color='red', linewidth=0.7)

    plt.legend(handles1, labels1, loc='best', fontsize='medium', 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0) 

    plt.grid(True, which='both', color='blue', linewidth=0.1)

    plt.tight_layout()
    graph = get_graph()
    return graph

