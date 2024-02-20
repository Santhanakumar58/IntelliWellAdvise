from django.shortcuts import render, redirect
from .models import RecordedLogsModel
from .forms import RecordedLogsForm
from selectedOilProducer.models import SelectedOilProducer
import os
import lasio
from .utils import get_log_plot, shale_volume, sw_archie, sw_simandoux, density_porosity, get_logs_calculated, get_porosity_density_cross_plot, get_other_cross_plots
import pandas as pd



def list_recorded_logs(request):     
    well = SelectedOilProducer.objects.all().first()   
    logs= RecordedLogsModel.objects.filter(wellid=well.wellid).all()
    return render (request, 'recordedlogs/recordedlogs.html', {'logs': logs})

def create_recorded_logs(request):   
    log = RecordedLogsModel()
    selectedwell = SelectedOilProducer.objects.first()  
    log.fgId = selectedwell.fgid
    log.wellid = selectedwell.wellid   
    form = RecordedLogsForm(request.POST or None, instance=log)
    if request.method =="POST":  
        form = RecordedLogsForm(request.POST, request.FILES, instance=log)       
        log.fgid = selectedwell.fgid
        log.wellid = selectedwell.wellid  
        if form.is_valid():
            form.save()
            return redirect ('recordedlogs:list_recorded_logs')
    return render (request, 'recordedlogs/recordedlogs_form.html', {'form': form})

def update_recorded_logs(request, id):
    log = RecordedLogsModel.objects.get(id=id)
    form = RecordedLogsForm(request.POST or None, instance=log)
    if request.method =="POST":  
        form = RecordedLogsForm(request.POST, request.FILES, instance=log) 
        if form.is_valid():
            print("Valid form")
            form.save()
            return redirect ('recordedlogs:list_recorded_logs')
    return render (request, 'recordedlogs/recordedlogs_form.html', {'form': form, 'log':log})

def delete_recorded_logs(request, id):
    log = RecordedLogsModel.objects.get(id=id)    
    if request.method == 'POST' :
        log.delete()
        return redirect ('recordedlogs:list_recorded_logs')
    return render (request, 'recordedlogs/recordedlogs_confirm_delete.html', {'log':log})

def view_log_from_data(request, id):
    logmodel= RecordedLogsModel.objects.get(id=id)  
    if logmodel.file_type=="LAS":       
        cwd = os.getcwd() 
        filename = logmodel.file_Name    
        name = filename.name
        pa = os.path.join(cwd, "media", name) 
        las = lasio.read(pa)       
        well = las.df() 
        min_depth = min(well.index)
        max_depth = max(well.index)
        min_depth = round((min_depth-50)/100)*100
        max_depth = round((max_depth+50)/100)*100     
        well['VSHALE'] = shale_volume(well['GR'], well['GR'].quantile(q=0.99),well['GR'].quantile(q=0.01))
        well['PHI'] = density_porosity(well['RHOB'], 2.65, 1)
        well['PHIECALC'] = well['PHI'] - (well['VSHALE'] * 0.3)
        well['SW'] = sw_archie(well['PHI'], well['RHOB'], well['MSFL'], 1, 2, 2)
        well['SW_SIM'] = sw_simandoux(well['PHIECALC'], well['RHOB'], well['MSFL'], 1, 2, 2, well['VSHALE'],2)
        well['SW_LIM'] = well['SW'].mask(well['SW']>1, 1)
        well['SW_SIM_LIM'] = well['SW_SIM'].mask(well['SW_SIM']>1, 1)       
        well_nan = well.notnull() * 1
        cols = well.columns       
        chart = get_logs_calculated(well, max_depth, min_depth, well_nan, cols)
        chart1 = get_porosity_density_cross_plot(well)
        chart2=get_other_cross_plots(well)
        return render (request, 'recordedlogs/viewlog.html', {'logmodel':logmodel, "chart":chart, "chart1":chart1,"chart2":chart2 })
    elif logmodel.file_type=="DLIS" :
        cwd = os.getcwd() 
        filename = logmodel.file_Name    
        name = filename.name
        pa = os.path.join(cwd, "media", name) 
        data = pd.read_csv(pa)        
        well = data
        print(well.head())
        min_depth = min(well.index)
        max_depth = max(well.index)
        min_depth = round((min_depth-50)/100)*100
        max_depth = round((max_depth+50)/100)*100     
        well['VSHALE'] = shale_volume(well['GR'], well['GR'].quantile(q=0.99),well['GR'].quantile(q=0.01))
        well['PHI'] = density_porosity(well['RHOB'], 2.65, 1)
        well['PHIECALC'] = well['PHI'] - (well['VSHALE'] * 0.3)
        cols = well.columns()
        print(cols)
        #well['SW'] = sw_archie(well['PHI'], well['RHOB'], well['MSFL'], 1, 2, 2)
        #well['SW_SIM'] = sw_simandoux(well['PHIECALC'], well['RHOB'], well['MSFL'], 1, 2, 2, well['VSHALE'],2)
        #well['SW_LIM'] = well['SW'].mask(well['SW']>1, 1)
        #well['SW_SIM_LIM'] = well['SW_SIM'].mask(well['SW_SIM']>1, 1)       
        #well_nan = well.notnull() * 1
        #chart = get_log_plot(well, max_depth, min_depth, well_nan)
        #chart = get_logs_calculated(well, max_depth, min_depth, well_nan)
        #chart1 = get_porosity_density_cross_plot(well)
        #chart2=get_other_cross_plots(well)
        return render (request, 'recordedlogs/viewlog.html', {'logmodel':logmodel, "chart":chart, "chart1":chart1,"chart2":chart2 })

    elif logmodel.file_type=="CSV":
        print('this is CSV WORLD')
        cwd = os.getcwd() 
        filename = logmodel.file_Name    
        name = filename.name
        pa = os.path.join(cwd, "media", name) 
        print(pa)
        data = pd.read_csv(pa)
        well = data
        print(well.head())
        min_depth = min(well.index)
        max_depth = max(well.index)
        min_depth = round((min_depth-50)/100)*100
        max_depth = round((max_depth+50)/100)*100     
        well['VSHALE'] = shale_volume(well['GR'], well['GR'].quantile(q=0.99),well['GR'].quantile(q=0.01))
        well['PHI'] = density_porosity(well['RHOB'], 2.65, 1)
        well['PHIECALC'] = well['PHI'] - (well['VSHALE'] * 0.3)
        cols = well.columns
        print(cols)
        if "RW" in cols or "MSFL" in cols:
            well['SW'] = sw_archie(well['PHI'], well['RHOB'], well['MSFL'], 1, 2, 2)
            well['SW_SIM'] = sw_simandoux(well['PHIECALC'], well['RHOB'], well['MSFL'], 1, 2, 2, well['VSHALE'],2)
            well['SW_LIM'] = well['SW'].mask(well['SW']>1, 1)
            well['SW_SIM_LIM'] = well['SW_SIM'].mask(well['SW_SIM']>1, 1)       
        well_nan = well.notnull() * 1       
        chart = get_logs_calculated(well, max_depth, min_depth, well_nan, cols)
        chart1 = get_porosity_density_cross_plot(well)
        chart2=get_other_cross_plots(well)
        return render (request, 'recordedlogs/viewlog.html', {'logmodel':logmodel, "chart1":chart1, "chart":chart,"chart2":chart2  })
    else :
        print ("Wrong  file format")
        print ("The file format should be in .LAS or .DLIS or .CSV")
        return render (request, 'recordedlogs/viewlog.html', {'logmodel':logmodel })

    return render (request, 'recordedlogs/viewlog.html', {'logmodel':logmodel })



