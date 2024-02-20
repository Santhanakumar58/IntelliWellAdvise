from django import forms
from .models import GPWellobjectivedata

class GPWellObjectivedataForm(forms.ModelForm):
    class Meta:        
        model = GPWellobjectivedata
        fields =fields =['gpwellid','date', 'gasrate_mmscfd', 'cgr_barrels_per_mmscf', 'watercut_percentage' ]
       
        
        