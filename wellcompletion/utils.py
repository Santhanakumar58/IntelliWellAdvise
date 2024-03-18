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
    plt.figure(figsize=(8,25))  
    ax=plt.axes()
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(1.0)  # change width
        ax.spines[axis].set_color('green')    # change color  
    widthsnew =[]
    for i in range(len(widths)):
        widthsnew.append(len(widths)*5-(i*3))
    widths = widthsnew
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
        lasteast = deviationdata.last() 
        maxdepth = 1000*(round(lasteast.measuredDepth+500)/1000)
        if lasteast.northSouth >5000:
            ratio = 50
        elif lasteast.northSouth >4000:
            ratio = 40
        elif lasteast.northSouth >3000:
            ratio = 30
        elif lasteast.northSouth >2000:
            ratio = 20
        elif lasteast.northSouth >1000:
            ratio = 10
        elif lasteast.northSouth >500:
            ratio = 5
        else :
            ratio = 3       
        
        for deviation in deviationdata:
            if deviation.measuredDepth <= depths[i]  and deviation.measuredDepth >= hangers[i] :
                x.append(float(deviation.northSouth + widths[i]*ratio/2))               
                y.append(float(-deviation.measuredDepth))
                x1.append(float(deviation.northSouth - widths[i]*ratio/2)) 
                xa=deviation.northSouth + widths[i]*ratio/2
                       
            if deviation.measuredDepth <= depths[i] and deviation.measuredDepth >= cements[i] :
                xx.append(float(deviation.northSouth + widths[i]*(ratio)/2+1) )              
                yy.append(float(-deviation.measuredDepth))
                xx1.append(float(deviation.northSouth - widths[i]*(ratio)/2-1))  
                xxx.append(float(deviation.northSouth + widths[i]*(ratio)/2-1) )
        
        x.append(x[-1])    
        y.append(float(-depths[i]))
        x1.append(x1[-1]) 
        xx.append(xx[-1] )   
        yy.append(float(-depths[i]))
        xx1.append(xx1[-1])  
        xxx.append(xxx[-1])     
        plt.plot(x,y, color='red') 
        #print(max(x), max(y))
        labela =f"{depths[i]}"
        plt.annotate(casingdefs[i] + "  casing at - " + labela, (xa,-depths[i]), textcoords='offset points', xytext=(0,-15), ha='center', color="blue")
        plt.plot(x1,y, color='red')
        plt.plot(xx,yy, color='cyan', linewidth=3, alpha=0.5)
        plt.plot(xx1,yy, color='cyan', linewidth=3, alpha=0.5) 
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
            tbgx.append(float(data.northSouth - (ratio/2))) 
            tbgx1.append(float(data.northSouth + (ratio/2))) 
            tbgy.append(-data.measuredDepth)

    #equipments   
    for i in  range(len(equipmentDepth)):
        plt.scatter(tbgx1[-1],-equipmentDepth[i] , color='green', marker="D", s=30)
        #if i%2  :
        plt.text(tbgx1[-1],-equipmentDepth[i] , equipmentName[i])
        #else:
        #     plt.text(tbgx1[-1],-equipmentDepth[i] , equipmentName[i])
    plt.plot(tbgx,tbgy, color='black', linewidth=2)
    plt.plot(tbgx1,tbgy, color='black', linewidth=2)    
    plt.xlabel("North Displacement" , color="cyan")    
    plt.ylabel("Measured Depth in ft" , color="cyan")    
    plt.tight_layout()
    plt.ylim(-(maxdepth+500), 0)
    #plt.xlim(-maxeast, maxeast)

    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  
    
    graph = get_graph()
    return graph
