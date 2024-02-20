from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from IntelligentOilWell.custom_context_processors import selectedfgi
from django.contrib import messages
from .models import FluidCompositionData 
from .forms import FluidCompositionDataForm
from reservoirfluidcomposition.models import FluidComposition
from sublayers.models import Sublayer
from tablib import Dataset
from selectedfgi.models import Selectedfgi
 
 
def list_fluid_composition_data(request, fcid):
    fc = FluidComposition.objects.get(id=fcid)
    fcdatas = FluidCompositionData.objects.filter(fluidcomposition = fc)   
    fcdatas = FluidCompositionData.objects.filter(fluidcomposition=fc)  
    total_weight_percent =0.0
    total_mol_percent=0.0
    for data in  fcdatas:
       total_mol_percent += data.mole_Percent
       total_weight_percent += data.weight_Percent 
    return render (request, 'reservoirfluidcompositiondata/fluid_compositiondata.html', {'fcdatas': fcdatas, "fcid":fcid, 'total_mol_percent': total_mol_percent, 'total_weight_percent':total_weight_percent})
    
def create_fluid_composition_data(request, fcid): 
   fc = FluidComposition.objects.get(id = fcid)
   fcdata= FluidCompositionData() 
   fcdata.fluidcomposition = fc 
   form = FluidCompositionDataForm(request.POST or None, instance=fcdata)  
   if request.method =="POST":        
        component = request.POST["component"]
        mole_weight = request.POST["molecular_Weight"]
        if mole_weight == 0 or mole_weight == None:
            molecularweight = get_molecular_weight(component)
            fcdata.molecular_Weight = molecularweight
        form = FluidCompositionDataForm(request.POST, instance=fcdata)  
        if form.is_valid():
            form.save() 
            return redirect ('reservoirfluidcompositiondata:list_fluid_composition_data', fcid)    
   return render (request, 'reservoirfluidcompositiondata/fluid_compositiondata_form.html', {'form': form, 'fcid':fcid})

def update_fluid_composition_data(request, id):
    fcdata = FluidCompositionData.objects.get(id=id)   
    fcid = (fcdata.fluidcomposition).pk  
    form = FluidCompositionDataForm(request.POST or None, instance=fcdata)
    if request.method == "POST":
      component = request.POST["component"]
      molecularweight = request.POST["molecular_Weight"]       
      if molecularweight =="0.0" or molecularweight == None:
         molecularweight = get_molecular_weight(component)
         fcdata.molecular_Weight = molecularweight  
      form = FluidCompositionDataForm(request.POST, instance=fcdata)   
      if form.is_valid():
         fcdata.molecular_Weight = molecularweight             
         form.save()
         return redirect ('reservoirfluidcompositiondata:list_fluid_composition_data', fcid)
    return render (request, 'reservoirfluidcompositiondata/fluid_compositiondata_form.html', {'form': form, 'fcdata':fcdata, 'id':id})

def delete_fluid_composition_data(request, id):
    fcdata = FluidCompositionData.objects.get(id=id)   
    fcid = (fcdata.fluidcomposition).pk  
    if request.method == 'POST' :
        fcdata.delete()
        return redirect ('reservoirfliudcompositiondata:list_fluid_composition_data', fcid)
    return render (request, 'reservoirfliudcompositiondata/fluid_compositiondata_confirm_delete.html', {'fcdata':fcdata, 'id':id})



def  get_molecular_weight(component):
   print(component)
   molecularweight=0
   if component == "Hydrogen_Sulfide":
      molecularweight = 34.08 
   elif component == "Carbon_Dioxide":
      molecularweight = 44.01
   elif component == "Nitrogen":
      molecularweight = 28.013
   elif component == "Methane":
      molecularweight = 16.043
   elif component == "Ethane":
      molecularweight = 30.07        
   elif component == "Propane":
      molecularweight = 44.097    
   elif component == "iso-Butane":
      molecularweight = 58.124
   elif component == "n-Butane":
      molecularweight = 58.124 
   elif component == "iso-Pentane":
      molecularweight = 72.151
   elif component == "n-Pentane":
      molecularweight = 72.151     
   elif component == "Hexanes":
      molecularweight = 86.178  
   elif component == "Heptanes":
      molecularweight = 100.205 
   elif component == "Octanes":
      molecularweight = 114.232
   elif component == "Nonanes":
      molecularweight = 128.259
   elif component == "Decanes":
      molecularweight = 142.286 
   elif component == "Undecanes":
      molecularweight = 156.30   
   elif component == "Dodecanes":
      molecularweight = 170.33
   elif component == "Tridecanes":
      molecularweight = 184.35
   elif component == "Tetradecanes":
      molecularweight =198.38
   elif component == "Pentadecanes":
      molecularweight = 212.41  
   elif component == "Hexadecanes":
      molecularweight = 226.43    
   elif component == "Heptadecanes":
      molecularweight = 240.46
   elif component == "Octadecanes":
      molecularweight = 254.48
   elif component == "Nonadecanes":
      molecularweight = 268.51
   elif component == "Eicosanes":
      molecularweight = 282.54
   elif component == "Heneicosanes":
      molecularweight = 296.56  
   elif component == "Docosanes":
      molecularweight =310.59 
   elif component == "Tricosanes":
      molecularweight = 324.61
   elif component == "Tetracosanes":
      molecularweight = 338.64
   elif component == "Pentacosanes":
      molecularweight = 352.67 
   elif component == "Hexacosanes":
      molecularweight = 366.69    
   elif component == "Heptacosanes":
      molecularweight = 380.72
   elif component == "Octacosanes":
      molecularweight = 394.74
   elif component == "Nonacosanes":
      molecularweight = 408.77  
   print(molecularweight)  
   return molecularweight


