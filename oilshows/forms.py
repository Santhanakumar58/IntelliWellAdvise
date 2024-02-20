from .models import OilShowModel 
from django import forms

class OilShowForm(forms.ModelForm):  
    class Meta:        
        model = OilShowModel
        fields =["formation" , "top_MD" , "bottom_MD" , "sample_Type", "sample_Description" ,"remarks" ]

