from django import forms
from .models import GPWellobjective

class GPWellObjectiveForm(forms.ModelForm):
    class Meta:        
        model = GPWellobjective
        fields =['gpobjectives']  
       
        
        