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

def get_porosity_density_cross_plot(well):
    plt.switch_backend('AGG')
    plt.figure(figsize=(9,4)) 
    plt.scatter(well["NPHI"], well["RHOB"], c=well["GR"],cmap="YlOrRd_r")
    plt.xlabel("NPHI (fraction)")
    plt.ylabel("RHOB (g/cc)")
    plt.title ("Porosity - Density Cross Plot")
    plt.colorbar(label="GR", orientation="vertical")
    plt.tight_layout()       
    graph = get_graph()
    return graph
    
def get_other_cross_plots(well):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,8)) 
    fig, ax = plt.subplots(figsize=(10,10))
    plt.title("Other Cross Plots", color="blue")

    ax1 = plt.subplot2grid((2,2), (0,0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((2,2), (0,1), rowspan=1, colspan=1)
    ax3 = plt.subplot2grid((2,2), (1,0), rowspan=1, colspan=1)
    ax4 = plt.subplot2grid((2,2), (1,1), rowspan=1, colspan=1)

    ax1.scatter(x= "GR", y= "RHOB", data= well, color="r", alpha= 0.2)
    ax1.set_ylim(3, 1.8)
    ax1.set_ylabel("RHOB (g/cc)")
    ax1.set_xlabel("GR (API)")
    ax1.set_title ("GR - Density Cross Plot", color="blue")


    ax2.scatter(x= "GR", y= "NPHI", data= well, color="g", alpha= 0.2)
    ax1.set_ylim(3, 1.8)
    ax2.set_ylabel("NPHI (fraction)")
    ax2.set_xlabel("GR (API)")
    ax2.set_title ("GR - NPHI Cross Plot", color="blue")

    ax3.scatter(x= "DT", y= "RHOB", data= well, color="b", alpha= 0.2)
    ax3.set_ylim(3, 1.8)
    ax3.set_ylabel("RHOB (g/cc)")
    ax3.set_xlabel("DT (us/ft)")
    ax3.set_title ("DT - RHOB Cross Plot", color="blue")

    ax4.scatter(x= "GR", y= "DT", data= well,color="orange", alpha= 0.2)
    ax4.set_ylabel("DT (us/ft)")
    ax4.set_xlabel("GR (API)") 
    ax4.set_title ("GR - DT Cross Plot", color="blue")
    plt.tight_layout()       
    graph = get_graph()
    return graph
    


def get_logs_calculated(well, max_depth, min_depth, well_nan, cols):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(10,15))
    #Set up the plot axes
    ax1 = plt.subplot2grid((1,7), (0,0), rowspan=1, colspan = 1)
    ax2 = plt.subplot2grid((1,7), (0,1), rowspan=1, colspan = 1)
    ax3 = plt.subplot2grid((1,7), (0,2), rowspan=1, colspan = 1)
    ax4 = plt.subplot2grid((1,7), (0,3), rowspan=1, colspan = 1)
    ax5 = ax3.twiny() #Twins the y-axis for the density track with the neutron track
    ax6 = plt.subplot2grid((1,7), (0,4), rowspan=1, colspan = 1)
    ax7 = ax6.twiny()
    ax8 = plt.subplot2grid((1,7), (0,5), rowspan=1, colspan = 1)
    ax9 = plt.subplot2grid((1,7), (0,6), rowspan=1, colspan = 1)
    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)
    # Gamma Ray track
    ax1.plot(well["GR"], well.index, color = "green")
    ax1.set_xlabel("Gamma")
    ax1.xaxis.label.set_color("green")
    ax1.set_xlim(0, 200)
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="green")
    ax1.spines["top"].set_edgecolor("green")
    ax1.title.set_color('green')
    ax1.set_xticks([0, 50, 100, 150, 200])
    # Resistivity track
    if "LLD" in cols or "RT" in cols:
        ax2.plot(well["LLD"],well.index, color = "red", linewidth=0.5)
        ax2.set_xlabel("Resistivity")
        ax2.set_xlim(0.2, 2000)
        ax2.xaxis.label.set_color("red")
        ax2.tick_params(axis='x', colors="red")
        ax2.spines["top"].set_edgecolor("red")
        ax2.set_xticks([0.1, 1, 10, 100, 1000])
        ax2.semilogx()
    # Density track
    if "RHOB" in cols:
        ax3.plot(well["RHOB"], well.index,color = "red")
        ax3.set_xlabel("Density")
        ax3.set_xlim(1.95, 2.95)
        ax3.xaxis.label.set_color("red")
        ax3.tick_params(axis='x', colors="red")
        ax3.spines["top"].set_edgecolor("red")
        ax3.set_xticks([1.95, 2.45, 2.95])
    # Sonic track
    if "DT" in cols:
        ax4.plot(well["DT"],well.index,  color = "purple")
        ax4.set_xlabel("Sonic")
        ax4.set_xlim(140, 40)
        ax4.xaxis.label.set_color("purple")
        ax4.tick_params(axis='x', colors="purple")
        ax4.spines["top"].set_edgecolor("purple")
    # Neutron track placed ontop of density track
    if "NPHI" in cols:
        ax5.plot(well["NPHI"], well.index,color = "blue")
        ax5.set_xlabel('Neutron')
        ax5.xaxis.label.set_color("blue")
        ax5.set_xlim(0.45, -0.15)
        ax5.set_ylim(max_depth, min_depth)
        ax5.tick_params(axis='x', colors="blue")
        ax5.spines["top"].set_position(("axes", 1.08))
        ax5.spines["top"].set_visible(True)
        ax5.spines["top"].set_edgecolor("blue")
        ax5.set_xticks([0.45,  0.15, -0.15])
    # Porosity track
    if "RHOB" in cols :
        ax6.plot(well["PHI"], well.index, color = "black")
        ax6.set_xlabel("Total PHI")
        ax6.set_xlim(0.5, 0)
        ax6.xaxis.label.set_color("black")
        ax6.tick_params(axis='x', colors="black")
        ax6.spines["top"].set_edgecolor("black")
        ax6.set_xticks([0, 0.25, 0.5])
    # Porosity track
    if "NPHI" and "GR" in cols:
        ax7.plot(well["PHIECALC"], well.index, color = "blue")
        ax7.set_xlabel("Effective PHI")
        ax7.set_xlim(0.5, 0)
        ax7.xaxis.label.set_color("blue")
        ax7.tick_params(axis='x', colors="blue")
        ax7.spines["top"].set_position(("axes", 1.08))
        ax7.spines["top"].set_visible(True)
        ax7.spines["top"].set_edgecolor("blue")
        ax7.set_xticks([0, 0.25, 0.5])
    # Sw track
    if "SW_LIM" in cols:
        ax8.plot(well["SW_LIM"], well.index, color = "green")
        ax8.fill_betweenx(well.index,well["SW_LIM"], 0, facecolor='cyan', alpha=0.5) 
        ax8.set_xlabel("SW - Archie")
        ax8.set_xlim(0, 1)
        ax8.xaxis.label.set_color("green")
        ax8.tick_params(axis='x', colors="black")
        ax8.spines["top"].set_edgecolor("black")
        ax8.set_xticks([0, 0.5, 1])
    # Sw track
    #ax9.fill_betweenx(well["SW_SIM"], well.index, color="green")
    if "SW_SIM_LIM" in cols:
        ax9.plot(well["SW_SIM_LIM"], well.index, color="green" ) 
        ax9.fill_betweenx(well.index,well["SW_SIM_LIM"], 0, facecolor='cyan', alpha=0.5) 
        ax9.set_xlabel("SW - Simandoux")
        ax9.set_xlim(0, 1)
        ax9.xaxis.label.set_color("cyan")
        ax9.tick_params(axis='x', colors="black")
        ax9.spines["top"].set_edgecolor("black")    
        ax9.set_xticks([0, 0.5, 1])
    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3, ax4, ax6, ax8, ax9]:
        ax.set_ylim(max_depth, min_depth)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))
    plt.tight_layout()
    fig.subplots_adjust(wspace = 0.15)      
    graph = get_graph()
    return graph

