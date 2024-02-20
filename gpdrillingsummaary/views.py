from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import GPDrillingSummary
from .forms import DrillingSummaryForm
from selectedGasProducer.models import SelectedGasProducer

def list_gpdrillingsummary(request):
    selectedwell = SelectedGasProducer.objects.all().first()   
    d_summaries= GPDrillingSummary.objects.filter(gpwellid = selectedwell.wellid).all()   
    return render (request, 'gpdrillingsummaary/gpdrillingsummary.html', {'d_summaries': d_summaries})
    
def create_gpdrillingsummary(request):  
   selctedoilproducer = SelectedGasProducer.objects.all().first()   
   d_summary = GPDrillingSummary()   
   d_summary.fgId = selctedoilproducer.fgid
   d_summary.wellid= selctedoilproducer.wellid
   if request.method == "POST":
        liquid = float(request.POST["liquid_Rate"])
        wc = float(request.POST["water_Cut"])
        gor = float(request.POST["gas_Oil_Ratio"])
        print(type(liquid), type(wc), type(gor))
        oilrate = (liquid*(1.0-wc/100.0))  
        gasrate = round(oilrate*gor/1000)
        d_summary.oil_Rate = oilrate
        d_summary.gas_Rate = gasrate
   form = DrillingSummaryForm(request.POST or None, instance=d_summary)  
   if form.is_valid():
       form.save()       
       return redirect ('gpdrillingsummaary:list_gpdrillingsummary')    
   return render (request, 'gpdrillingsummaary/gpdrillingsummary_form.html', {'form': form})

def update_gpdrillingsummary(request, id):
    d_summary = GPDrillingSummary.objects.get(id=id)
    if request.method == "POST":
        liquid = float(request.POST["liquid_Rate"])
        wc = float(request.POST["water_Cut"])
        gor = float(request.POST["gas_Oil_Ratio"])
        print(type(liquid), type(wc), type(gor))
        oilrate = (liquid*(1.0-wc/100.0))  
        gasrate = round(oilrate*gor/1000)
        d_summary.oil_Rate = oilrate
        d_summary.gas_Rate = gasrate
    form = DrillingSummaryForm(request.POST or None, instance=d_summary)
    if form.is_valid():
       form.save()
       return redirect ('gpdrillingsummaary:list_gpdrillingsummary')
    return render (request, 'gpdrillingsummaary/gpdrillingsummary_form.html', {'form': form, 'd_summary':d_summary})

def delete_gpdrillingsummary(request, id):
    d_summary = GPDrillingSummary.objects.get(id=id)   
    if request.method == 'POST' :
       d_summary.delete()
       return redirect ('gpdrillingsummaary:list_gpdrillingsummary')
    return render (request, 'gpdrillingsummaary/gpdrillingsummary_confirm_delete.html', {'d_summary':d_summary})




