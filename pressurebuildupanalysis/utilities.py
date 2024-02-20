from ast import Lambda
from encodings import normalize_encoding
from operator import contains
from turtle import color
from matplotlib import lines
import matplotlib.pyplot  as plt
plt.ion
import base64
from io import BytesIO
import numpy as np
from matplotlib.widgets import Cursor, Button
from matplotlib.backend_bases import MouseButton
import matplotlib.patches as mpl_patches  
import plotly.express as px
import plotly.graph_objects as go

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')    
    buffer.close()
    return graph

def get_constabt_Rate_Buildup_plot(t, p, q, x, m1, c1 , k,pi,s,t_since_shutin,your_guess):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,5))    
    # normal plot BHFP vs time
     

    plt.subplot(1,2,1)
    plt.plot(t, p, '.', color='black')
    plt.title('Normal Plot of BHFP vs Time', size=20, pad=10)
    plt.xlabel('Time since shut-in (hours)', size=17); plt.ylabel('Pressure (psia)', size=17)
    plt.xlim(0,max(t))

    ## plot the separate WTR and ETR region
    plt.axvspan(0, t[your_guess], color='blue', alpha=0.2)
    plt.axvspan(t[your_guess], max(t), color='green', alpha=0.3)

    labels2 = []
    labels2.append("Time @ shut-in = {} hours".format(np.round(t_since_shutin, 1)))  
    labels2.append("End of ETR Time = {} hours".format(np.round(t[your_guess], 3)))
    handles2 = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", 
                                  lw=0, alpha=0)] * 2

    plt.legend(handles2, labels2, loc='center right', fontsize='large', 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0) 
    plt.grid(True, which='both', color='black', linewidth=0.1)                                

    plt.subplot(1,2,2)
    plt.semilogx(x, p, '.', color='black')
    plt.title('Semilog Plot of BHFP vs Horner Time', size=20, pad=10)
    plt.xlabel(r'Horner time $(\frac{t_p+ \Delta t}{\Delta t})$', size=17) 
    plt.ylabel(r'$p_{wf}$ (psia)', size=17)
    plt.xlim(xmin=1)

    ## plot the separate WTR and ETR region
    plt.axvspan(0, x[-your_guess], color='green', alpha=0.3)
    plt.axvspan(x[-your_guess], 1E+25, color='blue', alpha=0.2)

    # output calculated results to plot
    labels1 = []
    labels1.append("Calc. Permeability = {} md".format(np.round(k, 3)))
    labels1.append("Calc. Initial Pressure = {} psia".format(np.round(pi, 3)))
    labels1.append("Calc. Skin Factor = {}".format(np.round(s, 3)))
    handles1 = [mpl_patches.Rectangle((0, 0), 1, 1, fc="white", ec="white", 
                                  lw=0, alpha=0)] * 3

    # plot regression line
    y_fit = m1 * np.log10(x) + c1
    plt.plot(x, y_fit, color='red', linewidth=0.8)

    # plt.gca().invert_xaxis()
    # plt.gca().yaxis.tick_right()
    # plt.gca().yaxis.set_label_position("right")

    plt.legend(handles1, labels1, loc='best', fontsize='large', 
              fancybox=True, framealpha=0.7, 
              handlelength=0, handletextpad=0) 

    plt.grid(True, which='both', color='black', linewidth=0.1)
    graph = get_graph()
    return graph
 

def get_totalplot1(p_data):      
    import matplotlib.pyplot as plt
    plt.rcParams['backend'] = 'TkAgg'
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    p_data= p_data.iloc[::20]
    x = p_data.index
    y =p_data['gauge_Pressure']
    click_count=0
    def onclick(event):
        click_count=+1
        if(click_count==1):
            plt.axvline(x=event.xdata, color='red', linestyle='--')
        if(click_count==2):
            plt.axvline(x=event.xdata, color='green', linestyle='--')
        if(click_count==3):
            plt.axvline(x=event.xdata, color='black', linestyle='--')
        print([event.xdata, event.ydata])
        plt.show()
    fig, ax = plt.subplots()

    # Plot a line in the range of 10
    ax.scatter(x,y, color='blue')

    # Bind the button_press_event with the onclick() method
    fig.canvas.mpl_connect('button_press_event', onclick)

    # Display the plot
    plt.show()
    # p_data= p_data.iloc[::20]
    # x = p_data.index
    # y =p_data['gauge_Pressure']
    # plt.scatter(x,y, color='blue')
    # plt.axvline(x=np.percentile(p_data.index, 30), color='red', linestyle='--')
    # plt.axvline(x=np.percentile(p_data.index, 60), color='red', linestyle='--')
    # plt.axvline(x=np.percentile(p_data.index, 80), color='red', linestyle='--')
    # plt.show()


