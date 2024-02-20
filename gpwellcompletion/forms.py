from .models import GPWellcompletion
from django import forms

class GPCompletionForm(forms.ModelForm):   
    class Meta:        
        model = GPWellcompletion
        fields =['gpequipment', 'gpequip_Od', 'gpequip_Id', 
        'gpequip_Md',
         ]

