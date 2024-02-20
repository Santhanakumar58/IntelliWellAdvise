from .models import GISlickline
from django import forms
    
class GISlicklineForm(forms.ModelForm):
    gistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    giend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GISlickline
        fields =['giunitname', 'gistart_Date', 'giend_Date', 
        'giexpected_liquid', 'giexpected_WC', 'giexpected_GOR',
        'gipre_slick_liquid', 'gipre_slick_WC', 'gipre_slick_GOR', 
        'gipost_slick_liquid', 'gipost_slick_WC', 'gipost_slick_GOR', 
        'gijobsummary' ]
