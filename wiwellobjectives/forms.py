from django import forms
from .models import WIWellobjective

class WIWellObjectiveForm(forms.ModelForm):
    class Meta:        
        model = WIWellobjective
        fields =['wiobjectives']  