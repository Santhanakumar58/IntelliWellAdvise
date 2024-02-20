from .models import Stimulation
from django import forms
    
class StimulationForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Stimulation
        fields =['unitname', 'start_Date', 'end_Date', 
        'expected_liquid', 'expected_WC', 'expected_GOR',
         'pre_stim_liquid', 'pre_stim_WC', 'pre_stim_GOR', 
         'post_stim_liquid', 'post_stim_WC', 'post_stim_GOR', 
         'jobsummary' ]
