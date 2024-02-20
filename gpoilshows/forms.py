from .models import GPOilShowModel 
from django import forms

class GPOilShowForm(forms.ModelForm):  
    class Meta:        
        model = GPOilShowModel
        fields =["gpformation" , "gptop_MD" , "gpbottom_MD" , "gpsample_Type", "gpsample_Description" ,"gpremarks" ]

