from .models import GPRigworkoverOperation
from django import forms


class GPRigworkoverOpsForm(forms.ModelForm):
    gpop_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    gptime_from = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    gptime_to= forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')))
    class Meta:        
        model = GPRigworkoverOperation
        fields =['gpunitname', 'gpop_Date', 'gptime_from', 
        'gptime_to', 'gpop_code', 'gpop_details'
         ]
