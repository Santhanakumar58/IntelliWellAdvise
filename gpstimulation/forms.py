from .models import GPStimulation
from django import forms
    
class GPStimulationForm(forms.ModelForm):
    gpstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gpend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPStimulation
        fields =['gpunitname', 'gpstart_Date', 'gpend_Date', 
        'gpexpected_liquid', 'gpexpected_WC', 'gpexpected_GOR',
        'gppre_stim_liquid', 'gppre_stim_WC', 'gppre_stim_GOR', 
        'gppost_stim_liquid', 'gppost_stim_WC', 'gppost_stim_GOR', 
        'gpjobsummary' ]
