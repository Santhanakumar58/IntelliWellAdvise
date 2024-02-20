from django import forms
from .models import OBWellobjective

class OBWellObjectiveForm(forms.ModelForm):
    class Meta:        
        model = OBWellobjective
        fields =['obobjectives']  