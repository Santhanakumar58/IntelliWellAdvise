from .models import OBStimulation
from django import forms
    
class OBStimulationForm(forms.ModelForm):
    obstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBStimulation
        fields =['obunitname', 'obstart_Date', 'obend_Date', 
        'obexpected_liquid', 'obexpected_WC', 'obexpected_GOR',
        'obpre_stim_liquid', 'obpre_stim_WC', 'obpre_stim_GOR', 
        'obpost_stim_liquid', 'obpost_stim_WC', 'obpost_stim_GOR', 
        'objobsummary' ]
