from django.shortcuts import render, redirect
from .models import GPPressureBuildupTestDesignModel
from .forms import GPPBUTestDesignForm
from selectedGasProducer.models import SelectedGasProducer
from .utils import get_plot, design_buildup_test, horner_method

def list_gppbu_test_design(request):     
    well = SelectedGasProducer.objects.all().first()   
    designs= GPPressureBuildupTestDesignModel.objects.filter(gpwellid=well.wellid).all()
    design = designs.last()
    if design :
        Q= design.design_Rate 
        k=design.layer_Permeability
        h=design.layer_Thickness
        mu=design.mu_oil
        ct = design.total_Compressibility
    else :
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
     
    return render (request, 'gpbuilduptestdesign/gppbudesign.html', {'designs': designs,'chart':chart })

def create_gppbu_test_design(request):   
    design = GPPressureBuildupTestDesignModel()
    selectedwell = SelectedGasProducer.objects.first()  
    design.fgid = selectedwell.fgid
    design.wellid = selectedwell.wellid   
    form = GPPBUTestDesignForm(request.POST or None, instance=design)
    if request.method =="POST":  
        form = GPPBUTestDesignForm(request.POST, request.FILES, instance=design)       
        design.fgid = selectedwell.fgid
        design.wellid = selectedwell.wellid  
    if form.is_valid():
        form.save()
        return redirect ('builduptestdesign:list_gppbu_test_design')
    return render (request, 'builduptestdesign/gppbudesign_form.html', {'form': form})

def update_gppbu_test_design(request, id):
    design = GPPressureBuildupTestDesignModel.objects.get(id=id)
    form = GPPBUTestDesignForm(request.POST or None, instance=design)
    if form.is_valid():
        form.save()
        return redirect ('gpbuilduptestdesign:list_gppbu_test_design')
    return render (request, 'gpbuilduptestdesign/gppbudesign_form.html', {'form': form, 'design':design})

def delete_gppbu_test_design(request, id):
    design = GPPressureBuildupTestDesignModel.objects.get(id=id)    
    if request.method == 'POST' :
        design.delete()
        return redirect ('gpbuilduptestdesign:list_gppbu_test_design')
    return render (request, 'gpbuilduptestdesign/gppbudesign_confirm_delete.html', {'design':design})

