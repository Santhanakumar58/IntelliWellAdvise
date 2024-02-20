from .models import OBSlickline
from django import forms
    
class OBSlicklineForm(forms.ModelForm):
    obstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    obend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = OBSlickline
        fields =['obunitname', 'obstart_Date', 'obend_Date', 
        'obexpected_liquid', 'obexpected_WC', 'obexpected_GOR',
        'obpre_slick_liquid', 'obpre_slick_WC', 'obpre_slick_GOR', 
        'obpost_slick_liquid', 'obpost_slick_WC', 'obpost_slick_GOR', 
        'objobsummary' ]
