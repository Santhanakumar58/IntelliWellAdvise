from .models import WIWellcompletion
from django import forms

class WICompletionForm(forms.ModelForm):   
    class Meta:        
        model = WIWellcompletion
        fields =['wiequipment', 'wiequip_Od', 'wiequip_Id', 
        'wiequip_Md',
         ]

