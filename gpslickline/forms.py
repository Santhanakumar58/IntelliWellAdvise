from .models import GPSlickline
from django import forms
    
class GPSlicklineForm(forms.ModelForm):
    gpstart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gpend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GPSlickline
        fields =['gpunitname', 'gpstart_Date', 'gpend_Date', 
        'gpexpected_liquid', 'gpexpected_WC', 'gpexpected_GOR',
        'gppre_slick_liquid', 'gppre_slick_WC', 'gppre_slick_GOR', 
        'gppost_slick_liquid', 'gppost_slick_WC', 'gppost_slick_GOR', 
        'gpjobsummary' ]
