from .models import OBDrillingProblems
from django import forms


class OBDrillingProblemForm(forms.ModelForm):
    obops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date'))) 
    class Meta:        
        model = OBDrillingProblems
        fields =['obops_Date','obhole_Size' , 'obdepth_From', 
        'obdepth_To', 'obdescription', 'obpossible_reason'
         ]
