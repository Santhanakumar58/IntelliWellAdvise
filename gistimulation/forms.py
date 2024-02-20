from .models import GIStimulation
from django import forms
    
class GIStimulationForm(forms.ModelForm):
    gistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    giend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIStimulation
        fields =['giunitname', 'gistart_Date', 'giend_Date', 
        'giexpected_liquid', 'giexpected_WC', 'giexpected_GOR',
        'gipre_stim_liquid', 'gipre_stim_WC', 'gipre_stim_GOR', 
        'gipost_stim_liquid', 'gipost_stim_WC', 'gipost_stim_GOR', 
        'gijobsummary' ]
