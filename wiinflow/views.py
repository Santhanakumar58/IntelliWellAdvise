from ast import Global
from decimal import Decimal
import math
from django.shortcuts import render, redirect
from blackoilpvt.models import BlackoilPVT
from blackoilpvt.utils import get_Bo, get_Pb, get_Viscosity
from selectedOilProducer.models import SelectedOilProducer
from .models import WIProductivityIndexModel, WIVogelModel, WIStandingsModel, WIWigginsModel, WIMultirateModel, WIDarcyModel
from .forms import WIProductivityIndexForm, WIStandingsForm, WIVogelForm, WIWigginsForm, WIMultiRateForm, WIDarcyModelForm
from .utils import draw_CompositeIPR_Darcy, draw_CompositeIPR_Multirate, draw_CompositePR_PI, draw_LayerIPR_Darcy, draw_LayerIPR_Multirate, draw_LayerIPR_PI, draw_LayerIPR_Standing, draw_LayerIPR_Vogel, draw_LayerIPR_Wiggin, draw_Multirateloglogplot, draw_compositeIPR_Standing, draw_compositeIPR_Vogel, draw_compositeIPR_Wiggins

def list_wiinflow(request): 
    selectedwell = SelectedOilProducer.objects.first() 
    if selectedwell.inflow =='PI':
        pimodels = WIProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        chart,xc,y,pis = draw_CompositePR_PI(pimodels)
        return render (request, 'wiinflow/pindex.html', {'pimodels': pimodels, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodels = WIVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        print((vogelmodels))
        chart = draw_compositeIPR_Vogel(vogelmodels)        
        return render (request, 'wiinflow/vogel.html', {'vogelmodels': vogelmodels, 'chart':chart})  
    elif selectedwell.inflow =='Standing':
        standingmodels = WIStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        print (len(standingmodels))
        chart = draw_compositeIPR_Standing(standingmodels)                  
        return render (request, 'wiinflow/standing.html', {'standingmodels': standingmodels, 'chart':chart})  
    elif selectedwell.inflow =='Wiggins':
        wigginmodels = WIWigginsModel.objects.filter(wellid=selectedwell.wellid).all()        
        chart = draw_compositeIPR_Wiggins(wigginmodels)         
        return render (request, 'wiinflow/wiggin.html', {'wigginmodels': wigginmodels, 'chart':chart}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodels = WIMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        chart =draw_CompositeIPR_Multirate(multiratemodels)         
        return render (request, 'wiinflow/multirate.html', {'multiratemodels': multiratemodels, 'chart':chart})
    elif selectedwell.inflow =='Darcy':        
        darcymodels = WIDarcyModel.objects.filter(wellid=selectedwell.wellid).all()  
        chart = draw_CompositeIPR_Darcy(darcymodels) 
        return render (request, 'wiinflow/darcy.html', {'darcymodels': darcymodels, 'chart':chart})       

def create_wiinflow(request):
    selectedwell = SelectedOilProducer.objects.first()    
    if selectedwell.inflow =='PI':
        models = WIProductivityIndexModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('wiinflow:list_inflow')  
        pimodel = WIProductivityIndexModel()
        pimodel.fgid = selectedwell.fgid
        pimodel.wellid = selectedwell.wellid  
        form = WIProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":           
            pimodel.fgid = selectedwell.fgid
            pimodel.wellid = selectedwell.wellid            
            form = WIProductivityIndexForm(request.POST or None, instance=pimodel)          
            if form.is_valid(): 
                form.save() 
                print(pimodel)
                chart = draw_LayerIPR_PI(pimodel)
                return render (request, 'wiinflow/pindex_form.html', {'form': form, 'chart':chart})             
        return render (request, 'wiinflow/pindex_form.html', {'form': form})             
    elif selectedwell.inflow =='Vogel':
        models = WIVogelModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('wiinflow:list_inflow')  
        vogelmodel = WIVogelModel()
        vogelmodel.fgid = selectedwell.fgid
        vogelmodel.wellid = selectedwell.wellid  
        form = WIVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":           
            vogelmodel.fgid = selectedwell.fgid
            vogelmodel.wellid = selectedwell.wellid
            form = WIVogelForm(request.POST or None, instance=vogelmodel)          
            if form.is_valid(): 
                vogelmodel.fgid = selectedwell.fgid
                vogelmodel.wellid = selectedwell.wellid
                vogelmodel.save() 
                print(vogelmodel)
                chart = draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'wiinflow/vogel_form.html', {'form': form, 'chart':chart})              
        return render (request, 'wiinflow/vogel_form.html', {'form': form})       
    elif selectedwell.inflow =='Standing':
        models = WIStandingsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('wiinflow:list_inflow')  
        standingmodel = WIStandingsModel()
        standingmodel.fgid = selectedwell.fgid
        standingmodel.wellid = selectedwell.wellid  
        form = WIStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":           
            standingmodel.fgid = selectedwell.fgid
            standingmodel.wellid = selectedwell.wellid
            form = WIStandingsForm(request.POST or None, instance=standingmodel)          
            if form.is_valid(): 
                form.save()
                chart = draw_LayerIPR_Standing(standingmodel) 
                return redirect ('wiinflow:list_inflow')             
        return render (request, 'wiinflow/standing_form.html', {'form': form})   
    elif selectedwell.inflow =='Wiggins':
        models = WIWigginsModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('wiinflow:list_inflow')  
        wigginmodel = WIWigginsModel()
        wigginmodel.fgid = selectedwell.fgid
        wigginmodel.wellid = selectedwell.wellid  
        form = WIWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":
            wigginmodel.fgid = selectedwell.fgid
            wigginmodel.wellid = selectedwell.wellid
            form = WIWigginsForm(request.POST or None, instance=wigginmodel)          
            if form.is_valid(): 
                form.save() 
                chart=draw_LayerIPR_Wiggin(wigginmodel)
                return redirect ('wiinflow:list_inflow')             
        return render (request, 'wiinflow/wiggin_form.html', {'form': form})   
    elif selectedwell.inflow =='MultiRate':
        models = WIMultirateModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('wiinflow:list_inflow')  
        multiratemodel = WIMultirateModel()
        multiratemodel.fgid = selectedwell.fgid
        multiratemodel.wellid = selectedwell.wellid  
        form = WIMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":
            multiratemodel.fgid = selectedwell.fgid
            form = WIMultiRateForm(request.POST or None, instance=multiratemodel)          
            if form.is_valid(): 
                form.save() 
                chart= draw_LayerIPR_Multirate(multiratemodel)
                loglogchart = draw_Multirateloglogplot(multiratemodel) 
                return render (request, 'wiinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})                           
        return render (request, 'wiinflow/multirate_form.html', {'form': form})     
    elif selectedwell.inflow =='Darcy':
        models = WIDarcyModel.objects.filter(wellid=selectedwell.wellid).all()
        if len(models) ==4 :            
            return redirect ('wiinflow:list_inflow')  
        darcymodel = WIDarcyModel()
        darcymodel.fgid = selectedwell.fgid
        darcymodel.wellid = selectedwell.wellid 
        form = WIDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":
            darcymodel = WIDarcyModel()
            darcymodel.fgid = selectedwell.fgid                   
            form = WIDarcyModelForm(request.POST or None, instance=darcymodel)          
            if form.is_valid(): 
                form.save() 
                chart = draw_LayerIPR_Darcy(darcymodel)
                return render (request,'wiinflow/darcy_form.html', {'form': form, 'chart':chart})             
        return render (request, 'wiinflow/darcy_form.html', {'form': form })   
   
def update_wiinflow(request, id):
    selectedwell = SelectedOilProducer.objects.first()
    if selectedwell.inflow =='PI':
        pimodel = WIProductivityIndexModel.objects.get(id=id)
        print(pimodel)
        chart= draw_LayerIPR_PI(pimodel)
        form = WIProductivityIndexForm(request.POST or None, instance=pimodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_PI(pimodel)
                return render (request, 'wiinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})
        return render (request, 'wiinflow/pindex_form.html', {'form': form, 'pimodel':pimodel, 'chart':chart})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = WIVogelModel.objects.get(id=id)
        chart= draw_LayerIPR_Vogel(vogelmodel)
        form = WIVogelForm(request.POST or None, instance=vogelmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Vogel(vogelmodel)
                return render (request, 'wiinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
        return render (request, 'wiinflow/vogel_form.html', {'form': form, 'vogelmodel':vogelmodel, 'chart':chart})
    elif selectedwell.inflow =='Standing':
        standingmodel = WIStandingsModel.objects.get(id=id)
        chart= draw_LayerIPR_Standing(standingmodel) 
        form = WIStandingsForm(request.POST or None, instance=standingmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Standing(standingmodel) 
                return render (request, 'wiinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
        return render (request, 'wiinflow/standing_form.html', {'form': form, 'standingmodel':standingmodel, 'chart':chart})
    elif selectedwell.inflow =='Wiggins':
        wigginmodel = WIWigginsModel.objects.get(id=id)
        chart= draw_LayerIPR_Wiggin(wigginmodel) 
        form = WIWigginsForm(request.POST or None, instance=wigginmodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()
                chart= draw_LayerIPR_Wiggin(wigginmodel)
                return render (request, 'wiinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
        return render (request, 'wiinflow/wiggin_form.html', {'form': form, 'wigginmodel':wigginmodel, 'chart':chart})
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = WIMultirateModel.objects.get(id=id)
        chart= draw_LayerIPR_Multirate(multiratemodel) 
        loglogchart = draw_Multirateloglogplot(multiratemodel) 
        form = WIMultiRateForm(request.POST or None, instance=multiratemodel)
        if request.method =="POST":        
            if form.is_valid():
                form.save()                
                chart= draw_LayerIPR_Multirate(multiratemodel)
                return render (request, 'wiinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
        return render (request, 'wiinflow/multirate_form.html', {'form': form, 'multiratemodel':multiratemodel, 'chart':chart, 'loglogchart':loglogchart})
    elif selectedwell.inflow =='Darcy':
        darcymodel = WIDarcyModel.objects.get(id=id)  
        chart= draw_LayerIPR_Darcy(darcymodel)      
        form = WIDarcyModelForm(request.POST or None, instance=darcymodel)
        if request.method =="POST":        
            if form.is_valid():
                darcymodel.save()
                chart= draw_LayerIPR_Darcy(darcymodel)
                return render (request, 'wiinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart}) 
        return render (request, 'wiinflow/darcy_form.html', {'form': form, 'darcymodel':darcymodel, 'chart':chart})      
        
def delete_wiinflow(request, id):
    selectedwell = SelectedOilProducer.objects.first()  
    if selectedwell.inflow =='PI':
        pimodel = WIProductivityIndexModel.objects.get(id=id)  
        if request.method == 'POST' :
            pimodel.delete()
            return redirect ('wiinflow:list_inflow')
        return render (request, 'wiinflow/pindex_confirm_delete.html', {'pimodel':pimodel})  
    elif selectedwell.inflow =='Vogel':
        vogelmodel = WIVogelModel.objects.get(id=id)  
        if request.method == 'POST' :
            vogelmodel.delete()
            return redirect ('wiinflow:list_inflow')
        return render (request, 'wiinflow/vogel_confirm_delete.html', {'vogelmodel':vogelmodel})   
    elif selectedwell.inflow =='Standing':
        standingmodel = WIStandingsModel.objects.get(id=id)  
        if request.method == 'POST' :
            standingmodel.delete()
            return redirect ('wiinflow:list_inflow')
        return render (request, 'wiinflow/standing_confirm_delete.html', {'standingmodel':standingmodel})  
    elif selectedwell.inflow =='Wiggins':
        wigginsmodel = WIWigginsModel.objects.get(id=id)  
        if request.method == 'POST' :
            wigginsmodel.delete()
            return redirect ('wiinflow:list_inflow')
        return render (request, 'wiinflow/wiggin_confirm_delete.html', {'wigginsmodel':wigginsmodel}) 
    elif selectedwell.inflow =='MultiRate':
        multiratemodel = WIMultirateModel.objects.get(id=id)  
        if request.method == 'POST' :
            multiratemodel.delete()
            return redirect ('wiinflow:list_inflow')
        return render (request, 'wiinflow/multirate_confirm_delete.html', {'multiratemodel':multiratemodel}) 
    elif selectedwell.inflow =='Darcy':
        darcymodel = WIDarcyModel.objects.get(id=id)  
        if request.method == 'POST' :
            darcymodel.delete()
            return redirect ('wiinflow:list_inflow')
        return render (request, 'wiinflow/darcy_confirm_delete.html', {'darcymodel':darcymodel}) 
   


