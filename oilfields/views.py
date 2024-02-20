from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Oilfield

class OilfieldBaseView(View):
    model = Oilfield
    fields = '__all__'
    success_url = reverse_lazy('oilfields:all')

class OilfieldListView(OilfieldBaseView, ListView):
    """View to list all Oilfield.
    Use the 'Oilfield_list' variable in the template
    to access all Oilfield objects"""

class OilfieldDetailView(OilfieldBaseView, DetailView):
    """View to list the details from one Oilfield.
    Use the 'Oilfield' variable in the template to access
    the specific Oilfield here and in the Views below"""

class OilfieldCreateView(OilfieldBaseView, CreateView):
    """View to create a new Oilfield"""

class OilfieldUpdateView(OilfieldBaseView, UpdateView):
    """View to update a Oilfield"""

class OilfieldDeleteView(OilfieldBaseView, DeleteView):
    """View to delete a Oilfield"""