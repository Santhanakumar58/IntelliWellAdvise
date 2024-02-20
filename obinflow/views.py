from ast import Global
from decimal import Decimal
import math
from django.shortcuts import render, redirect
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity
from selectedObserver.models import SelectedObserver
from .models import OBProductivityIndexModel, OBVogelModel, OBStandingsModel, OBWigginsModel, OBMultirateModel, OBDarcyModel
from .forms import OBProductivityIndexForm, OBStandingsForm, OBVogelForm, OBWigginsForm, OBMultiRateForm, OBDarcyModelForm
from .utils import draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_CompositePR_PI, draw_LayerIPR_Darcy, draw_LayerIPR_Multirate, draw_LayerIPR_PI, draw_LayerIPR_Standing, draw_LayerIPR_Vogel, draw_LayerIPR_Wiggin, draw_Multirateloglogplot, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins

def list_obinflow(request): 
    selectedwell = SelectedObserver.objects.first() 
    if selectedwell.inflow =='PI':
        pimodels = OBProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y,pis = draw_CompositePR_PI(pimodels)
        return render (request, 'obinflow/pindex.html', {'pimodels': pimodels, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodels = OBVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        print((vogelmodels))
        chart = draw_compositeIPR_Vogel(vogelmodels)        
        return render (request, 'obinflow/vogel.html', {'vogelmodels': vogelmodels, 'chart':chart})  
    elif selectedwell.inflow =='Standing':
        standingmodels = OBStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        print (len(standingmodels))
        chart = draw_compositeIPR_Standing(standingmodels)                  
        return render (request, 'obinflow/standing.html', {'standingmodels': standingmodels, 'chart':chart})  
    elif selectedwell.inflow =='OBWiggins':
        wigginmodels = OBWigginsModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart = draw_compositeIPR_Wiggins(wigginmodels)         
        return render (request, 'obinflow/wiggin.html', {'wigginmodels': wigginmodels, 'chart':chart}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodels = OBMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        chart =draw_CompositeIPR_Multirate(multiratemodels)         
        return render (request, 'obinflow/multirate.html', {'multiratemodels': multiratemodels, 'chart':chart})
    elif selectedwell.inflow =='OBDarcy':        
        darcymodels = OBDarcyModel.objects.filter(wellid=selectedwell.wellid).all()  
        chart = draw_CompositeIPR_Darcy(darcymodels) 
        return render (request, 'obinflow/darcy.html', {'darcymodels': darcymodels, 'chart':chart})       

def create_obinflow(request):
    selectedwell = SelectedObserver.objects.first()    
    if selectedwell.inflow =='PI':
        models = OBProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('obinflow:list_inflow')  
        pimodel = OBProductivityIndexModel()
        pimodel.fgid = selectedwell.fgid
        pimodel.wellid = selectedwell.wellid  
        form = OBProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":           
            pimodel.fgid = selectedwell.fgid
            pimodel.wellid = selectedwell.wellid            
            form = OBProductivityIndexForm(request.POST or None, instance=pimodel)          
            if form.is_valid(): 
                form.save() 
                print(pimodel)
                chart = draw_LayerIPR_PI(pimodel)
                return render (request, 'obinflow/pindex_form.html', {'form': form, 'chart':chart})            
        return render (request, 'obinflow/pindex_form.html', {'form': form})             
    elif selectedwell.inflow =='Vogel':
        models = OBVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('obinflow:list_inflow')  
        vogelmodel = OBVogelModel()
        vogelmodel.fgid = selectedwell.fgid
        vogelmodel.wellid = selectedwell.wellid  
        form = OBVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":           
            vogelmodel.fgid = selectedwell.fgid
            vogelmodel.wellid = selectedwell.wellid
            form = OBVogelForm(request.POST or None, instance=vogelmodel)          
            if form.is_valid(): 
                vogelmodel.fgid = selectedwell.fgid
                vogelmodel.wellid = selectedwell.wellid
                vogelmodel.save() 
                print(vogelmodel)
                chart = draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'obinflow/vogel_form.html', {'form': form, 'chart':chart})              
        return render (request, 'obinflow/vogel_form.html', {'form': form})       
    elif selectedwell.inflow =='Standing':
        models = OBStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('obinflow:list_inflow')  
        standingmodel = OBStandingsModel()
        standingmodel.fgid = selectedwell.fgid
        standingmodel.wellid = selectedwell.wellid  
        form = OBStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":           
            standingmodel.fgid = selectedwell.fgid
            standingmodel.wellid = selectedwell.wellid
            form = OBStandingsForm(request.POST or None, instance=standingmodel)          
            if form.is_valid(): 
                form.save()
                chart = draw_LayerIPR_Standing(standingmodel) 
                return redirect ('obinflow:list_inflow')             
        return render (request, 'obinflow/standing_form.html', {'form': form})   
    elif selectedwell.inflow =='OBWiggins':
        models = OBWigginsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('obinflow:list_inflow')  
        wigginmodel = OBWigginsModel()
        wigginmodel.fgid = selectedwell.fgid
        wigginmodel.wellid = selectedwell.wellid  
        form = OBWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":
            wigginmodel.fgid = selectedwell.fgid
            wigginmodel.wellid = selectedwell.wellid
            form = OBWigginsForm(request.POST or None, instance=wigginmodel)          
            if form.is_valid(): 
                form.save() 
                chart=draw_LayerIPR_Wiggin(wigginmodel)
                return redirect ('obinflow:list_inflow')             
        return render (request, 'obinflow/wiggin_form.html', {'form': form})   
    elif selectedwell.inflow =='MultiRate':
        models = OBMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('obinflow:list_inflow')  
        multiratemodel = OBMultirateModel()
        multiratemodel.fgid = selectedwell.fgid
        multiratemodel.wellid = selectedwell.wellid  
        form = OBMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":
            multiratemodel.fgid = selectedwell.fgid
            form = OBMultiRateForm(request.POST or None, instance=multiratemodel)          
            if form.is_valid(): 
                form.save() 
                chart= draw_LayerIPR_Multirate(multiratemodel)
                loglogchart = draw_Multirateloglogplot(multiratemodel) 
                return render (request, 'obinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})                           
        return render (request, 'obinflow/multirate_form.html', {'form': form})     
    elif selectedwell.inflow =='OBDarcy':
        models = OBDarcyModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('obinflow:list_inflow')  
        darcymodel = OBDarcyModel()
        darcymodel.fgid = selectedwell.fgid
        darcymodel.wellid = selectedwell.wellid 
        form = OBDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":
            darcymodel = OBDarcyModel()
            darcymodel.fgid = selectedwell.fgid
            darcymodel.wellid = selectedwell.wellid
            #darcymodel.analysis_Date=request.POST.get('analysis_Date')
            #darcymodel.layer_Permeability=request.POST.get('layer_Permeability')
            #darcymodel.layer_Thickness=request.POST.get('layer_Thickness')
            #darcymodel.drainage_Radius=request.POST.get('drainage_Radius')
            #darcymodel.wellbore_Radius=request.POST.get('wellbore_Radius')
            #darcymodel.layer_Skin=request.POST.get('layer_Skin')
            #darcymodel.current_Reservoir_Pressure=request.POST.get('current_Reservoir_Pressure')
            #darcymodel.pvt_Well=request.POST.get('pvt_Well_id')            
            #darcymodel.layer_Name = request.POST.get('layer_Name_id')            
            form = OBDarcyModelForm(request.POST or None, instance=darcymodel)          
            if form.is_valid(): 
                form.save() 
                chart = draw_LayerIPR_Darcy(darcymodel)
                return render (request,'obinflow/darcy_form.html', {'form': form, 'chart':chart})             
        return render (request, 'obinflow/darcy_form.html', {'form': form })   
   
def update_obinflow(request, id):
    selectedwell = SelectedObserver.objects.first()
    if selectedwell.inflow =='PI':
        pimodel = OBProductivityIndexModel.objects.get(id=id)
        print(pimodel)
        chart= draw_LayerIPR_PI(pimodel)
        form = OBProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_PI(pimodel)
                return render (request, 'obinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})
        return render (request, 'obinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = OBVogelModel.objects.get(id=id)
        chart= draw_LayerIPR_Vogel(vogelmodel)
        form = OBVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'obinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
        return render (request, 'obinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
    elif selectedwell.inflow =='Standing':
        standingmodel = OBStandingsModel.objects.get(id=id)
        chart= draw_LayerIPR_Standing(standingmodel) 
        form = OBStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Standing(standingmodel) 
                return render (request, 'obinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
        return render (request, 'obinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
    elif selectedwell.inflow =='OBWiggins':
        wigginmodel = OBWigginsModel.objects.get(id=id)
        chart= draw_LayerIPR_Wiggin(wigginmodel) 
        form = OBWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Wiggin(wigginmodel)
                return render (request, 'obinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
        return render (request, 'obinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = OBMultirateModel.objects.get(id=id)
        chart= draw_LayerIPR_Multirate(multiratemodel) 
        loglogchart = draw_Multirateloglogplot(multiratemodel) 
        form = OBMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()                
                chart= draw_LayerIPR_Multirate(multiratemodel)
                return render (request, 'obinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
        return render (request, 'obinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
    elif selectedwell.inflow =='OBDarcy':
        darcymodel = OBDarcyModel.objects.get(id=id)  
        chart= draw_LayerIPR_Darcy(darcymodel)      
        form = OBDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":        
            if form.is_valid():
                darcymodel.save()
                chart= draw_LayerIPR_Darcy(darcymodel)
                return render (request, 'obinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart}) 
        return render (request, 'obinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart})      
        
def delete_obinflow(request, id):
    selectedwell = SelectedObserver.objects.first()  
    if selectedwell.inflow =='PI':
        pimodel = OBProductivityIndexModel.objects.get(id=id)  
        if request.method == 'POST' :
            pimodel.delete()
            return redirect ('obinflow:list_inflow')
        return render (request, 'obinflow/pindex_confirm_delete.html', {'pimodel':pimodel})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = OBVogelModel.objects.get(id=id)  
        if request.method == 'POST' :
            vogelmodel.delete()
            return redirect ('obinflow:list_inflow')
        return render (request, 'obinflow/vogel_confirm_delete.html', {'vogelmodel':vogelmodel})   
    elif selectedwell.inflow =='Standing':
        standingmodel = OBStandingsModel.objects.get(id=id)  
        if request.method == 'POST' :
            standingmodel.delete()
            return redirect ('obinflow:list_inflow')
        return render (request, 'obinflow/standing_confirm_delete.html', {'standingmodel':standingmodel})  
    elif selectedwell.inflow =='OBWiggins':
        wigginsmodel = OBWigginsModel.objects.get(id=id)  
        if request.method == 'POST' :
            wigginsmodel.delete()
            return redirect ('obinflow:list_inflow')
        return render (request, 'obinflow/wiggin_confirm_delete.html', {'wigginsmodel':wigginsmodel}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = OBMultirateModel.objects.get(id=id)  
        if request.method == 'POST' :
            multiratemodel.delete()
            return redirect ('obinflow:list_inflow')
        return render (request, 'obinflow/multirate_confirm_delete.html', {'multiratemodel':multiratemodel}) 
    elif selectedwell.inflow =='OBDarcy':
        darcymodel = OBDarcyModel.objects.get(id=id)  
        if request.method == 'POST' :
            darcymodel.delete()
            return redirect ('obinflow:list_inflow')
        return render (request, 'obinflow/darcy_confirm_delete.html', {'darcymodel':darcymodel}) 
   


