from .models import Rigworkover
from django import forms
    
class RigworkoverForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Rigworkover
        fields =['rigname', 'start_Date', 'end_Date', 
        'expected_liquid', 'expected_WC', 'expected_GOR',
         'pre_wor_liquid', 'pre_wor_WC', 'pre_wor_GOR', 'pre_wor_Lift',
         'post_wor_liquid', 'post_wor_WC', 'post_wor_GOR', 'post_wor_Lift',
         'jobsummary' ]
