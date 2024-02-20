import os
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Layer
from django.shortcuts import redirect, render
from .forms import VolumetricForm
import pandas as pd
import numpy as np
from .utils import get_contours, compute_area, trapezoid, pyramidal, simpson, get_plot1, get_oil_plot, get_figs, get_contour_plots
from scipy.interpolate import griddata
import matplotlib.patches as mpl_patches 
import matplotlib.pyplot as plt 



class LayerBaseView(View):

    model = Layer
    fields = '__all__'
    success_url = reverse_lazy('layers:all')

class LayerListView(LayerBaseView, ListView):
    """View to list all layer.
    Use the 'layer_list' variable in the template
    to access all layer objects"""

class LayerDetailView(LayerBaseView, DetailView):
    """View to list the details from one layer.
    Use the 'layer' variable in the template to access
    the specific layer here and in the Views below"""

class LayerCreateView(LayerBaseView, CreateView):
    """View to create a new layer"""

class LayerUpdateView(LayerBaseView, UpdateView):
    """View to update a layer"""

class LayerDeleteView(LayerBaseView, DeleteView):
    """View to delete a Layer"""

class LayerVolumetrics (LayerBaseView, DetailView):
    """View to Details a Layer"""

def Layer_Volumetrics(request, pk):
    layer = Layer.objects.get(id=pk)   
    layer = Layer.objects.get(id=pk)
    path =layer.volumetric_data  
    filename = path.name
    path1 = 'C:/SanthanaKumar/PythonWellAdvisorNew/WellAdvisorPython/media/'
    pa = os.path.join(path1, filename) 
    welldat = pd.read_csv(pa)   
    x, y, z, h, poro, sw = welldat.x, welldat.y, welldat.depth, welldat.h, welldat.poro, welldat.sw
    Bo = 1.435 
    z = np.array([[z, h],
              [poro, sw]])
    # grid x and y coordinate data
    xi = np.linspace(min(x), max(x), 100)
    yi = np.linspace(min(y), max(y), 100)
    xi, yi = np.meshgrid(xi, yi)
    chart= get_plot1(x,y,xi,yi,z)       
    N = h * poro * (1 - sw) / Bo
    N = N * (1 / 5.61458) # convert the result from ft3/ft2 to standard STB/ft2
    df = pd.DataFrame({"well_id": welldat.well_id, "N (STB/ft2)": N})
    df = pd.merge(welldat, df, on='well_id')
    z = N   
    # grid N data with cubic interpolation method
    zi = griddata((x,y),z,(xi,yi),method='cubic')
    levels = np.arange(0, 1.1, 0.1) 
    figs = get_figs(xi,yi,zi,levels)
    chart1 = get_oil_plot(x,y,xi, yi,zi, levels)    
    chart2 = get_contour_plots(figs, xi, yi, plot='Yes')
    contour_all = get_contours(figs, xi, yi, plot='Yes')
    contour_area = compute_area(contour_all)
    areas = pd.DataFrame({"OIP Contour(STB)": levels, "Area(ft2)": contour_area})   
    oip_trapezo = round(trapezoid(contour_area, 0.1)/1E+06,3)
    oip_pyramidal = round(pyramidal(contour_area, 0.1)/1E+06,3)
    oip_simpson = round(simpson(contour_area, 0.1)/1E+06,3)
    print("Oil in Place using Trapezoidal Method:", np.round(oip_trapezo, 3), "million STB")
    print("Oil in Place using Pyramidal Method:", np.round((oip_pyramidal), 3), "million STB")
    print("Oil in Place using Simpson 1/3 Method:", np.round((oip_simpson), 3), "million STB")  
    form = VolumetricForm(request.POST or None, instance=layer)
    if request.method == 'POST' :
        form = VolumetricForm(request.POST or None,  instance=layer)
        return redirect ('layers:all')
    return render (request, 'layers/volumetricsform.html', {'layer':layer, 'chart':chart, 'chart1':chart1,'chart2':chart2, 'oip_trapezo':oip_trapezo, 'oip_pyramidal':oip_pyramidal, "oip_simpson":oip_simpson })

