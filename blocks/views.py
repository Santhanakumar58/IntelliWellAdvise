from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Block

class BlockBaseView(View):
    model = Block
    fields = '__all__'
    success_url = reverse_lazy('blocks:all')

class BlockListView(BlockBaseView, ListView):
    """View to list all Block.
    Use the 'Block_list' variable in the template
    to access all Block objects"""

class BlockDetailView(BlockBaseView, DetailView):
    """View to list the details from one Block.
    Use the 'Block' variable in the template to access
    the specific Block here and in the Views below"""

class BlockCreateView(BlockBaseView, CreateView):
    """View to create a new Block"""

class BlockUpdateView(BlockBaseView, UpdateView):
    """View to update a Block"""

class BlockDeleteView(BlockBaseView, DeleteView):    
    """View to delete a Asset"""