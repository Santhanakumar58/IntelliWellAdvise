from django import forms
from .models import OPWellobjective

class OPWellObjectiveForm(forms.ModelForm):
    class Meta:        
        model = OPWellobjective
        fields =['opobjectives']  
       
        
        



  
