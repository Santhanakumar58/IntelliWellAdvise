from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sublayer

class SublayerBaseView(View):

    model = Sublayer
    fields = '__all__'
    success_url = reverse_lazy('sublayers:all')

class SublayerListView(SublayerBaseView, ListView):
    """View to list all layer.
    Use the 'layer_list' variable in the template
    to access all layer objects"""

class SublayerDetailView(SublayerBaseView, DetailView):
    """View to list the details from one layer.
    Use the 'layer' variable in the template to access
    the specific layer here and in the Views below"""

class SublayerCreateView(SublayerBaseView, CreateView):
    """View to create a new layer"""

class SublayerUpdateView(SublayerBaseView, UpdateView):
    """View to update a layer"""

class SublayerDeleteView(SublayerBaseView, DeleteView):
    model=Sublayer
    """View to delete a Layer"""