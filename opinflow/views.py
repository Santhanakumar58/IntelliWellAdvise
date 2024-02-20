from ast import Global
from decimal import Decimal
import math
from django.shortcuts import render, redirect
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity
from selectedOilProducer.models import SelectedOilProducer
from .models import ProductivityIndexModel, VogelModel, StandingsModel, WigginsModel, MultirateModel, DarcyModel
from .forms import ProductivityIndexForm, StandingsForm, VogelForm, WigginsForm, MultiRateForm, DarcyModelForm
from .utility import draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_CompositePR_PI, draw_LayerIPR_Darcy, draw_LayerIPR_Multirate, draw_LayerIPR_PI, draw_LayerIPR_Standing, draw_LayerIPR_Vogel, draw_LayerIPR_Wiggin, draw_Multirateloglogplot, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins

def list_inflow(request): 
    selectedwell = SelectedOilProducer.objects.first() 
    if selectedwell.inflow =='PI':
        pimodels = ProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y,pis = draw_CompositePR_PI(pimodels)
        return render (request, 'opinflow/pindex.html', {'pimodels': pimodels, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodels = VogelModel.objects.filter(wellid=selectedwell.wellid).all()
        print((vogelmodels))
        chart = draw_compositeIPR_Vogel(vogelmodels)        
        return render (request, 'opinflow/vogel.html', {'vogelmodels': vogelmodels, 'chart':chart})  
    elif selectedwell.inflow =='Standing':
        standingmodels = StandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        print (len(standingmodels))
        chart = draw_compositeIPR_Standing(standingmodels)                  
        return render (request, 'opinflow/standing.html', {'standingmodels': standingmodels, 'chart':chart})  
    elif selectedwell.inflow =='Wiggins':
        wigginmodels = WigginsModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart = draw_compositeIPR_Wiggins(wigginmodels)         
        return render (request, 'opinflow/wiggin.html', {'wigginmodels': wigginmodels, 'chart':chart}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodels = MultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        chart =draw_CompositeIPR_Multirate(multiratemodels)         
        return render (request, 'opinflow/multirate.html', {'multiratemodels': multiratemodels, 'chart':chart})
    elif selectedwell.inflow =='Darcy':        
        darcymodels = DarcyModel.objects.filter(wellid=selectedwell.wellid).all()  
        chart = draw_CompositeIPR_Darcy(darcymodels) 
        return render (request, 'opinflow/darcy.html', {'darcymodels': darcymodels, 'chart':chart})       

def create_inflow(request):
    selectedwell = SelectedOilProducer.objects.first()    
    if selectedwell.inflow =='PI':
        models = ProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('opinflow:list_inflow')  
        pimodel = ProductivityIndexModel()
        pimodel.fgid = selectedwell.fgid
        pimodel.wellid = selectedwell.wellid  
        form = ProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":           
            pimodel.fgid = selectedwell.fgid
            pimodel.wellid = selectedwell.wellid            
            form = ProductivityIndexForm(request.POST or None, instance=pimodel)          
            if form.is_valid(): 
                form.save() 
                print(pimodel)
                chart = draw_LayerIPR_PI(pimodel)
                return render (request, 'opinflow/pindex_form.html', {'form': form, 'chart':chart})             
        return render (request, 'opinflow/pindex_form.html', {'form': form})             
    elif selectedwell.inflow =='Vogel':
        models = VogelModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('opinflow:list_inflow')  
        vogelmodel = VogelModel()
        vogelmodel.fgid = selectedwell.fgid
        vogelmodel.wellid = selectedwell.wellid  
        form = VogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":           
            vogelmodel.fgid = selectedwell.fgid
            vogelmodel.wellid = selectedwell.wellid
            form = VogelForm(request.POST or None, instance=vogelmodel)          
            if form.is_valid(): 
                vogelmodel.fgid = selectedwell.fgid
                vogelmodel.wellid = selectedwell.wellid
                vogelmodel.save() 
                print(vogelmodel)
                chart = draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'opinflow/vogel_form.html', {'form': form, 'chart':chart})              
        return render (request, 'opinflow/vogel_form.html', {'form': form})       
    elif selectedwell.inflow =='Standing':
        models = StandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('opinflow:list_inflow')  
        standingmodel = StandingsModel()
        standingmodel.fgid = selectedwell.fgid
        standingmodel.wellid = selectedwell.wellid  
        form = StandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":           
            standingmodel.fgid = selectedwell.fgid
            standingmodel.wellid = selectedwell.wellid
            form = StandingsForm(request.POST or None, instance=standingmodel)          
            if form.is_valid(): 
                form.save()
                chart = draw_LayerIPR_Standing(standingmodel) 
                return redirect ('opinflow:list_inflow')             
        return render (request, 'opinflow/standing_form.html', {'form': form})   
    elif selectedwell.inflow =='Wiggins':
        models = WigginsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('opinflow:list_inflow')  
        wigginmodel = WigginsModel()
        wigginmodel.fgid = selectedwell.fgid
        wigginmodel.wellid = selectedwell.wellid  
        form = WigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":
            wigginmodel.fgid = selectedwell.fgid
            wigginmodel.wellid = selectedwell.wellid
            form = WigginsForm(request.POST or None, instance=wigginmodel)          
            if form.is_valid(): 
                form.save() 
                chart=draw_LayerIPR_Wiggin(wigginmodel)
                return redirect ('opinflow:list_inflow')             
        return render (request, 'opinflow/wiggin_form.html', {'form': form})   
    elif selectedwell.inflow =='MultiRate':
        models = MultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('opinflow:list_inflow')  
        multiratemodel = MultirateModel()
        multiratemodel.fgid = selectedwell.fgid
        multiratemodel.wellid = selectedwell.wellid  
        form = MultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":
            multiratemodel.fgid = selectedwell.fgid
            form = MultiRateForm(request.POST or None, instance=multiratemodel)          
            if form.is_valid(): 
                form.save() 
                chart= draw_LayerIPR_Multirate(multiratemodel)
                loglogchart = draw_Multirateloglogplot(multiratemodel) 
                return render (request, 'opinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})                           
        return render (request, 'opinflow/multirate_form.html', {'form': form})     
    elif selectedwell.inflow =='Darcy':
        models = DarcyModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('opinflow:list_inflow')  
        darcymodel = DarcyModel()
        darcymodel.fgid = selectedwell.fgid
        darcymodel.wellid = selectedwell.wellid 
        form = DarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":
            darcymodel = DarcyModel()
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
            form = DarcyModelForm(request.POST or None, instance=darcymodel)          
            if form.is_valid(): 
                form.save() 
                chart = draw_LayerIPR_Darcy(darcymodel)
                return render (request,'opinflow/darcy_form.html', {'form': form, 'chart':chart})             
        return render (request, 'opinflow/darcy_form.html', {'form': form })   
   
def update_inflow(request, id):
    selectedwell = SelectedOilProducer.objects.first()
    if selectedwell.inflow =='PI':
        pimodel = ProductivityIndexModel.objects.get(id=id)
        print(pimodel)
        chart= draw_LayerIPR_PI(pimodel)
        form = ProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_PI(pimodel)
                return render (request, 'opinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})
        return render (request, 'opinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = VogelModel.objects.get(id=id)
        chart= draw_LayerIPR_Vogel(vogelmodel)
        form = VogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'opinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
        return render (request, 'opinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
    elif selectedwell.inflow =='Standing':
        standingmodel = StandingsModel.objects.get(id=id)
        chart= draw_LayerIPR_Standing(standingmodel) 
        form = StandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Standing(standingmodel) 
                return render (request, 'opinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
        return render (request, 'opinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
    elif selectedwell.inflow =='Wiggins':
        wigginmodel = WigginsModel.objects.get(id=id)
        chart= draw_LayerIPR_Wiggin(wigginmodel) 
        form = WigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Wiggin(wigginmodel)
                return render (request, 'opinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
        return render (request, 'opinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = MultirateModel.objects.get(id=id)
        chart= draw_LayerIPR_Multirate(multiratemodel) 
        loglogchart = draw_Multirateloglogplot(multiratemodel) 
        form = MultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()                
                chart= draw_LayerIPR_Multirate(multiratemodel)
                return render (request, 'opinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
        return render (request, 'opinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
    elif selectedwell.inflow =='Darcy':
        darcymodel = DarcyModel.objects.get(id=id)  
        chart= draw_LayerIPR_Darcy(darcymodel)      
        form = DarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":        
            if form.is_valid():
                darcymodel.save()
                chart= draw_LayerIPR_Darcy(darcymodel)
                return render (request, 'opinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart}) 
        return render (request, 'opinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart})      
        
def delete_inflow(request, id):
    selectedwell = SelectedOilProducer.objects.first()  
    if selectedwell.inflow =='PI':
        pimodel = ProductivityIndexModel.objects.get(id=id)  
        if request.method == 'POST' :
            pimodel.delete()
            return redirect ('opinflow:list_inflow')
        return render (request, 'opinflow/pindex_confirm_delete.html', {'pimodel':pimodel})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = VogelModel.objects.get(id=id)  
        if request.method == 'POST' :
            vogelmodel.delete()
            return redirect ('opinflow:list_inflow')
        return render (request, 'opinflow/vogel_confirm_delete.html', {'vogelmodel':vogelmodel})   
    elif selectedwell.inflow =='Standing':
        standingmodel = StandingsModel.objects.get(id=id)  
        if request.method == 'POST' :
            standingmodel.delete()
            return redirect ('opinflow:list_inflow')
        return render (request, 'opinflow/standing_confirm_delete.html', {'standingmodel':standingmodel})  
    elif selectedwell.inflow =='Wiggins':
        wigginsmodel = WigginsModel.objects.get(id=id)  
        if request.method == 'POST' :
            wigginsmodel.delete()
            return redirect ('opinflow:list_inflow')
        return render (request, 'opinflow/wiggin_confirm_delete.html', {'wigginsmodel':wigginsmodel}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = MultirateModel.objects.get(id=id)  
        if request.method == 'POST' :
            multiratemodel.delete()
            return redirect ('opinflow:list_inflow')
        return render (request, 'opinflow/multirate_confirm_delete.html', {'multiratemodel':multiratemodel}) 
    elif selectedwell.inflow =='Darcy':
        darcymodel = DarcyModel.objects.get(id=id)  
        if request.method == 'POST' :
            darcymodel.delete()
            return redirect ('opinflow:list_inflow')
        return render (request, 'opinflow/darcy_confirm_delete.html', {'darcymodel':darcymodel}) 
   

