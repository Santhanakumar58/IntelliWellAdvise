from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import WIDrillingSummary
from .forms import WIDrillingSummaryForm
from selectedWaterInjector.models import SelectedWaterInjector

def list_widrillingsummary(request):
    selectedwell = SelectedWaterInjector.objects.all().first()   
    d_summaries= WIDrillingSummary.objects.filter(wiwellid = selectedwell.wellid).all()   
    return render (request, 'widrillingsummary/widrillingsummary.html', {'d_summaries': d_summaries})
    
def create_widrillingsummary(request):  
   selctedoilproducer = SelectedWaterInjector.objects.all().first()   
   d_summary = WIDrillingSummary()   
   d_summary.wifgId = selctedoilproducer.fgid
   d_summary.wiwellid= selctedoilproducer.wellid
   if request.method == "POST":
        liquid = float(request.POST["liquid_Rate"])
        wc = float(request.POST["water_Cut"])
        gor = float(request.POST["gas_Oil_Ratio"])
        print(type(liquid), type(wc), type(gor))
        oilrate = (liquid*(1.0-wc/100.0))  
        gasrate = round(oilrate*gor/1000)
        d_summary.oil_Rate = oilrate
        d_summary.gas_Rate = gasrate
   form = WIDrillingSummaryForm(request.POST or None, instance=d_summary)  
   if form.is_valid():
       form.save()       
       return redirect ('widrillingsummary:list_widrillingsummary')    
   return render (request, 'widrillingsummary/widrillingsummary_form.html', {'form': form})

def update_widrillingsummary(request, id):
    d_summary = WIDrillingSummary.objects.get(id=id)
    if request.method == "POST":
        liquid = float(request.POST["liquid_Rate"])
        wc = float(request.POST["water_Cut"])
        gor = float(request.POST["gas_Oil_Ratio"])
        print(type(liquid), type(wc), type(gor))
        oilrate = (liquid*(1.0-wc/100.0))  
        gasrate = round(oilrate*gor/1000)
        d_summary.oil_Rate = oilrate
        d_summary.gas_Rate = gasrate
    form = WIDrillingSummaryForm(request.POST or None, instance=d_summary)
    if form.is_valid():
       form.save()
       return redirect ('widrillingsummary:list_widrillingsummary')
    return render (request, 'widrillingsummary/widrillingsummary_form.html', {'form': form, 'd_summary':d_summary})

def delete_widrillingsummary(request, id):
    d_summary = WIDrillingSummary.objects.get(id=id)   
    if request.method == 'POST' :
       d_summary.delete()
       return redirect ('widrillingsummary:list_widrillingsummary')
    return render (request, 'widrillingsummary/widrillingsummary_confirm_delete.html', {'d_summary':d_summary})




