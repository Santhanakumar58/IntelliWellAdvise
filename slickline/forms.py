from .models import Slickline
from django import forms
    
class SlicklineForm(forms.ModelForm):
    start_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    end_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = Slickline
        fields =['unitname', 'start_Date', 'end_Date', 
        'expected_liquid', 'expected_WC', 'expected_GOR',
        'pre_slick_liquid', 'pre_slick_WC', 'pre_slick_GOR', 
        'post_slick_liquid', 'post_slick_WC', 'post_slick_GOR', 
        'jobsummary' ]
