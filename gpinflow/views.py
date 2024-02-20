from ast import Global
from decimal import Decimal
import math
from django.shortcuts import render, redirect
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity
from selectedGasProducer.models import SelectedGasProducer
from .models import GPProductivityIndexModel, GPVogelModel, GPStandingsModel, GPWigginsModel, GPMultirateModel, GPDarcyModel
from .forms import GPProductivityIndexForm, GPStandingsForm, GPVogelForm, GPWigginsForm, GPMultiRateForm, GPDarcyModelForm
from .utils import draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_CompositePR_PI, draw_LayerIPR_Darcy, draw_LayerIPR_Multirate, draw_LayerIPR_PI, draw_LayerIPR_Standing, draw_LayerIPR_Vogel, draw_LayerIPR_Wiggin, draw_Multirateloglogplot, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins

def list_gpinflow(request): 
    selectedwell = SelectedGasProducer.objects.first() 
    if selectedwell.inflow =='PI':
        pimodels = GPProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y,pis = draw_CompositePR_PI(pimodels)
        return render (request, 'gpinflow/pindex.html', {'pimodels': pimodels, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodels = GPVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        print((vogelmodels))
        chart = draw_compositeIPR_Vogel(vogelmodels)        
        return render (request, 'gpinflow/vogel.html', {'vogelmodels': vogelmodels, 'chart':chart})  
    elif selectedwell.inflow =='Standing':
        standingmodels = GPStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        print (len(standingmodels))
        chart = draw_compositeIPR_Standing(standingmodels)                  
        return render (request, 'gpinflow/standing.html', {'standingmodels': standingmodels, 'chart':chart})  
    elif selectedwell.inflow =='Wiggins':
        wigginmodels = GPWigginsModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart = draw_compositeIPR_Wiggins(wigginmodels)         
        return render (request, 'gpinflow/wiggin.html', {'wigginmodels': wigginmodels, 'chart':chart}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodels = GPMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        chart =draw_CompositeIPR_Multirate(multiratemodels)         
        return render (request, 'gpinflow/multirate.html', {'multiratemodels': multiratemodels, 'chart':chart})
    elif selectedwell.inflow =='Darcy':        
        darcymodels = GPDarcyModel.objects.filter(wellid=selectedwell.wellid).all()  
        chart = draw_CompositeIPR_Darcy(darcymodels) 
        return render (request, 'gpinflow/darcy.html', {'darcymodels': darcymodels, 'chart':chart})       

def create_gpinflow(request):
    selectedwell = SelectedGasProducer.objects.first()    
    if selectedwell.inflow =='PI':
        models = GPProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('gpinflow:list_gpinflow')  
        pimodel = GPProductivityIndexModel()
        pimodel.fgid = selectedwell.fgid
        pimodel.wellid = selectedwell.wellid  
        form = GPProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":           
            pimodel.fgid = selectedwell.fgid
            pimodel.wellid = selectedwell.wellid            
            form = GPProductivityIndexForm(request.POST or None, instance=pimodel)          
            if form.is_valid(): 
                form.save() 
                print(pimodel)
                chart = draw_LayerIPR_PI(pimodel)
                return render (request, 'gpinflow/pindex_form.html', {'form': form, 'chart':chart})             
        return render (request, 'gpinflow/pindex_form.html', {'form': form})             
    elif selectedwell.inflow =='Vogel':
        models = GPVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('gpinflow:list_gpinflow')  
        vogelmodel = GPVogelModel()
        vogelmodel.fgid = selectedwell.fgid
        vogelmodel.wellid = selectedwell.wellid  
        form = GPVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":           
            vogelmodel.fgid = selectedwell.fgid
            vogelmodel.wellid = selectedwell.wellid
            form = GPVogelForm(request.POST or None, instance=vogelmodel)          
            if form.is_valid(): 
                vogelmodel.fgid = selectedwell.fgid
                vogelmodel.wellid = selectedwell.wellid
                vogelmodel.save() 
                print(vogelmodel)
                chart = draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'gpinflow/vogel_form.html', {'form': form, 'chart':chart})              
        return render (request, 'gpinflow/vogel_form.html', {'form': form})       
    elif selectedwell.inflow =='Standing':
        models = GPStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('gpinflow:list_inflow')  
        standingmodel = GPStandingsModel()
        standingmodel.fgid = selectedwell.fgid
        standingmodel.wellid = selectedwell.wellid  
        form = GPStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":           
            standingmodel.fgid = selectedwell.fgid
            standingmodel.wellid = selectedwell.wellid
            form = GPStandingsForm(request.POST or None, instance=standingmodel)          
            if form.is_valid(): 
                form.save()
                chart = draw_LayerIPR_Standing(standingmodel) 
                return redirect ('gpinflow:list_inflow')             
        return render (request, 'gpinflow/standing_form.html', {'form': form})   
    elif selectedwell.inflow =='Wiggins':
        models = GPWigginsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('gpinflow:list_inflow')  
        wigginmodel = GPWigginsModel()
        wigginmodel.fgid = selectedwell.fgid
        wigginmodel.wellid = selectedwell.wellid  
        form = GPWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":
            wigginmodel.fgid = selectedwell.fgid
            wigginmodel.wellid = selectedwell.wellid
            form = GPWigginsForm(request.POST or None, instance=wigginmodel)          
            if form.is_valid(): 
                form.save() 
                chart=draw_LayerIPR_Wiggin(wigginmodel)
                return redirect ('gpinflow:list_inflow')             
        return render (request, 'gpinflow/wiggin_form.html', {'form': form})   
    elif selectedwell.inflow =='MultiRate':
        models = GPMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('gpinflow:list_inflow')  
        multiratemodel = GPMultirateModel()
        multiratemodel.fgid = selectedwell.fgid
        multiratemodel.wellid = selectedwell.wellid  
        form = GPMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":
            multiratemodel.fgid = selectedwell.fgid
            form = GPMultiRateForm(request.POST or None, instance=multiratemodel)          
            if form.is_valid(): 
                form.save() 
                chart= draw_LayerIPR_Multirate(multiratemodel)
                loglogchart = draw_Multirateloglogplot(multiratemodel) 
                return render (request, 'gpinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})                           
        return render (request, 'gpinflow/multirate_form.html', {'form': form})     
    elif selectedwell.inflow =='Darcy':
        models = GPDarcyModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('gpinflow:list_inflow')  
        darcymodel = GPDarcyModel()
        darcymodel.fgid = selectedwell.fgid
        darcymodel.wellid = selectedwell.wellid 
        form = GPDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":
            darcymodel = GPDarcyModel()
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
            form = GPDarcyModelForm(request.POST or None, instance=darcymodel)          
            if form.is_valid(): 
                form.save() 
                chart = draw_LayerIPR_Darcy(darcymodel)
                return render (request,'gpinflow/darcy_form.html', {'form': form, 'chart':chart})             
        return render (request, 'gpinflow/darcy_form.html', {'form': form })   
   
def update_gpinflow(request, id):
    selectedwell = SelectedGasProducer.objects.first()
    if selectedwell.inflow =='PI':
        pimodel = GPProductivityIndexModel.objects.get(id=id)
        print(pimodel)
        chart= draw_LayerIPR_PI(pimodel)
        form = GPProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_PI(pimodel)
                return render (request, 'gpinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})
        return render (request, 'gpinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = GPVogelModel.objects.get(id=id)
        chart= draw_LayerIPR_Vogel(vogelmodel)
        form = GPVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'gpinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
        return render (request, 'gpinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
    elif selectedwell.inflow =='Standing':
        standingmodel = GPStandingsModel.objects.get(id=id)
        chart= draw_LayerIPR_Standing(standingmodel) 
        form = GPStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Standing(standingmodel) 
                return render (request, 'gpinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
        return render (request, 'gpinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
    elif selectedwell.inflow =='Wiggins':
        wigginmodel = GPWigginsModel.objects.get(id=id)
        chart= draw_LayerIPR_Wiggin(wigginmodel) 
        form = GPWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Wiggin(wigginmodel)
                return render (request, 'gpinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
        return render (request, 'gpinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = GPMultirateModel.objects.get(id=id)
        chart= draw_LayerIPR_Multirate(multiratemodel) 
        loglogchart = draw_Multirateloglogplot(multiratemodel) 
        form = GPMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()                
                chart= draw_LayerIPR_Multirate(multiratemodel)
                return render (request, 'gpinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
        return render (request, 'gpinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
    elif selectedwell.inflow =='Darcy':
        darcymodel = GPDarcyModel.objects.get(id=id)  
        chart= draw_LayerIPR_Darcy(darcymodel)      
        form = GPDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":        
            if form.is_valid():
                darcymodel.save()
                chart= draw_LayerIPR_Darcy(darcymodel)
                return render (request, 'gpinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart}) 
        return render (request, 'gpinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart})      
        
def delete_gpinflow(request, id):
    selectedwell = SelectedGasProducer.objects.first()  
    if selectedwell.inflow =='PI':
        pimodel = GPProductivityIndexModel.objects.get(id=id)  
        if request.method == 'POST' :
            pimodel.delete()
            return redirect ('gpinflow:list_inflow')
        return render (request, 'gpinflow/pindex_confirm_delete.html', {'pimodel':pimodel})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = GPVogelModel.objects.get(id=id)  
        if request.method == 'POST' :
            vogelmodel.delete()
            return redirect ('gpinflow:list_inflow')
        return render (request, 'gpinflow/vogel_confirm_delete.html', {'vogelmodel':vogelmodel})   
    elif selectedwell.inflow =='Standing':
        standingmodel = GPStandingsModel.objects.get(id=id)  
        if request.method == 'POST' :
            standingmodel.delete()
            return redirect ('gpinflow:list_inflow')
        return render (request, 'gpinflow/standing_confirm_delete.html', {'standingmodel':standingmodel})  
    elif selectedwell.inflow =='Wiggins':
        wigginsmodel = GPWigginsModel.objects.get(id=id)  
        if request.method == 'POST' :
            wigginsmodel.delete()
            return redirect ('gpinflow:list_inflow')
        return render (request, 'gpinflow/wiggin_confirm_delete.html', {'wigginsmodel':wigginsmodel}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = GPMultirateModel.objects.get(id=id)  
        if request.method == 'POST' :
            multiratemodel.delete()
            return redirect ('gpinflow:list_inflow')
        return render (request, 'gpinflow/multirate_confirm_delete.html', {'multiratemodel':multiratemodel}) 
    elif selectedwell.inflow =='Darcy':
        darcymodel = GPDarcyModel.objects.get(id=id)  
        if request.method == 'POST' :
            darcymodel.delete()
            return redirect ('gpinflow:list_inflow')
        return render (request, 'gpinflow/darcy_confirm_delete.html', {'darcymodel':darcymodel}) 
   