def get_totalplot(p_data):      
    plt.ion
    import plotly.graph_objects as go
    import numpy as np   
    p_data =p_data.iloc[::20]
    x = p_data.index
    y =p_data['gauge_Pressure']
    f = go.FigureWidget([go.Scatter(x=x, y=y, mode='markers')])

    scatter = f.data[0]
    colors = ['#a3a7e4'] * 100
    marker_color = colors
    marker_size = [10] * 100
    f.layout.hovermode = 'closest'
   

    # create our callback function
    def update_point(trace, points, selector):
        c = list(marker_color)
        s = list(marker_size)
        for i in points.point_inds:
            c[i] = '#bae2be'
            s[i] = 20
            with f.batch_update():
                scatter_marker_color = c
                scatter_marker_size = s

    scatter.on_click(update_point)
    f.show()

def get_limits(p_data):  
    plt.switch_backend('AGG') 
    # define Draggable lines class    
    p_data =p_data.iloc[::20]
    class draggable_lines:
        def __init__(self, ax, kind, XorY, label, color):
            self.ax = ax
            self.c = ax.get_figure().canvas
            self.o = kind
            self.XorY = XorY
            self.label = label
            x=[]
            y=[]
            if kind == "h":
                x = [-1, 1]
                y = [XorY, XorY]

            elif kind == "v":
                x = [XorY, XorY]
                y = [0.00001, 1000000]
            self.line = lines.Line2D(x, y, picker=5, label=label, color=color)
            self.ax.add_line(self.line)
            self.c.draw_idle()
            self.sid = self.c.mpl_connect('pick_event', self.clickonline)

        def clickonline(self, event):
            if event.artist == self.line:
                self.follower = self.c.mpl_connect("motion_notify_event", self.followmouse)
                self.releaser = self.c.mpl_connect("button_press_event", self.releaseonclick)

        def followmouse(self, event):
            if self.o == "h":
                self.line.set_ydata([event.ydata, event.ydata])
            else:
                self.line.set_xdata([event.xdata, event.xdata])
            self.c.draw_idle()

        def releaseonclick(self, event):
            global DD_start, DD_end, BU_end
            if self.o == "h":
                self.XorY = self.line.get_ydata()[0]
            else:
                self.XorY = self.line.get_xdata()[0]
                if self.label == "DD_Start":
                    DD_start = round(self.XorY)
                elif self.label == "DD_end":
                    DD_end = round(self.XorY)
                elif self.label == "BU_end":
                    BU_end = round(self.XorY)

            self.c.mpl_disconnect(self.releaser)
            self.c.mpl_disconnect(self.follower)

    # plot pressure data
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(p_data.index, p_data["gauge_Pressure"], linestyle="none", marker="o", markersize=3)
    DD1 = draggable_lines(ax, "v", np.percentile(p_data.index, 30), label="DD_Start", color="green")
    DD2 = draggable_lines(ax, "v", np.percentile(p_data.index, 60), label="DD_end", color="red")
    BU2 = draggable_lines(ax, "v", np.percentile(p_data.index, 80), label="BU_end", color="black")
    plt.subplots_adjust()
    plt.suptitle("Pressure Plot")
    plt.title("Move the lines then click to estimate start and end times of each flow period DD/BU")
    plt.ylim([0, max(p_data["gauge_Pressure"]) + 1000])
    plt.legend()
    plt.grid() 
    plt.show()  
 
    try:
        # Filter Draw-down and Buildup data
        DD_data = p_data.loc[(p_data.index >= DD_start) & (p_data.index <= DD_end), ["DateTime", "gauge_Pressure"]].copy()
        DD_data.reset_index(inplace=True, drop=True)
        BU_data = p_data.loc[(p_data.index >= DD_end) & (p_data.index <= BU_end), ["DateTime", "gauge_Pressure"]].copy()
        BU_data.reset_index(inplace=True, drop=True)  
        data =[DD_data, BU_data]     
        print(data) 
        return data
    except NameError:
        print("Limits were not selected")

