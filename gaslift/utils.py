from turtle import color
import matplotlib.pyplot  as plt
import matplotlib  as mpl
import base64
from io import BytesIO
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from matplotlib.ticker import NullFormatter
from matplotlib.dates import MonthLocator, DateFormatter
import numpy as np
import datetime
from scipy.optimize import curve_fit
import pandas as pd
from shapely.geometry import linestring 


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_gaslift_design_plot(df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_Depth,reservoir_line):
    plt.switch_backend('AGG')  
    plt.style.use("seaborn")
    fig,ax=plt.subplots(1,1,figsize=(8,6))
    #fig.suptitle("GasLift Design",size=10)
    # draw the formation line:
    point1,point2=[df["P2"].iloc[-1],df["Depth"].iloc[-1]], [Pwf,total_Depth]
    ax.plot([point1[0],point2[0]],[point1[1],point2[1]],label="Formation",c="#080cdd")
    # draw the tubing line
    ax.plot([Pwh1,df["P2"].iloc[-1]],[0,df["Depth"].iloc[-1]],label="Tubing",c="#139100")
    # draw the modified tubing line
    ax.plot([Pwh2,df["P2"].iloc[-1]],[0,df["Depth"].iloc[-1]],label="Safty",c="#72f25c")
    # draw the casing line 
    #get_intersection
    d,p=find_intersection(reservoir_line,[1,-Pcs/40000,Pcs])
    ax.plot([Pcs,p],[0,d], c ="red" ,label="Casing")
    # ploting the horizontal lines and inclindes lines
    ax.plot([Pwh1,df["P1"].iloc[0]],[0,df["Depth"].iloc[0]],c="#bbb") 
     # horisontal lines
    for index,row in df.iterrows():
        ax.plot([row["P1"],row["P2"]],[row["Depth"],row["Depth"]],c="#bbb") 
    # inclinded lines
    for index,row in df.iterrows():
        if index +1 >= len(df):
            break
        else:
            ax.plot([row["P2"],df["P1"].iloc[index+1]],[row["Depth"],df["Depth"].iloc[index+1]],c="#bbb")
    # draw the line of kick_off
    ax.plot([Pko,df["P1"].iloc[0]],[0,df["Depth"].iloc[0]],label="Kick_off",c="orange")
    plt.gca().invert_yaxis()
    ax.xaxis.tick_top()
    ax.set_xlabel("Pressure (psi)")
    ax.set_ylabel("Depth (ft)")
    ax.xaxis.set_label_position("top")
    ax.set_xlim(0, Pwf+250)
    ax.set_ylim(total_Depth+250,0)
    plt.legend() 
    graph = get_graph()
    return graph













# GAS LIFT DESIGN FUNCTIONS

def get_equations(Pcs,j,BHSP,Q,Gs,D_total):
    """
    Pcs : surface injection pressure (psi) 
    j : productivity index 
    BHSP : bottomhole static pressure (psi)
    Q : oil flow rate ( bbl / day)
    Gs : static gradient ( psi/ft )
    D_total : total depth to the perforation (Ft)
    return 
    1- equation of reservoir line
    2- equation of caisng line
    """
        # so that we get injection point
    Gcs = Pcs/40000
    Pcs = Pcs-100
    Pwf= BHSP-(Q/j)
    # reservoir line
    reservoir_line = [1 ,-Gs, (Pwf - (Gs* D_total))]
    # casing line
    casing_line = [1,-Gcs,Pcs]
    
    return reservoir_line, casing_line ,Pwf

def find_intersection(line_1,line_2): 
    Z= np.array([ [line_1[0],line_1[1]],[line_2[0],line_2[1]] ])
    X= np.array([ [line_1[-1],line_1[-2]],[line_2[-1],line_2[-2]] ])
    Y= np.array([ [line_1[0],line_1[-1]],[line_2[0],line_2[-1]] ])
    try:
        D = np.linalg.det(Z)
        Dx= np.linalg.det(X)
        Dy= np.linalg.det(Y)
        P= Dx/D
        Depth= Dy/D 
        return np.round(Depth,2) , np.round(P,2)
    except:
        print("Error, there is no intersection")

