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

def get_plot(x,y,z, y1,y2,y3, y4):
    plt.switch_backend('AGG')   
    figure, axis = plt.subplots(2, 2)
    figure.set_size_inches(10, 10)     
    figure.suptitle("Production Performance Curves")  
    axis[0,1].plot(x, y, color='red', label = 'Gas Rate')    
    axis[0,1].set_title("Gas Rate")
    axis[0,1].set_xlabel('Date')
    axis[0,1].set_ylabel('Gas Rate scf/day')     
    axis[0,1].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[0,1].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[0,1].get_xticklabels():
        label.set_rotation(45) 

    axis[0,0].plot(x, y1, color='green', label = 'oil')
    axis[0,0].plot(x, y2, color='cyan', label = 'water')
    axis[0,0].plot(x, y3, color='red', label = 'liquid')
    axis[0,0].set_title("Liquid Rates") 
    axis[0,0].set_xlabel('Date')
    axis[0,0].set_ylabel('Liquid Rate Bbls/day')    
    axis[0,0].legend()  
    axis[0,0].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[0,0].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[0,0].get_xticklabels():
        label.set_rotation(45) 

    axis[1,1].plot(x, z, color='red', label = 'GOR')   
    axis[1,1].set_title("Gas Oil Ratio") 
    axis[1,1].set_xlabel('Date')
    axis[1,1].set_ylabel('GOR scf/bbl')   
    axis[1,1].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[1,1].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[1,1].get_xticklabels():
        label.set_rotation(45) 
    
    axis[1,0].plot(x, y4, color='green', label = 'Water Cut %')   
    axis[1,0].set_title("Water Cut") 
    axis[1,0].set_xlabel('Date')
    axis[1,0].set_ylabel('Water Cut %')     
    axis[1,0].xaxis.set_major_locator(MonthLocator(interval=1))
    axis[1,0].xaxis.set_major_formatter(mdates.DateFormatter('%b%y'))
    for label in axis[1,0].get_xticklabels():
        label.set_rotation(45) 


    figure.tight_layout()
    axis[0,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[0,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[1,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[1,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph

def hyperbolic(t, qi, di, b):
    """
    Hyperbolic decline function
    """
    import numpy as np
    return qi / (np.abs((1 + b * di * t))**(1/b))

def arps_fit(t, q, plot=True):
    plt.switch_backend('AGG')
    """
    Arps Decline Curve Analysis using Non-Linear Curve-Fitting
  
    Input:
    t = time array (in numpy datetime64)
    q = production rate array (unit: STB/day, or SCF/day)
    Output:
    qi = initial production rate (unit: STB/day, or SCF/day)
    di = initial decline rate (unit: STB/day, or SCF/day)
    b = decline exponent 
    """  
    di=2
    b=0.5   
    qi=max(q)  


    def hyperbolic(t, qi, di, b):
      return qi / (np.abs((1 + b * di * t))**(1/b))
  
    def rmse(y, yfit):
      N = len(y)
      return np.sqrt(np.sum(y-yfit)**2 / N)

    # subtract one datetime to another datetime
    date = t
    timedelta = [j-i for i, j in zip(t[:-1], t[1:])]
    timedelta = np.array(timedelta)
    timedelta = timedelta / datetime.timedelta(days=1)
    # take cumulative sum over timedeltas
    t = np.cumsum(timedelta)
    t = np.append(0, t)
    t = t.astype(float)
    # normalize the time and rate data
    t_normalized = t / max(t)
    q_normalized = q / max(q)  
    # fitting the data with the hyperbolic function
    popt, pcov = curve_fit(hyperbolic, t_normalized, q_normalized)
    qi, di, b = popt

    # RMSE is calculated on the normalized variables
    qfit_normalized = hyperbolic(t_normalized, qi, di, b)
    RMSE = rmse(q_normalized, qfit_normalized)
    # De-normalize qi and di
    qi = qi * max(q)
    di = di / max(t)
    if plot==True:
      # Print all parameters and RMSE
      print('Initial production rate (qi)  : {:.5f} VOL/D'.format(qi))
      print('Initial decline rate (di)     : {:.5f} VOL/D'.format(di))
      print('Decline coefficient (b)       : {:.5f}'.format(b))
      print('RMSE of regression            : {:.5f}'.format(RMSE))  
      # Produce the hyperbolic curve (fitted)
      tfit = np.linspace(min(t), max(t), 100)
      qfit = hyperbolic(tfit, qi, di, b)

      # Plot data and hyperbolic curve
      plt.figure(figsize=(8,5))
      plt.step(t, q, color='blue', label="Data")
      plt.plot(tfit, qfit, color='red', label="Hyperbolic Curve")
      plt.title(' Arps Decline Curve', size=20, pad=15)
      plt.xlabel('Days')
      plt.ylabel('Rate (Bbls/d)')
      plt.xlim(min(t), max(t)); plt.ylim(ymin=0)

      plt.legend()
      plt.grid()
      graph = get_graph()

    return qi, di, b, RMSE, graph

def arps_bootstrap(t, q, size=1):
    """
    Bootstrapping of Decline Curves
    """
    import numpy as np
    import datetime
    from scipy.optimize import curve_fit
    import matplotlib.pyplot as plt

    """ The exact copy of "arps_fit" function """
    #     def hyperbolic(t, qi, di, b):
    #       return qi / (np.abs((1 + b * di * t))**(1/b))
    
    def rmse(y, yfit):
      N = len(y)
      return np.sqrt(np.sum(y-yfit)**2 / N)

    # subtract one datetime to another datetime
    date = t
    timedelta = [j-i for i, j in zip(t[:-1], t[1:])]
    timedelta = np.array(timedelta)
    timedelta = timedelta / datetime.timedelta(days=1)

    # take cumulative sum over timedeltas
    t = np.cumsum(timedelta)
    t = np.append(0, t)
    t = t.astype(float)

    # normalize the time and rate data
    t_normalized = t / max(t)
    q_normalized = q / max(q)      

   
    # Set up array of indices to sample from: inds
    inds = np.arange(0, len(t_normalized))

    # Initialize replicates for qi, di, b
    bs_qi_reps = np.empty(size)
    bs_di_reps = np.empty(size)
    bs_b_reps = np.empty(size)   

    plt.figure(figsize=(10,7)) 

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = t_normalized[bs_inds], q_normalized[bs_inds]
        popt, pcov = curve_fit(hyperbolic, bs_x, bs_y)

        # qi, di, and b replicates
        bs_qi_reps[i], bs_di_reps[i], bs_b_reps[i] = popt

        # Denormalize replicates
        bs_qi_reps[i] = bs_qi_reps[i] * max(q)
        bs_di_reps[i] = bs_di_reps[i] / max(t)
    
        # Produce the hyperbolic curve (fitted)
        tfit = np.linspace(min(t), max(t), 100)
        qfit_reps = hyperbolic(tfit, bs_qi_reps[i], bs_di_reps[i], bs_b_reps[i])

        # Plot hyperbolic curve replicates
        plt.plot(tfit, qfit_reps, color='orange', alpha=0.3)

    # Calculate 95% CI
    ci95_qi = np.percentile(bs_qi_reps, [2.5, 97.5])
    ci95_di = np.percentile(bs_di_reps, [2.5, 97.5])
    ci95_b = np.percentile(bs_b_reps, [2.5, 97.5])

    min_qi, max_qi = ci95_qi
    min_di, max_di = ci95_di
    min_b, max_b = ci95_b

    print("95% CI of initial production rate (qi) : {:.5f} to {:.5f} VOL/D".format(min_qi, max_qi))
    print("95% CI of initial decline rate (di)    : {:.5f} to {:.5f} VOL/D".format(min_di, max_di))
    print("95% CI of decline exponent (b)         : {:.5f} to {:.5f}".format(min_b, max_b))

    ## Production rate using min CI
    qfit_min_ci = hyperbolic(tfit, min_qi, min_di, min_b) 
    qfit_max_ci = hyperbolic(tfit, max_qi, max_di, max_b) 

    # The exact DCA
    qi, di, b, RMSE, graph = arps_fit(date, q, plot=True)
    qfit = hyperbolic(tfit, qi, di, b)    

    plt.plot(tfit, qfit_reps, color='green', alpha=0.5, label="Replicates")
    plt.plot(tfit, qfit_min_ci, "--", color='purple', label="Minimum 95% CI")
    plt.plot(tfit, qfit_max_ci, "--", color='purple', label='Max 95% CI')
    #plt.plot(tfit, qfit*0.90, color="yellow", label="lower Range")
    #plt.plot(tfit, qfit*1.10, color="yellow", label="upper Range")
    plt.fill_between(tfit, qfit_min_ci, qfit_max_ci, color='yellow')
    plt.step(t, q, color='blue', label="Data")
    plt.title('Arps Bootstrap Curve', size=20, pad=15)
    plt.xlabel('Days')
    plt.ylabel('Rate (SCF/d)')
    plt.xlim(min(t), max(t))
    plt.ylim(0, max(q))
    plt.legend()
    plt.grid()  
    graph1 = get_graph()  

  

    return ci95_qi, ci95_di, ci95_b, graph1

def remove_outlier(df, column_name, window, number_of_stdevs_away_from_mean, trim=False):
   """
   Removing outlier of production data and trim initial buildup

   INPUT:

   df: Production dataframe
   column_name: Column name of production rate
   window: Rolling average window
   number_of_stdevs_away_from_mean: Distance from standard dev. where outliers
                                    will be removed
   trim: Option to trim initial buildup (Because buildup is an outlier). 
         Default is False.

   OUTPUT:

   df: New dataframe where outliers have been removed 
   """
   df[column_name+'_rol_Av']=df[column_name].rolling(window=window, center=True).mean()
   df[column_name+'_rol_Std']=df[column_name].rolling(window=window, center=True).std()

   # Detect anomalies by determining how far away from the mean (in terms of standard deviation)
   df[column_name+'_is_Outlier']=(abs(df[column_name]-df[
                              column_name+'_rol_Av'])>(
                              number_of_stdevs_away_from_mean*df[
                              column_name+'_rol_Std']))
  
   # outlier and not-outlier will be recorded in the '_is_Outlier'
   # column as 'True' and 'False'. Now, outlier is removed, so column that
   # contains 'True' values are masked out
   result = df.drop(df[df[column_name+'_is_Outlier'] == True].index).reset_index(drop=True)

   # Remove rows where "_rol_Av" has NaNs
   result = result[result[column_name+'_rol_Av'].notna()]  

   if trim==True:
    # Trim initial buildup
    maxi = result[column_name+'_rol_Av'].max()
    maxi_index = (result[result[column_name+'_rol_Av']==maxi].index.values)[0]
    result = result.iloc[maxi_index:,:].reset_index(drop=True)

   return result  

def convert_date_to_days(t):
    """
    Convert Numpy Datetime to Days 
    """
    import datetime
    import numpy as np

    # subtract one datetime to another datetime
    timedelta = [j-i for i, j in zip(t[:-1], t[1:])]
    timedelta = np.array(timedelta)
    timedelta = timedelta / datetime.timedelta(days=1)

    # take cumulative sum over timedeltas
    t = np.cumsum(timedelta)
    t = np.append(0, t)
    t = t.astype(float)
    return t


def get_arps_plots(t,q, qfit, q1fit):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,10))   
    tfit = np.linspace(min(t), max(t), 100) 
    figure, axis = plt.subplots(2, 1)
    figure.set_size_inches(12, 4) 

    axis[0,0].plot(t, q, color='blue', label = 'Data') 
    axis[0,0].plot(tfit, qfit, color='red', label = 'Hyperbolic Curve')       
    axis[0,0].set_title("Arps Decline Curve")
    axis[0,0].set_xlabel('Days on Production')
    axis[0,0].set_ylabel('Oil Rate Bbls/d')   
    for label in axis[0,1].get_xticklabels():
      label.set_rotation(45) 

    axis[0,1].plot(t, q, color='blue', label = 'Data') 
    axis[0,1].plot(tfit, q1fit, color='red', label = 'Hyperbolic Curve')     
    axis[0,1].set_title("Liquid Rates") 
    axis[0,1].set_xlabel('Date')
    axis[0,1].set_ylabel('Liquid Rate Bbls/day')    
    axis[0,1].legend()    
    for label in axis[0,1].get_xticklabels():
      label.set_rotation(45) 

    figure.tight_layout()
    axis[0,0].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    axis[0,1].grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph


def get_Beggs_Hagedorn_plot(pipline_range, pressures, pressures1, holdups, holdups1):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(12, 4))    
    plt.subplot(1,2,2)   

    plt.subplot(1,2,1)
    plt.plot(pipline_range, pressures,  label='BB', color = "r")
    plt.plot(pipline_range, pressures1,  label='HB', color = "green")
    plt.xlabel('Depth in ft')
    plt.ylabel('Pressure in psi')
    plt.legend(loc="upper right")    
    plt.title("Tubing Performance Curve")
    plt.ylim(max(pressures)+250, 0)
    plt.xlim(0, max(pipline_range) + 250)


    plt.subplot(1,2,2)
    plt.plot(pipline_range, holdups,  label='BB', color = "r")
    plt.plot(pipline_range, holdups1,  label='HB', color = "green")
    plt.xlabel('Depth in ft')
    plt.ylabel('Liquid Holdup')
    plt.legend(loc="upper right")    
    plt.title("Holdup Curve")    
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_Beggs_q_vs_press_plot(df, pdrop):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(10,6))    
    plt.subplot(1,1,1)
    plt.subplot(1,1,1)
    plt.plot(df["x1"], df['y1'],  label='Outflow', color = "r")
    plt.plot(df["x2"], df['y2'],  label='Inflow', color = "g")

    x2,y2=intersection(df["x1"], df['y1'], df["x2"], df['y2'] )
    

    plt.scatter(pdrop.liquid_Rate, pdrop.th_Pres)
    #plt.scatter(x2[-1],y2[-1], s=30, color="blue")
    xx=[x2[-1],x2[-1],0]
    yy=[0,y2[-1],y2[-1]]
    plt.plot(xx,yy, color="black" ,linestyle="dotted")
    xxx2 = round(x2[-1])
    yyy2 = round(y2[-1])
    plt.text(x2[-1],y2[-1], f"Intersection Point {xxx2} , {yyy2}")
    
    plt.xlabel('Liquid Rate BOPD')
    plt.ylabel('Pressure in psi')
    plt.legend(loc="upper right")    
    plt.title("Inflow-outflow Plot")
    plt.ylim(0, max(df['y1'])+250)
    plt.xlim(0, max(df["x2"]) + 250)
    
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_tubing_sensitivity_plot(df, pdrop):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(10,6))    
    plt.subplot(1,1,1)
    plt.subplot(1,1,1)
    plt.plot(df["x1"], df['y1'],  label='Tubing Id : 2.441 Inch ', color = "orange")    
    plt.plot(df["x1"], df['y2'],  label='Tubing Id : 2.867 Inch', color = "g", alpha=0.5)
    plt.plot(df["x1"], df['y3'],  label='Tubing Id : 3.883 Inch', color = "blue", alpha=0.7)   
    plt.plot(df["x5"], df['y5'],  label='Inflow', color = "r")
    x2,y2=intersection(df["x1"], df['y2'], df["x5"], df['y5'] )   
    plt.scatter(pdrop.liquid_Rate, pdrop.th_Pres)     
    xx=[x2[-1],x2[-1],0]
    yy=[0,y2[-1],y2[-1]]   
    plt.plot(xx,yy, color="black" ,linestyle="dotted")
    xxx2 = round(x2[-1])
    yyy2 = round(y2[-1])
    plt.text(x2[-1],y2[-1], f" Rate={xxx2} , Pres. ={yyy2}")
    
    plt.xlabel('Liquid Rate BOPD')
    plt.ylabel('Pressure in psi')
    plt.legend(loc="upper right")    
    plt.title("Tubing ID Sensitivities")
    plt.ylim(0, max(df['y1'])+250)
    plt.xlim(0, max(df["x1"]) + 250)
    #plt.subplot(1,2,2)
    #plt.plot(pipline_range, holdups,  label='BB', color = "r")
    #plt.plot(pipline_range, holdups1,  label='HB', color = "green")
    #plt.xlabel('Depth in ft')
    #plt.ylabel('Liquid Holdup')
    #plt.legend(loc="upper right")    
    #plt.title("Holdup Curve")    
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_gor_sensitivity_plot(df, pdrop):
    plt.switch_backend('AGG')  
    plt.figure(figsize=(10,6))    
    plt.subplot(1,1,1)
    plt.subplot(1,1,1)
    plt.plot(df["x1"], df['y1'],  label='80% of current GOR ', color = "orange")    
    plt.plot(df["x1"], df['y2'],  label='90%% of current GOR', color = "g", alpha=0.5)
    plt.plot(df["x1"], df['y3'],  label='Current GOR', color = "blue", alpha=0.7)
    plt.plot(df["x1"], df['y4'],  label='110 % of current GOR', color = "gray", alpha=0.9)
    plt.plot(df["x1"], df['y5'],  label='120% of current GOR', color = "black", alpha=0.7)
    plt.plot(df["x6"], df['y6'],  label='Inflow', color = "r")
    x2,y2=intersection(df["x1"], df['y3'], df["x6"], df['y6'] )   
    plt.scatter(pdrop.liquid_Rate, pdrop.th_Pres)   
    xx=[x2[-1],x2[-1],0]
    yy=[0,y2[-1],y2[-1]]   
    plt.plot(xx,yy, color="black" ,linestyle="dotted")
    xxx2 = round(x2[-1])
    yyy2 = round(y2[-1])
    plt.text(x2[-1],y2[-1], f" Rate={xxx2} , Pres. ={yyy2}")    
    plt.xlabel('Liquid Rate BOPD')
    plt.ylabel('Pressure in psi')
    plt.legend(loc="upper right")    
    plt.title("GOR Sensitivities")
    plt.ylim(0, max(df['y1'])+250)
    plt.xlim(0, max(df["x1"]) + 250)   
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_gaslift_design_plot(df,Pwf,Pwh1,Pwh2,Pcs,Pko,total_Depth,reservoir_line):
    plt.switch_backend('AGG')  
    plt.style.use("seaborn")
    fig,ax=plt.subplots(1,1,figsize=(8,6))
    fig.suptitle("GasLift Design",size=10)
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
    ax.plot([Pcs,p],[0,d],label="Casing")
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
    ax.plot([Pko,df["P1"].iloc[0]],[0,df["Depth"].iloc[0]],label="Kick_off",c="#1e647f")
    plt.gca().invert_yaxis()
    ax.xaxis.tick_top()
    ax.set_xlabel("Pressure (psi)")
    ax.set_ylabel("Depth (ft)")
    ax.xaxis.set_label_position("top")
    plt.legend() 
    graph = get_graph()
    return graph




