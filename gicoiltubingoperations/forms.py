from .models import GICoiltubingOperation
from django import forms


class GICoiltubingOpsForm(forms.ModelForm):
    giop_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gitime_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    gitime_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = GICoiltubingOperation
        fields =['gictname', 'giop_Date', 'gitime_from', 
        'gitime_to', 'giop_code', 'giop_details'
         ]
