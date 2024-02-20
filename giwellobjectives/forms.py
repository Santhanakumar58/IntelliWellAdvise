from django import forms
from .models import GIWellobjective

class GIWellObjectiveForm(forms.ModelForm):
    class Meta:        
        model = GIWellobjective
        fields =['giobjectives']  