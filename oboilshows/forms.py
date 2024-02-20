from .models import OBOilShowModel 
from django import forms

class OBOilShowForm(forms.ModelForm):  
    class Meta:        
        model = OBOilShowModel
        fields =["obformation" , "obtop_MD" , "obbottom_MD" , "obsample_Type", "obsample_Description" ,"obremarks" ]