def get_GF1_GF2(Tubing_head,Pcs,injection_depth, injection_pressure):
    Gf1 = (injection_pressure - Tubing_head) / injection_depth
    Pwh2= Tubing_head + 0.2*(Pcs - Tubing_head)
    Gf2=  (injection_pressure - Pwh2) / injection_depth
    return round(Gf1,3) , round(Gf2,3), round(Pwh2,3) 

def get_spacings(Pwh1,Pwh2,Pcs,Pko,Glf,Gf2,injection_depth,injection_pressure):
    depths=[]
    P1=[]
    P2=[]  
    casing_ko=[1,(-Pko/40000),Pko]
    line_1= [1,-Glf,Pwh1]
    depth,p1= find_intersection(casing_ko,line_1)
    depths.append(depth)
    P1.append(p1)
    p2= Pwh2 + Gf2*depths[-1]
    P2.append(p2)
    # new_line
    Gcs = Pcs/40000
#     for i in range(30):
    while depths[-1] < injection_depth:
        Pc_0 = Pcs*(1+(depths[-1]/40000))
#         casing_ps=[1,-Pc_0/40000,Pc_0]
        casing_ps=[1,-Gcs,Pc_0]
        line_2= [1,-Glf,P2[-1]]
        depth,p1= find_intersection(casing_ps,line_2)
        depths.append(depth + depths[-1])
        P1.append(p1)
        p2= Pwh2 + Gf2*depths[-1]
        P2.append(p2)
    dics={
    "Depth":np.round(depths,2),
     "P1":np.round(P1,2),
     "P2":np.round(P2,2)
     }

    df =pd.DataFrame(dics)
    df.drop(axis=0,index=df.index[-1],inplace=True)
    final_depth=np.round(injection_depth,2)
    p1= Pcs * (1+ (final_depth / 40000))
    p2= injection_pressure
    final={
    "Depth":np.round(injection_depth,2),
     "P1":np.round(p1,2),
     "P2":np.round(p2,2)
     }
    
    # df=df.append(final,ignore_index=True)
    # new lines 
    if (df.loc[df.index[-1],"Depth"] - df.loc[df.index[-2],"Depth"])  < 200:
        df.drop(axis=0,index=df.index[-2],inplace=True)
        
    # write the number of valves
    valves= [i+1 for i in range(len(df["Depth"]))]
    df["Valve .No"]= valves
    # df=df[["Valve .No","Depth","P1","P2"]]
    cols=["Valve .No","Depth","P1","P2"]
    df=df.reindex(columns=cols)
    return df 

def gaslift_design_function(total_depth,wellhead_pressure, Pcs ,Pko,Glf,Gs,Q,BHSP,J,Tre,Ts,R):
    reservoir_line,casing_line,Pwf = get_equations(Pcs,J,BHSP,Q,Gs,total_depth)
    injection_depth,injection_pressure = find_intersection(reservoir_line,casing_line)
    Gf1,Gf2,Pwh2 = get_GF1_GF2(wellhead_pressure,Pcs,injection_depth,injection_pressure)
    df=get_spacings(wellhead_pressure,Pwh2,Pcs,Pko,Glf,Gf2,injection_depth,injection_pressure) 
    
    # Tg= ((Tre-Ts) / total_depth)
    # df["Temp"] = np.round(Ts + Tg * df["Depth"],2)
    # df["Pdt"] = np.round((1-R)*df["P1"] + R*df["P2"],2)
    # make the Ct and get Pd and also Pvo
    Ct_data= pd.read_csv("./../GasliftData/Tempcoefficient.csv")
    Tg= ((Tre-Ts) / total_depth)
    df["Temp"] = np.round(Ts + Tg * df["Depth"],2)
    df["Pdt"] = np.round((1-R)*df["P1"] + R*df["P2"],2)
    df["Ct"]= df.Temp.apply(lambda T: (Ct_data[(Ct_data["temp"]== round(T))]["Ct"].values)[0] ) 
    df["Pd"]=round(df["Pdt"] * df["Ct"],2)
    df["Pvo"] = round(df["Pd"] / (1-R) ,2)
    return df,Pwf,wellhead_pressure,Pwh2,Pcs,Pko,total_depth,reservoir_line
