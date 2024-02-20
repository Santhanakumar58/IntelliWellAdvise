from .models import GIOilShowModel 
from django import forms

class GIOilShowForm(forms.ModelForm):  
    class Meta:        
        model = GIOilShowModel
        fields =["giformation" , "gitop_MD" , "gibottom_MD" , "gisample_Type", "gisample_Description" ,"giremarks" ]

