from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import numpy as np
 

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,x1,xequip, yequip, xequip1, equipname, xequipmid,  casingxlistx,casingxlisty,casingxlistx1, noofcasings, cementxlistx,cementxlisty,cementxlistx1):   
    plt.switch_backend('AGG')    
    plt.rcParams["figure.figsize"] = [10.50, 8.50]
    plt.rcParams["figure.autolayout"] = True 
    #plt.plot(x, y, label='Completion', color='r')  
    #plt.plot(x1, y, label='Completion', color='r')   
    plt.plot(xequip, yequip, label='Completion', color='black')  
    plt.plot(xequip1, yequip, label='Completion', color='black')
    plt.scatter(xequipmid, yequip, label='Completion', color='black')
    # plt.plot(xequipmid, yequip, label='Completion', color='b', 
    #    marker= '+',
    #     mfc = 'none',
    #     lw = 2,
    #     mew = 2,
    #     ms = 20) 
    for i, txt in enumerate(equipname):
        plt.annotate(txt + " at " + str(yequip[i]), (xequip1[i] +30, yequip[i]))
 
    for i in range (0, noofcasings):
        plt.plot(casingxlistx[i], casingxlisty[i], color='blue')
        plt.plot(casingxlistx1[i],casingxlisty[i], color='blue') 
        plt.plot(cementxlistx[i], cementxlisty[i], color='cyan')
        plt.plot(cementxlistx1[i],cementxlisty[i], color='cyan') 
    graph = get_graph()
    return graph

def autolabel(ax, rects, xpos='center'):
   ha = {'center': 'center', 'right': 'left', 'left': 'right'}
   offset = {'center': 0, 'right': 1, 'left': -1}
   for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
        xy=(rect.get_x() + rect.get_width() / 2, height),
        xytext=(offset[xpos]*3, 3), # use 3 points offset
        textcoords="offset points", # in both directions
        ha=ha[xpos], va='bottom')

def get_plot1(dat,x1,x2,x3,y1,y2,y3):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,5))      
    labels =[x1,x2,x3]
    values=[y1,y2,y3]
    ind=np.arange(len(values))
    fig, ax = plt.subplots()    
    pp= ax.bar(labels, values, color=['red','green', 'orange'])    
    for p in pp:
        height = p.get_height()
        ax.annotate('{}'.format(height),
        xy=(p.get_x() + p.get_width() / 2, height),
        xytext=(0, 3), # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom')
    plt.ylabel('Rate Bbls/day / Gas Rate 1000 scf/day') 
    plt.title(f"Gains of Coil Tubing Intervention dated {dat}")  
    plt.legend(loc='upper right')
    plt.tight_layout()     
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    graph = get_graph()
    return graph


def get_plot2(widths, depths, hangers, cements, deviationdata, casingdefs, completion_datas, equipmentx,equipmentDepth,equipmentName ):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,15))  
    ax=plt.axes()
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2.5)  # change width
        ax.spines[axis].set_color('green')    # change color  
    widthsnew =[]
    for i in range(len(widths)):
        widthsnew.append(len(widths)*10-(i*10))
    widths = widthsnew
    lasteast = deviationdata.last() 
    maxdepth = 1000*(round(lasteast.measuredDepth+500)/1000)
    maxeast = 1000*(round(lasteast.eastWest+500)/1000)
    if lasteast.eastWest >5000:
        ratio = 50
    elif lasteast.eastWest >4000:
        ratio = 40
    elif lasteast.eastWest >3000:
        ratio = 30
    elif lasteast.eastWest >2000:
        ratio = 20
    elif lasteast.eastWest >1000:
        ratio = 10
    elif lasteast.eastWest >500:
        ratio = 5
    else :
        ratio = 3

    for i in range(len(widths)):
        x = []
        x1=[]
        y=[]
        xx=[]
        yy=[]
        xx1=[]      
        xxx=[]
        depth1=0.0
        east=0.0
        for deviation in deviationdata:
            if deviation.measuredDepth <= depths[i] and deviation.measuredDepth >= hangers[i] :
                x.append(float(deviation.eastWest + widths[i]*ratio))               
                y.append(float(-deviation.measuredDepth))
                x1.append(float(deviation.eastWest - widths[i]*ratio)) 
                xa=deviation.eastWest + widths[i]*ratio
               

            if deviation.measuredDepth <= depths[i] and deviation.measuredDepth >= cements[i] :
                xx.append(float(deviation.eastWest + widths[i]*(ratio+2)) )              
                yy.append(float(-deviation.measuredDepth))
                xx1.append(float(deviation.eastWest - widths[i]*(ratio+2)))  
                #xxx.append(float(deviation.eastWest + widths[i]*(ratio)) )     
       
        
        plt.plot(x,y, color='red')
        labela =f"{depths[i]}"
        plt.annotate(casingdefs[i] + "  casing at - " + labela, (xa,-depths[i]+100), textcoords='offset points', xytext=(0,-15), ha='left', color="blue")
        plt.plot(x1,y, color='red')
        plt.plot(xx,yy, color='cyan', linewidth=3, alpha=0.5)
        plt.plot(xx1,yy, color='cyan', linewidth=3, alpha=0.5)  
        #plt.fill_between(x, y3, y4, color='grey', alpha='0.5')       
        #plt.fill_between(xx,xx1,yy ,color='grey', alpha=0.5)
    # Tubing
    tubingend=0.0
    for equip in completion_datas:
        if equip.equipment == "Tubing_end":
            tubingend = equip.equip_Md        
            tbgendname =  str(equip.equip_Od)+ " , " + equip.equipment
    #equipname.append(ename) 
    tbgx=[]    
    tbgx1=[] 
    tbgy =[]
   
    for data in deviationdata :
        if data.measuredDepth <= tubingend:
            tbgx.append(float(data.eastWest - (2* ratio))) 
            tbgx1.append(float(data.eastWest + (2* ratio))) 
            tbgy.append(-data.measuredDepth)

    #equipments   
    for i in  range(len(equipmentDepth)):
        plt.scatter(equipmentx[i]+(ratio),-equipmentDepth[i] , color='green', marker="D", s=30)
        if i%2  :
            plt.text(equipmentx[i]+ratio,-equipmentDepth[i] , equipmentName[i])
        else:
             plt.text(equipmentx[i]+500,-equipmentDepth[i] , equipmentName[i])
    plt.plot(tbgx,tbgy, color='black', linewidth=2)
    plt.plot(tbgx1,tbgy, color='black', linewidth=2)    
    plt.xlabel("East Displacement" , color="blue")    
    plt.ylabel("Measured Depth in ft" , color="blue")    
    plt.tight_layout()
    plt.ylim(-(maxdepth+500), 0)
    plt.xlim(-maxeast, maxeast)

    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  
    
    graph = get_graph()
    return graph
