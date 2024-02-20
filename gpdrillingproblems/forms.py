from .models import GPDrillingProblems
from django import forms


class GPDrillingProblemForm(forms.ModelForm):
    gpops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date'))) 
    class Meta:        
        model = GPDrillingProblems
        fields =['gpops_Date','gphole_Size' , 'gpdepth_From', 
        'gpdepth_To', 'gpdescription', 'gppossible_reason'
         ]
