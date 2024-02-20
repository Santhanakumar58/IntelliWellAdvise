from .models import Wellcompletion
from django import forms

class CompletionForm(forms.ModelForm):   
    class Meta:        
        model = Wellcompletion
        fields =['equipment', 'equip_Od', 'equip_Id', 
        'equip_Md',
         ]

