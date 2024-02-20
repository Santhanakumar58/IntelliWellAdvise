from .models import GIDrillingProblems
from django import forms


class GIDrillingProblemForm(forms.ModelForm):
    giops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date'))) 
    class Meta:        
        model = GIDrillingProblems
        fields =['giops_Date','gihole_Size' , 'gidepth_From', 
        'gidepth_To', 'gidescription', 'gipossible_reason'
         ]
