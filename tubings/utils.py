from turtle import color
import matplotlib.pyplot  as plt
import base64
from io import BytesIO
import numpy as np
from IntelligentOilWell.custom_context_processors import linear_interpolation


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y,z,xa, ya, x1,y1,z1, x2,y2,z2,xb,yb, x3,y3,z3, x4,y4,z4, xc, yc, x5,y5,z5, casinga, casingb, casingc):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,10))
    plt.title("Casing Diagram")
    plt.plot(x,y, color='red')
    plt.plot(z,y, color='red')   
    labela =f"{ya}"
    plt.annotate(casinga + "casing at - " + labela, (xa,ya), textcoords='offset points', xytext=(0,-15), ha='center')
    plt.plot(x1,y1, color='green')
    plt.plot(z1,y1, color='green')
    plt.plot(x2,y2, color='red')
    plt.plot(z2,y2, color='red')
    labelb =f"{yb}"
    plt.annotate(casingb + "casing at - " + labelb, (xb,yb), textcoords='offset points', xytext=(0,-15), ha='center')
    plt.plot(x3,y3, color='green')
    plt.plot(z3,y3, color='green')
    plt.plot(x4,y4, color='red')
    plt.plot(z4,y4, color='red')
    labelc =f"{yc}"
    plt.annotate(casingc + "casing at - " + labelc, (xc,yc), textcoords='offset points', xytext=(0,-15), ha='center')
    plt.plot(x5,y5, color='green')
    plt.plot(z5,y5, color='green')    
    plt.gca().invert_yaxis()   
    plt.xticks(rotation=45)
    plt.xlabel('East-West')
    plt.ylabel('True Vertical Depth (ft)') 
    plt.legend()
    plt.xlim(-500,500)
    plt.ylim(10000,0)
    plt.tight_layout()
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  
    graph = get_graph()
    return graph

def get_plot2(widths, depths, hangers, cements, deviationdata, casingdefs, tubings, equipmentx,equipmentDepth,equipmentName ):
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
                x.append(float( widths[i]*ratio/5))               
                y.append(float(-deviation.measuredDepth))
                x1.append(float(- widths[i]*ratio/5)) 
                xa=20+widths[i]*ratio/5
                       
            if deviation.measuredDepth <= depths[i] and deviation.measuredDepth >= cements[i] :
                xx.append(float( widths[i]*(ratio)/5+1) )              
                yy.append(float(-deviation.measuredDepth))
                xx1.append(float( - widths[i]*(ratio)/5-1))  
                xxx.append(float( + widths[i]*(ratio)/5-1) )  
        x.append(x[-1])    
        y.append(float(-depths[i]))
        x1.append(x1[-1]) 
        xx.append(xx[-1] )   
        yy.append(float(-depths[i]))
        xx1.append(xx1[-1])  
        xxx.append(xxx[-1])     
        plt.plot(x,y, color='red', linewidth=3)         
        labela =f"{depths[i]}"
        plt.annotate(casingdefs[i] + "  casing at - " + labela, (xa,-depths[i]), textcoords='offset points', xytext=(0,-15), ha='center', color="blue")
        plt.plot(x1,y, color='red', linewidth=3)
        plt.plot(xx,yy, color='cyan', linewidth=3, alpha=0.5)
        plt.plot(xx1,yy, color='cyan', linewidth=3, alpha=0.5) 
    # Tubing
      
    for i in range(len(tubings)):
        tx = []
        tx1=[]
        ty=[] 
        tx.append(2.5) 
        tx.append(2.5)  
        if tubings[i].tubingType == "Tubing":
            col = "gray"  
        elif tubings[i].tubingType == "FlowCoupling" :
            col="green"   
        elif tubings[i].tubingType == "SCSSSV" :
            col="red"  
        elif tubings[i].tubingType == "PupJoint" :
            col="orange"  
        elif tubings[i].tubingType == "Packer" :
            col="blue"  
        else:
            col="brown"

        ty.append(float(-tubings[i].depth_From))
        ty.append(float(-tubings[i].depth_To))
        label = tubings[i].tubingType + " top at - " + str(tubings[i].depth_From)
        tx1.append(-2.5)
        tx1.append(-2.5)        
        #tx.append(tx[-1])    
        #ty.append(float(-tubings[i].depth_To))
        #tx1.append(tx1[-1]) 
        plt.plot(tx,ty,color=col, label=label, linewidth=3) 
        plt.plot(tx1,ty, color= col, linewidth=3)
        if tubings[i].tubingType == "Packer" :
            tx=[]
            ty=[]
            tx.append(2.5)
            tx.append(8.5)
            tx.append(8.5)
            tx.append(2.5)
            ty.append(float(-tubings[i].depth_From))
            ty.append(float(-tubings[i].depth_From))
            ty.append(float(-tubings[i].depth_To))
            ty.append(float(-tubings[i].depth_To))
            plt.plot(tx,ty,color=col, linewidth=3)  
            plt.fill_betweenx (ty, tx[0], tx[1], color="blue")
            tx1=[]
            ty1=[]
            tx1.append(-2.5)
            tx1.append(-8.5)
            tx1.append(-8.5)
            tx1.append(-2.5)
            ty1.append(float(-tubings[i].depth_From))
            ty1.append(float(-tubings[i].depth_From))
            ty1.append(float(-tubings[i].depth_To))
            ty1.append(float(-tubings[i].depth_To))
            plt.plot(tx1,ty1,color=col, linewidth=3)
            plt.fill_betweenx (ty1, tx1[0], tx1[1], color="blue")   

    plt.xlabel("" , color="cyan")    
    plt.ylabel("Measured Depth in ft" , color="cyan")  
    plt.legend() 
    plt.tight_layout()
    plt.ylim(-(maxdepth+500), 0)
    plt.xlim(-60,60)
    #plt.xlim(-maxeast, maxeast)

    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  
    
    graph = get_graph()
    return graph


def get_dummyplot():
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,10))
    plt.title("Casing Diagram")
    x=[100,100]
    y=[0,100]
    z=[200,200]
    ya="Outer Casing"
    plt.plot(x,y, color='red')
    plt.plot(z,y, color='red')   
    labela =f"{ya}"
    #plt.annotate(gicasinga + "gicasing at - " + labela, (xa,ya), textcoords='offset points', xytext=(0,-15), ha='center')
    x1=[125,125]
    y1=[0,500]
    z1=[175,175]
    yb="Conducter Casing"
    plt.plot(x1,y1, color='green')
    plt.plot(z1,y1, color='green')
    #plt.plot(x2,y2, color='red')
    #plt.plot(z2,y2, color='red')
    labelb =f"{yb}"
   #plt.annotate(gicasingb + "gicasing at - " + labelb, (xb,yb), textcoords='offset points', xytext=(0,-15), ha='center')
   #plt.plot(x3,y3, color='green')
   #plt.plot(z3,y3, color='green')
   #plt.plot(x4,y4, color='red')
   #plt.plot(z4,y4, color='red')
   #labelc =f"{yc}"
   #plt.annotate(gicasingc + "gicasing at - " + labelc, (xc,yc), textcoords='offset points', xytext=(0,-15), ha='center')
   #plt.plot(x5,y5, color='green')
   #plt.plot(z5,y5, color='green')    
    plt.gca().invert_yaxis()   
    plt.xticks(rotation=45)
    plt.xlabel('East-West')
    plt.ylabel('True Vertical Depth (ft)') 
    plt.legend()
    plt.xlim(0,300)
    plt.ylim(600,0)
    plt.tight_layout()
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  

    graph = get_graph()
    return graph
