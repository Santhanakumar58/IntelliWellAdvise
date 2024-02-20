from cProfile import label
from decimal import *
import math
from re import T
from tkinter import Label
from turtle import color
from matplotlib import gridspec
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import numpy as np
import seaborn as sns
import plotly.express as px
 


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot():
    plt.switch_backend('AGG')
    plt.figure(figsize=(9,9))
    # Define the cation and anion names and concentrations (in meq/L)
    cations = ['Na', 'K', 'Mg', 'Ca']
    cat_conc = [10, 4, 3, 1]
    anions = ['HCO3', 'SO4', 'Cl']
    an_conc = [10, 2, 8]

    # Calculate the total cation and anion concentrations
    total_cat_conc = np.sum(cat_conc)
    total_an_conc = np.sum(an_conc)

    # Calculate the cation and anion proportions
    cat_prop = [x / total_cat_conc for x in cat_conc]
    an_prop = [x / total_an_conc for x in an_conc]
    # Calculate the positions of the cation and anion triangles
    cat_x = [cat_prop[0], 0.5 * (cat_prop[0] + cat_prop[1]), cat_prop[1], cat_prop[2] + 0.5 * cat_prop[3], 1 - cat_prop[3], cat_prop[2]]
    cat_y = [0, 0.5 * np.sqrt(3) * cat_prop[1], np.sqrt(3) * cat_prop[1], np.sqrt(3) * (cat_prop[0] + cat_prop[1] + cat_prop[2]), 0.5 * np.sqrt(3) * cat_prop[3], 0]

    an_x = [an_prop[0], 1 - an_prop[1] - an_prop[2], an_prop[1]]
    an_y = [0, 0, np.sqrt(3) * an_prop[1]]

    # Create the plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    ax.plot(cat_x, cat_y, 'k-', linewidth=2)
    ax.plot(an_x, an_y, 'k--', linewidth=2)

    #ax.scatter(cat_x, cat_y, s=cat_conc, color='r')
    ax.scatter(an_x, an_y, s=an_conc, color='b')

    # Label the plot
    for i, cat in enumerate(cations):
        ax.text(cat_x[i], cat_y[i], cat, ha='center', va='center', fontsize=12)

    for i, an in enumerate(anions):
        ax.text(an_x[i], an_y[i], an, ha='center', va='center', fontsize=12)

    ax.text(0.5, 1.1, 'Piper Diagram', ha='center', va='center', fontsize=16)
    ax.text(0.5, -0.1, f'Total cations: {total_cat_conc} meq/L, Total anions: {total_an_conc} meq/L', ha='center', va='center', fontsize=12)

    graph = get_graph()
    return graph





