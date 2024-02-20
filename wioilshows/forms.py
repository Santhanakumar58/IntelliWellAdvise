from .models import WIOilShowModel 
from django import forms

class WIOilShowForm(forms.ModelForm):  
    class Meta:        
        model = WIOilShowModel
        fields =["wiformation" , "witop_MD" , "wibottom_MD" , "wisample_Type", "wisample_Description" ,"wiremarks" ]

