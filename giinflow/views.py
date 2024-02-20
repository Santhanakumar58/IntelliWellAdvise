from ast import Global
from decimal import Decimal
import math
from django.shortcuts import render, redirect
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity
from selectedOilProducer.models import SelectedOilProducer
from .models import GIProductivityIndexModel, GIVogelModel, GIStandingsModel, GIWigginsModel, GIMultirateModel, GIDarcyModel
from .forms import GIProductivityIndexForm, GIStandingsForm, GIVogelForm, GIWigginsForm, GIMultiRateForm, GIDarcyModelForm
from .utils import draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_CompositePR_PI, draw_LayerIPR_Darcy, draw_LayerIPR_Multirate, draw_LayerIPR_PI, draw_LayerIPR_Standing, draw_LayerIPR_Vogel, draw_LayerIPR_Wiggin, draw_Multirateloglogplot, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins

def list_giinflow(request): 
    selectedwell = SelectedOilProducer.objects.first() 
    if selectedwell.inflow =='PI':
        pimodels = GIProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y,pis = draw_CompositePR_PI(pimodels)
        return render (request, 'giinflow/pindex.html', {'pimodels': pimodels, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodels = GIVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        print((vogelmodels))
        chart = draw_compositeIPR_Vogel(vogelmodels)        
        return render (request, 'giinflow/vogel.html', {'vogelmodels': vogelmodels, 'chart':chart})  
    elif selectedwell.inflow =='Standing':
        standingmodels = GIStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        print (len(standingmodels))
        chart = draw_compositeIPR_Standing(standingmodels)                  
        return render (request, 'giinflow/standing.html', {'standingmodels': standingmodels, 'chart':chart})  
    elif selectedwell.inflow =='Wiggins':
        wigginmodels = GIWigginsModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart = draw_compositeIPR_Wiggins(wigginmodels)         
        return render (request, 'giinflow/wiggin.html', {'wigginmodels': wigginmodels, 'chart':chart}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodels = GIMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        chart =draw_CompositeIPR_Multirate(multiratemodels)         
        return render (request, 'giinflow/multirate.html', {'multiratemodels': multiratemodels, 'chart':chart})
    elif selectedwell.inflow =='Darcy':        
        darcymodels = GIDarcyModel.objects.filter(wellid=selectedwell.wellid).all()  
        chart = draw_CompositeIPR_Darcy(darcymodels) 
        return render (request, 'giinflow/darcy.html', {'darcymodels': darcymodels, 'chart':chart})       

def create_giinflow(request):
    selectedwell = SelectedOilProducer.objects.first()    
    if selectedwell.inflow =='PI':
        models = GIProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('giinflow:list_inflow')  
        pimodel = GIProductivityIndexModel()
        pimodel.fgid = selectedwell.fgid
        pimodel.wellid = selectedwell.wellid  
        form = GIProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":           
            pimodel.fgid = selectedwell.fgid
            pimodel.wellid = selectedwell.wellid            
            form = GIProductivityIndexForm(request.POST or None, instance=pimodel)          
            if form.is_valid(): 
                form.save() 
                print(pimodel)
                chart = draw_LayerIPR_PI(pimodel)
                return render (request, 'giinflow/pindex_form.html', {'form': form, 'chart':chart})             
        return render (request, 'giinflow/pindex_form.html', {'form': form})             
    elif selectedwell.inflow =='Vogel':
        models = GIVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('giinflow:list_inflow')  
        vogelmodel = GIVogelModel()
        vogelmodel.fgid = selectedwell.fgid
        vogelmodel.wellid = selectedwell.wellid  
        form = GIVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":           
            vogelmodel.fgid = selectedwell.fgid
            vogelmodel.wellid = selectedwell.wellid
            form = GIVogelForm(request.POST or None, instance=vogelmodel)          
            if form.is_valid(): 
                vogelmodel.fgid = selectedwell.fgid
                vogelmodel.wellid = selectedwell.wellid
                vogelmodel.save() 
                print(vogelmodel)
                chart = draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'giinflow/vogel_form.html', {'form': form, 'chart':chart})              
        return render (request, 'giinflow/vogel_form.html', {'form': form})       
    elif selectedwell.inflow =='Standing':
        models = GIStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('giinflow:list_inflow')  
        standingmodel = GIStandingsModel()
        standingmodel.fgid = selectedwell.fgid
        standingmodel.wellid = selectedwell.wellid  
        form = GIStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":           
            standingmodel.fgid = selectedwell.fgid
            standingmodel.wellid = selectedwell.wellid
            form = GIStandingsForm(request.POST or None, instance=standingmodel)          
            if form.is_valid(): 
                form.save()
                chart = draw_LayerIPR_Standing(standingmodel) 
                return redirect ('giinflow:list_inflow')             
        return render (request, 'giinflow/standing_form.html', {'form': form})   
    elif selectedwell.inflow =='Wiggins':
        models = GIWigginsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('giinflow:list_inflow')  
        wigginmodel = GIWigginsModel()
        wigginmodel.fgid = selectedwell.fgid
        wigginmodel.wellid = selectedwell.wellid  
        form = GIWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":
            wigginmodel.fgid = selectedwell.fgid
            wigginmodel.wellid = selectedwell.wellid
            form = GIWigginsForm(request.POST or None, instance=wigginmodel)          
            if form.is_valid(): 
                form.save() 
                chart=draw_LayerIPR_Wiggin(wigginmodel)
                return redirect ('giinflow:list_inflow')             
        return render (request, 'giinflow/wiggin_form.html', {'form': form})   
    elif selectedwell.inflow =='MultiRate':
        models = GIMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('giinflow:list_inflow')  
        multiratemodel = GIMultirateModel()
        multiratemodel.fgid = selectedwell.fgid
        multiratemodel.wellid = selectedwell.wellid  
        form = GIMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":
            multiratemodel.fgid = selectedwell.fgid
            form = GIMultiRateForm(request.POST or None, instance=multiratemodel)          
            if form.is_valid(): 
                form.save() 
                chart= draw_LayerIPR_Multirate(multiratemodel)
                loglogchart = draw_Multirateloglogplot(multiratemodel) 
                return render (request, 'giinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})                           
        return render (request, 'giinflow/multirate_form.html', {'form': form})     
    elif selectedwell.inflow =='Darcy':
        models = GIDarcyModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('giinflow:list_inflow')  
        darcymodel = GIDarcyModel()
        darcymodel.fgid = selectedwell.fgid
        darcymodel.wellid = selectedwell.wellid 
        form = GIDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":
            darcymodel = GIDarcyModel()
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
            form = GIDarcyModelForm(request.POST or None, instance=darcymodel)          
            if form.is_valid(): 
                form.save() 
                chart = draw_LayerIPR_Darcy(darcymodel)
                return render (request,'giinflow/darcy_form.html', {'form': form, 'chart':chart})             
        return render (request, 'giinflow/darcy_form.html', {'form': form })   
   
def update_giinflow(request, id):
    selectedwell = SelectedOilProducer.objects.first()
    if selectedwell.inflow =='PI':
        pimodel = GIProductivityIndexModel.objects.get(id=id)
        print(pimodel)
        chart= draw_LayerIPR_PI(pimodel)
        form = GIProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_PI(pimodel)
                return render (request, 'giinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})
        return render (request, 'giinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = GIVogelModel.objects.get(id=id)
        chart= draw_LayerIPR_Vogel(vogelmodel)
        form = GIVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'giinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
        return render (request, 'giinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
    elif selectedwell.inflow =='Standing':
        standingmodel = GIStandingsModel.objects.get(id=id)
        chart= draw_LayerIPR_Standing(standingmodel) 
        form = GIStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Standing(standingmodel) 
                return render (request, 'giinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
        return render (request, 'giinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
    elif selectedwell.inflow =='Wiggins':
        wigginmodel = GIWigginsModel.objects.get(id=id)
        chart= draw_LayerIPR_Wiggin(wigginmodel) 
        form = GIWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Wiggin(wigginmodel)
                return render (request, 'giinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
        return render (request, 'giinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = GIMultirateModel.objects.get(id=id)
        chart= draw_LayerIPR_Multirate(multiratemodel) 
        loglogchart = draw_Multirateloglogplot(multiratemodel) 
        form = GIMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()                
                chart= draw_LayerIPR_Multirate(multiratemodel)
                return render (request, 'giinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
        return render (request, 'giinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
    elif selectedwell.inflow =='Darcy':
        darcymodel = GIDarcyModel.objects.get(id=id)  
        chart= draw_LayerIPR_Darcy(darcymodel)      
        form = GIDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":        
            if form.is_valid():
                darcymodel.save()
                chart= draw_LayerIPR_Darcy(darcymodel)
                return render (request, 'giinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart}) 
        return render (request, 'giinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart})      
        
def delete_giinflow(request, id):
    selectedwell = SelectedOilProducer.objects.first()  
    if selectedwell.inflow =='PI':
        pimodel = GIProductivityIndexModel.objects.get(id=id)  
        if request.method == 'POST' :
            pimodel.delete()
            return redirect ('giinflow:list_inflow')
        return render (request, 'giinflow/pindex_confirm_delete.html', {'pimodel':pimodel})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = GIVogelModel.objects.get(id=id)  
        if request.method == 'POST' :
            vogelmodel.delete()
            return redirect ('giinflow:list_inflow')
        return render (request, 'giinflow/vogel_confirm_delete.html', {'vogelmodel':vogelmodel})   
    elif selectedwell.inflow =='Standing':
        standingmodel = GIStandingsModel.objects.get(id=id)  
        if request.method == 'POST' :
            standingmodel.delete()
            return redirect ('giinflow:list_inflow')
        return render (request, 'giinflow/standing_confirm_delete.html', {'standingmodel':standingmodel})  
    elif selectedwell.inflow =='Wiggins':
        wigginsmodel = GIWigginsModel.objects.get(id=id)  
        if request.method == 'POST' :
            wigginsmodel.delete()
            return redirect ('giinflow:list_inflow')
        return render (request, 'giinflow/wiggin_confirm_delete.html', {'wigginsmodel':wigginsmodel}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = GIMultirateModel.objects.get(id=id)  
        if request.method == 'POST' :
            multiratemodel.delete()
            return redirect ('giinflow:list_inflow')
        return render (request, 'giinflow/multirate_confirm_delete.html', {'multiratemodel':multiratemodel}) 
    elif selectedwell.inflow =='Darcy':
        darcymodel = GIDarcyModel.objects.get(id=id)  
        if request.method == 'POST' :
            darcymodel.delete()
            return redirect ('giinflow:list_inflow')
        return render (request, 'giinflow/darcy_confirm_delete.html', {'darcymodel':darcymodel}) 
   


