from django.shortcuts import render, redirect
from .models import PressureBuildupTestDesignModel
from .forms import PBUTestDesignForm
from selectedOilProducer.models import SelectedOilProducer
from .utils import get_plot, design_buildup_test, horner_method

def list_pbu_test_design(request):     
    well = SelectedOilProducer.objects.all().first()   
    designs= PressureBuildupTestDesignModel.objects.filter(wellid=well.wellid).all()
    design = designs.last()
    if design :
        Q= design.design_Rate 
        k=design.layer_Permeability
        h=design.layer_Thickness
        mu=design.mu_oil
        ct = design.total_Compressibility
    else:
        Q= 1000 
        k=100
        h=50
        mu=0.45
        ct = 0.000065
    t, p_true, p_measured = design_buildup_test(Q, k, h, mu, ct)
    print(t,p_true, p_measured)
    m, b = horner_method(p_measured, t)
    print ("m=", m , "b=", b )
    chart = get_plot(t, p_measured,m,b)
    return render (request, 'builduptestdesign/pbudesign.html', {'designs': designs,'chart':chart })

def create_pbu_test_design(request):   
    design = PressureBuildupTestDesignModel()
    selectedwell = SelectedOilProducer.objects.first()  
    design.fgid = selectedwell.fgid
    design.wellid = selectedwell.wellid   
    form = PBUTestDesignForm(request.POST or None, instance=design)
    if request.method =="POST":  
        form = PBUTestDesignForm(request.POST, request.FILES, instance=design)       
        design.fgid = selectedwell.fgid
        design.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('builduptestdesign:list_pbu_test_design')
    return render (request, 'builduptestdesign/pbudesign_form.html', {'form': form})

def update_pbu_test_design(request, id):
    design = PressureBuildupTestDesignModel.objects.get(id=id)
    form = PBUTestDesignForm(request.POST or None, instance=design)
    if form.is_valid():
        form.save()
        return redirect ('builduptestdesign:list_pbu_test_design')
    return render (request, 'builduptestdesign/pbudesign_form.html', {'form': form, 'design':design})

def delete_pbu_test_design(request, id):
    design = PressureBuildupTestDesignModel.objects.get(id=id)    
    if request.method == 'POST' :
        design.delete()
        return redirect ('builduptestdesign:list_pbu_test_design')
    return render (request, 'builduptestdesign/pbudesign_confirm_delete.html', {'design':design})

