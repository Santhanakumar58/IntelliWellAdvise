from .models import OBWellcompletion
from django import forms

class OBCompletionForm(forms.ModelForm):   
    class Meta:        
        model = OBWellcompletion
        fields =['obequipment', 'obequip_Od', 'obequip_Id', 
        'obequip_Md',
         ]

