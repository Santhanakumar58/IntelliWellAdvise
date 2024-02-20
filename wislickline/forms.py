from .models import WISlickline
from django import forms
    
class WISlicklineForm(forms.ModelForm):
    wistart_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    wiend_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WISlickline
        fields =['wiunitname', 'wistart_Date', 'wiend_Date', 
        'wiexpected_liquid', 'wiexpected_WC', 'wiexpected_GOR',
        'wipre_slick_liquid', 'wipre_slick_WC', 'wipre_slick_GOR', 
        'wipost_slick_liquid', 'wipost_slick_WC', 'wipost_slick_GOR', 
        'wijobsummary' ]