def get_log_plot (well, max_depth, min_depth, well_nan):
    plt.switch_backend('AGG')
    fig, ax = plt.subplots(figsize=(10,15))
    #Set up the plot axes
    ax1 = plt.subplot2grid((1,6), (0,0), rowspan=1, colspan = 1)
    ax2 = plt.subplot2grid((1,6), (0,1), rowspan=1, colspan = 1, sharey = ax1)
    ax3 = plt.subplot2grid((1,6), (0,2), rowspan=1, colspan = 1, sharey = ax1)
    ax4 = plt.subplot2grid((1,6), (0,3), rowspan=1, colspan = 1, sharey = ax1)
    ax5 = ax3.twiny() #Twins the y-axis for the density track with the neutron track
    ax6 = plt.subplot2grid((1,6), (0,4), rowspan=1, colspan = 1, sharey = ax1)
    ax7 = ax2.twiny()
    

    # As our curve scales will be detached from the top of the track,
    # this code adds the top border back in without dealing with splines
    ax10 = ax1.twiny()
    ax10.xaxis.set_visible(False)
    ax11 = ax2.twiny()
    ax11.xaxis.set_visible(False)
    ax12 = ax3.twiny()
    ax12.xaxis.set_visible(False)
    ax13 = ax4.twiny()
    ax13.xaxis.set_visible(False)
    ax14 = ax6.twiny()
    ax14.xaxis.set_visible(False)

    

    # Gamma Ray track
    ax1.plot(well["GR"], well.index, color = "green", linewidth = 0.5)
    ax1.set_xlabel("Gamma")
    ax1.xaxis.label.set_color("green")
    ax1.set_xlim(0, 200)
    ax1.set_ylabel("Depth (m)")
    ax1.tick_params(axis='x', colors="green")
    ax1.spines["top"].set_edgecolor("green")
    ax1.title.set_color('green')
    ax1.set_xticks([0, 50, 100, 150, 200])

    # Resistivity track
    ax2.plot(well["LLD"], well.index, color = "red", linewidth = 0.5)
    ax2.set_xlabel("Resistivity - Deep")
    ax2.set_xlim(0.2, 2000)
    ax2.xaxis.label.set_color("red")
    ax2.tick_params(axis='x', colors="red")
    ax2.spines["top"].set_edgecolor("red")
    ax2.set_xticks([0.1, 1, 10, 100, 1000])
    ax2.semilogx()

    # Density track
    ax3.plot(well["RHOB"], well.index, color = "red", linewidth = 0.5)
    ax3.set_xlabel("Density")
    ax3.set_xlim(1.95, 2.95)
    ax3.xaxis.label.set_color("red")
    ax3.tick_params(axis='x', colors="red")
    ax3.spines["top"].set_edgecolor("red")
    ax3.set_xticks([1.95, 2.45, 2.95])

    # Sonic track
    ax4.plot(well["DT"], well.index, color = "purple", linewidth = 0.5)
    ax4.set_xlabel("Sonic")
    ax4.set_xlim(140, 40)
    ax4.xaxis.label.set_color("purple")
    ax4.tick_params(axis='x', colors="purple")
    ax4.spines["top"].set_edgecolor("purple")

    # Neutron track placed ontop of density track
    ax5.plot(well["NPHI"], well.index, color = "blue", linewidth = 0.5)
    ax5.set_xlabel('Neutron')
    ax5.xaxis.label.set_color("blue")
    ax5.set_xlim(0.45, -0.15)
     
    ax5.tick_params(axis='x', colors="blue")
    ax5.spines["top"].set_position(("axes", 1.08))
    ax5.spines["top"].set_visible(True)
    ax5.spines["top"].set_edgecolor("blue")
    ax5.set_xticks([0.45,  0.15, -0.15])

    # Caliper track
    ax6.plot(well["CALI"], well.index, color = "black", linewidth = 0.5)
    ax6.set_xlabel("Caliper")
    ax6.set_xlim(6, 16)
    ax6.xaxis.label.set_color("black")
    ax6.tick_params(axis='x', colors="black")
    ax6.spines["top"].set_edgecolor("black")
    ax6.fill_betweenx(well_nan.index, 8.5, well["CALI"], facecolor='yellow')
    ax6.set_xticks([6,  11, 16])

    # Resistivity track - Curve 2
    ax7.plot(well["LLS"], well.index, color = "green", linewidth = 0.5)
    ax7.set_xlabel("Resistivity - Shallow")
    ax7.set_xlim(0.2, 2000)
    ax7.xaxis.label.set_color("green")
    ax7.spines["top"].set_position(("axes", 1.08))
    ax7.spines["top"].set_visible(True)
    ax7.tick_params(axis='x', colors="green")
    ax7.spines["top"].set_edgecolor("green")
    ax7.set_xticks([0.1, 1, 10, 100, 1000])
    ax7.semilogx()
    # Common functions for setting up the plot can be extracted into
    # a for loop. This saves repeating code.
    for ax in [ax1, ax2, ax3, ax4, ax6]:
        ax.set_ylim(max_depth, min_depth)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))


    for ax in [ax2, ax3, ax4, ax6]:
        plt.setp(ax.get_yticklabels(), visible = False)

    plt.tight_layout()
    fig.subplots_adjust(wspace = 0.15)      
    graph = get_graph()
    return graph

def shale_volume(gamma_ray, gamma_ray_max, gamma_ray_min):
    vshale = (gamma_ray - gamma_ray_min) / (gamma_ray_max - gamma_ray_min)
    return round(vshale, 4)

def density_porosity(input_density, matrix_density, fluid_density):
    denpor = (matrix_density - input_density) / (matrix_density - fluid_density)
    return round(denpor, 4)

def sw_archie(porosity, rt, rw, archieA, archieM, archieN):
    sw = ((archieA / (porosity ** archieM)) * (rw/rt))**(1/archieN)
    return sw

def sw_simandoux(phie, rt, rw, archieA, archieM, archieN, vshale, rshale):
    A = (1 - vshale) * archieA * rw / (phie ** archieM)
    B = A * vshale / (2 * rshale)
    C = A / rt    
    sw = ((B **2 + C)**0.5 - B) **(2 / archieN)
    return sw