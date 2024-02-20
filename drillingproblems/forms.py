from .models import DrillingProblems
from django import forms


class DrillingProblemForm(forms.ModelForm):
    ops_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date'))) 
    class Meta:        
        model = DrillingProblems
        fields =['ops_Date','hole_Size' , 'depth_From', 
        'depth_To', 'description', 'possible_reason'
         ]
