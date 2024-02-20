from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FGIModel

class FGIBaseView(View):
    model = FGIModel
    fields = '__all__'
    success_url = reverse_lazy('fgis:all')

class FGIListView(FGIBaseView, ListView):    
    """View to list all Block.
    Use the 'Block_list' variable in the template
    to access all Block objects"""

class FGIDetailView(FGIBaseView, DetailView):
    """View to list the details from one Block.
    Use the 'Block' variable in the template to access
    the specific Block here and in the Views below"""

class FGICreateView(FGIBaseView, CreateView):
    """View to create a new Block"""

class FGIUpdateView(FGIBaseView, UpdateView):
    """View to update a Block"""

class FGIDeleteView(FGIBaseView, DeleteView):
    """View to delete a Asset"""


   

