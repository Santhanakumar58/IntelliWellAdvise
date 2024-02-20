from .models import GIWellcompletion
from django import forms

class GICompletionForm(forms.ModelForm):   
    class Meta:        
        model = GIWellcompletion
        fields =['giequipment', 'giequip_Od', 'giequip_Id', 
        'giequip_Md',
         ]

