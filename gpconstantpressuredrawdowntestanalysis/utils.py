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

