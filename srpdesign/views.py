from django.shortcuts import render, redirect
from selectedOilProducer.models import SelectedOilProducer
from .models import SRPDesignModel
from .forms import SRPDesignForm
from.utils import calculate_inflow, get_ipr_plot, calculate_srp_parameters

# Create your views here.
def list_srp_design_data(request):
    selectedwell = SelectedOilProducer.objects.first()   
    srpdatas = SRPDesignModel.objects.filter(wellid =selectedwell.wellid).all().order_by('-design_Date')  
    srpdata= srpdatas.first()   
    if srpdata:
        inflowdf, x1, y1, pip =calculate_inflow(srpdata, selectedwell)
        chart = get_ipr_plot(inflowdf, srpdata, x1, y1) 
        CBE = calculate_srp_parameters(srpdata)
        
        return render (request, 'srpdesign/srp_design_data.html', {'srpdatas': srpdatas, 'chart':chart})     
   
    
    #q,q1,q2,head,eff,power, rangex, rangey, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead= Generate_pump_curves(espdata)
    #chart1= get_esp_plot1(q,q1,q2,head,eff,power, rangex, rangey, pump_name)
    #chart2= get_esp_plot2(q,head, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead)
    #chart3 = vlp_curve_for_esp(espdata)    
    return render (request, 'srpdesign/srp_design_data.html', {'srpdatas': srpdatas})   
 
def create_srp_design_data(request):    
    srpdata = SRPDesignModel()
    selectedwell = SelectedOilProducer.objects.first()  
    srpdata.fgid = selectedwell.fgid
    srpdata.wellid = selectedwell.wellid 
    form = SRPDesignForm(request.POST or None, instance=srpdata)
    tdh =0
    if request.method =="POST":  
         form = SRPDesignForm(request.POST, request.FILES, instance=srpdata)       
         srpdata.fgid = selectedwell.fgid
         srpdata.wellid = selectedwell.wellid                       
         if form.is_valid():
            form.save()  
            return redirect ('srpdesign:list_srp_design_data') 
    return render (request, 'srpdesign/srp_design_data_form.html', {'form': form})

def update_srp_design_data(request, id): 
   srpdata = SRPDesignModel.objects.get(id=id)  
   form = SRPDesignForm(request.POST or None, instance=srpdata)   
   if request.method =="POST":
        form = SRPDesignForm(request.POST, request.FILES, instance=srpdata)        
        if form.is_valid():            
            form.save() 
            #return redirect ('espdesign:list_esp_design_data')
   return render (request, 'srpdesign/srp_design_data_form.html', {'form': form, 'srpdata':srpdata})

def delete_srp_design_data(request, id):
   srpdata = SRPDesignModel.objects.get(id=id)   
   if request.method == 'POST' :
       srpdata.delete()
       return redirect ('srpdesign:list_srp_design_data')
   return render (request, 'srpdesign/srp_design_data_confirm_delete.html', {'srpdata':srpdata})

def srp_design(request, id):
    srpdata = SRPDesignModel.objects.get(id=id)  
    form = SRPDesignForm(request.POST or None, instance=srpdata) 
    selectedwell = SelectedOilProducer.objects.first()  
    inflowdf, x1, y1, pip =calculate_inflow(srpdata, selectedwell)
    chart = get_ipr_plot(inflowdf, srpdata, x1, y1)    
    PPRL, MPRL, PT, PRHP, CBE = calculate_srp_parameters(srpdata)
    #q,q1,q2,head,eff,power, rangex, rangey, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead= Generate_pump_curves(espdata)
    #chart1= get_esp_plot1(q,q1,q2,head,eff,power, rangex, rangey, pump_name)
    #chart2= get_esp_plot2(q,head, pump_name, h11, h12, q11, q12, hz,bestEffrate,bestEffhead, berate, behead, minimumrate, minimumhead, maximumrate, maximumhead)
    #chart3 = vlp_curve_for_esp(espdata)
    return render (request, 'srpdesign/srp_design.html', {'srpdata':srpdata, 'form':form,'chart':chart,'PPRL':PPRL, 'MPRL':MPRL, 'PT':PT, 'PRHP':PRHP, 'CBE':CBE })

