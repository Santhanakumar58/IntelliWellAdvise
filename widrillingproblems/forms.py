from .models import WIDrillingProblems
from django import forms


class WIDrillingProblemForm(forms.ModelForm):
    wiops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date'))) 
    class Meta:        
        model = WIDrillingProblems
        fields =['wiops_Date','wihole_Size' , 'widepth_From', 
        'widepth_To', 'widescription', 'wipossible_reason'
         ]
