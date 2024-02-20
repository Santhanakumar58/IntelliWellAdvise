from .models import GIRigworkoverOperation
from django import forms


class GIRigworkoverOpsForm(forms.ModelForm):
    giop_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gitime_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    gitime_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = GIRigworkoverOperation
        fields =['giunitname', 'giop_Date', 'gitime_from', 
        'gitime_to', 'giop_code', 'giop_details'
         ]