def prepare_data(raw_DD_data, raw_BU_data, params, required_test="BU"):
    plt.switch_backend('AGG')
    # add parameters to dictionary
    params["tp"] = (raw_DD_data.loc[len(raw_DD_data) - 1, "DateTime"] - raw_DD_data.loc[0, "DateTime"]).total_seconds() / 3600
    params["BU_duration"] = (raw_BU_data.loc[len(raw_BU_data) - 1, "DateTime"] - raw_BU_data.loc[0, "DateTime"]).total_seconds() / 3600
    params["test_type"] = required_test
    # prepare Buildup data
    if params["test_type"] == "BU":
        raw_data = raw_BU_data.copy()
        raw_data["p"] = raw_data["gauge_Pressure"]
        raw_data["t"] = raw_data["DateTime"].apply(lambda x:  (x - raw_data.loc[0, "DateTime"]).total_seconds() / 3600)
        raw_data["dp"] = raw_data["p"] - raw_data.loc[0, "p"]
        raw_data["te"] = raw_data["t"] * params["tp"] / (raw_data["t"] + params["tp"])
        params["pwf"] = raw_data.loc[0, "p"]
    # prepare Draw-down data
    else:
        raw_data = raw_DD_data.copy()
        raw_data["p"] = raw_data["gauge_Pressure"]
        raw_data["t"] = raw_data["DateTime"].apply(lambda x:  (x - raw_data.loc[0, "DateTime"]).total_seconds() / 3600)
        raw_data["dp"] = params["Pi"] - raw_data["p"]
        raw_data["te"] = raw_data["t"]
        params["pwf"] = np.mean(raw_data["p"])
    return raw_data, params



def clickonline(self, event):
    if event.artist == self.line:
        self.follower = self.c.mpl_connect("motion_notify_event", self.followmouse)
        self.releaser = self.c.mpl_connect("button_press_event", self.releaseonclick)
def followmouse(self, event):
    if self.o == "h":
        self.line.set_ydata([event.ydata, event.ydata])
    else:
        self.line.set_xdata([event.xdata, event.xdata])
        self.c.draw_idle()

def releaseonclick(self, event):
    global DD_start, DD_end, BU_end
    if self.o == "h":
        self.XorY = self.line.get_ydata()[0]
    else:
        self.XorY = self.line.get_xdata()[0]
        if self.label == "DD_Start":
            DD_start = round(self.XorY)
        elif self.label == "DD_end":
            DD_end = round(self.XorY)
        elif self.label == "BU_end":
            BU_end = round(self.XorY)
    self.c.mpl_disconnect(self.releaser)
    self.c.mpl_disconnect(self.follower)


def convert(x, from_='c', to_='f'):
    """
    Convert metric / SI units to oilfield units
    """

    # temperature
    if from_ == 'c' and to_ == 'f':
        return((x * 9 / 5) + 32)
    if from_ == 'c' and to_ == 'k':
        return(x + 273.15)
    if from_ == 'c' and to_ == 'r':
        return((x * 9 / 5) + 491.67)
    if from_ == 'f' and to_ == 'c':
        return((x - 32) * 5 / 9)
    if from_ == 'f' and to_ == 'k':
        return(((x - 32) * 5 / 9) + 273.15)
    if from_ == 'f' and to_ == 'r':
        return(x + 459.67)
    if from_ == 'k' and to_ == 'c':
        return(x - 273.15)
    if from_ == 'k' and to_ == 'f':
        return((x - 273.15) * (9 / 5) + 32)
    if from_ == 'k' and to_ == 'r':
        return(x * 9 / 5)
    if from_ == 'r' and to_ == 'c':
        return((x - 491.67) * 5 / 9)
    if from_ == 'r' and to_ == 'f':
        return(x - 459.67)
    if from_ == 'r' and to_ == 'k':
        return(x * 5 / 9)

    # pressure
    if from_ == 'atm' and to_ == 'psi':
        return(x * 14.6959)
    if from_ == 'pa' and to_ == 'psi':
        return(x * 0.000145038)
    if from_ == 'bar' and to_ == 'psi':
        return(x * 14.5038)
    if from_ == 'lbf/ft2' and to_ == 'psi':
        return(x / 144)
    if from_ == 'dyne/cm2' and to_ == 'psi':
        return(x * 68947.6)

    # mass
    if from_ == 'kg' and to_ == 'lbm':
        return(x * 2.20462)

    # length
    if from_ == 'm' and to_ == 'ft':
        return(x * 3.28084)
    if from_ == 'mile' and to_ == 'ft':
        return(x * 5280)

    # area
    if from_ == 'm2' and to_ == 'ft2':
        return(x * 10.7639)
    if from_ == 'acre' and to_ == 'ft2':
        return(x * 43560)
    if from_ == 'ha' and to_ == 'ft2':
        return(x * 107639)

    # volume
    if from_ == 'm3' and to_ == 'ft3':
        return(x * 35.3147)
    if from_ == 'acre-ft' and to_ == 'ft3':
        return(x * 43559.9)
    if from_ == 'm3' and to_ == 'bbl':
        return(x * 6.28981)
    if from_ == 'acre-ft' and to_ == 'bbl':
        return(x * 7758.36)
    if from_ == 'ft3' and to_ == 'bbl':
        return(x * 0.178108)
    if from_ == 'bbl' and to_ == 'ft3':
        return(x * 5.61458)
    if from_ == 'gal' and to_ == 'bbl':
        return(x * 0.02)
    if from_ == 'gal' and to_ == 'ft3':
        return(x * 0.133681)

    # permeability
    if from_ == 'm2' and to_ == 'md':
        return(x * 9.869233E+13)
    if from_ == 'ft2' and to_ == 'md':
        return((x / 10.764) * 9.869233E+13)

