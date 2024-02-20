from .models import WIStimulation
from django import forms
    
class WIStimulationForm(forms.ModelForm):
    wistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    wiend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIStimulation
        fields =['wiunitname', 'wistart_Date', 'wiend_Date', 
        'wiexpected_liquid', 'wiexpected_WC', 'wiexpected_GOR',
         'wipre_stim_liquid', 'wipre_stim_WC', 'wipre_stim_GOR', 
         'wipost_stim_liquid', 'wipost_stim_WC', 'wipost_stim_GOR', 
         'wijobsummary' ]