def intersection(x1,y1,x2,y2):
    """
    INTERSECTIONS Intersections of curves.
    Computes the (x,y) locations where two curves intersect.  The curves
    can be broken with NaNs or have vertical segments.
    usage:
    x,y=intersection(x1,y1,x2,y2)
    Example:
    a, b = 1, 2
    phi = np.linspace(3, 10, 100)
    x1 = a*phi - b*np.sin(phi)
    y1 = a - b*np.cos(phi)
    x2=phi    
    y2=np.sin(phi)+2
    x,y=intersection(x1,y1,x2,y2)
    plt.plot(x1,y1,c='r')
    plt.plot(x2,y2,c='g')
    plt.plot(x,y,'*k')
    plt.show()
    """
    ii,jj=_rectangle_intersection_(x1,y1,x2,y2)
    n=len(ii)

    dxy1=np.diff(np.c_[x1,y1],axis=0)
    dxy2=np.diff(np.c_[x2,y2],axis=0)

    T=np.zeros((4,n))
    AA=np.zeros((4,4,n))
    AA[0:2,2,:]=-1
    AA[2:4,3,:]=-1
    AA[0::2,0,:]=dxy1[ii,:].T
    AA[1::2,1,:]=dxy2[jj,:].T

    BB=np.zeros((4,n))
    BB[0,:]=-x1[ii].ravel()
    BB[1,:]=-x2[jj].ravel()
    BB[2,:]=-y1[ii].ravel()
    BB[3,:]=-y2[jj].ravel()

    for i in range(n):
        try:
            T[:,i]=np.linalg.solve(AA[:,:,i],BB[:,i])
        except:
            T[:,i]=np.NaN
    in_range= (T[0,:] >=0) & (T[1,:] >=0) & (T[0,:] <=1) & (T[1,:] <=1)

    xy0=T[2:,in_range]
    xy0=xy0.T
    return xy0[:,0],xy0[:,1]

def _rect_inter_inner(x1,x2):
    n1=x1.shape[0]-1
    n2=x2.shape[0]-1
    X1=np.c_[x1[:-1],x1[1:]]
    X2=np.c_[x2[:-1],x2[1:]]    
    S1=np.tile(X1.min(axis=1),(n2,1)).T
    S2=np.tile(X2.max(axis=1),(n1,1))
    S3=np.tile(X1.max(axis=1),(n2,1)).T
    S4=np.tile(X2.min(axis=1),(n1,1))
    return S1,S2,S3,S4

def _rectangle_intersection_(x1,y1,x2,y2):
    S1,S2,S3,S4=_rect_inter_inner(x1,x2)
    S5,S6,S7,S8=_rect_inter_inner(y1,y2)

    C1=np.less_equal(S1,S2)
    C2=np.greater_equal(S3,S4)
    C3=np.less_equal(S5,S6)
    C4=np.greater_equal(S7,S8)

    ii,jj=np.nonzero(C1 & C2 & C3 & C4)
    return ii,jj


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