def dictionary(parameter):
    """
    Nomenclatures for inputs and outputs, giving the descriptions, and the oilfield units
    Input:
    parameter = the input-output parameter, string
    Output:
    description = the description of the parameter
    unit = the oilfield unit of the parameter
    """
    description = {"Bg": "gas formation volume factor",
                   "Bo": "oil formation volume factor",
                   "Bw": "water formation volume factor",
                   "p": "pressure",
                   "temp": "temperature",
                   "cf":"formation compressibility",
                   "cw": "water compressibility",
                   "Efw": "formation expansion factor",
                   "Eg": "gas expansion factor",
                   "F": "reservoir voidage",
                   "Fr": "recovery factor",
                   "Gfgi": "initial gas in place",
                   "Gp": "cumulative gas produced",
                   "h": "thickness",
                   "Rv": "volatile oil-gas ratio",
                   "Rs": "solution gas-oil ratio",
                   "sw": "water saturation",
                   "t": "time",
                   "We": "water encroachment from aquifer",
                   "We_D": "dimensionless water encroachment from aquifer",
                   "Wp": "cumulative water produced",
                   "z": "gas compressibility factor",
                   "sg": "gas specific gravity",
                   "poro": "porosity",
                   "area": "reservoir productive area",
                   "Wi": "cumulative water injected",
                   "Gi": "cumulative gas injected",
                   "Vo": "condensate volume in PVT cell",
                   "z2": "two-phase compressibility factor",
                   "x_co2": "mole fraction of CO2 in gas",
                   "x_h2s": "mole fraction of H2S in gas",
                   "P_pr": "pseudo-reduced pressure",
                   "T_pr": "pseudo-reduced temperature"
                   }
    unit = {"Bg": "RB/scf",
            "Bo": "RB/STB",
            "Bw": "RB/STB",
            "p": "psia",
            "temp": "fahrenheit, celsius, rankine, kelvin",
            "cf": "psi^-1",
            "cw": "psi^-1",
            "Efw": "dimensionless",
            "Eg": "RB/scf",
            "F": "res bbl",
            "Fr": "dimensionless",
            "Gfgi": "ft3 (scf)",
            "Gp": "ft3 (scf)",
            "h": "ft",
            "Rv": "RB/scf",
            "Rs": "RB/STB",
            "swi": "fraction, v/v",
            "t": "any",
            "We": "res bbl",
            "We_D": "dimensionless",
            "Wp": "STB",
            "z": "dimensionless",
            "sg": "dimensionless",
            "poro": "fraction, v/v",
            "area": "ft2",
            "Wi": "STB",
            "Gi": "ft3 (scf)",
            "Vo": "res bbl",
            "z2": "dimensionless",
            "x_co2": "fraction, v/v",
            "x_h2s": "fraction, v/v",
            "P_pr": "dimensionless",
            "T_pr": "dimensionless"
            }

    description = description[parameter]
    unit = unit[parameter]

    return (description, unit)