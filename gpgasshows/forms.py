from .models import GPGasShowModel
from django import forms

class GPGasShowForm(forms.ModelForm):  
    class Meta:        
        model = GPGasShowModel
        fields =["gpformation" , "gptop_MD" , "gpbottom_MD" , "gptotal_Gas", "gpmethane" ,
                "gpethane",  "gppropane" , "gpiso_Butane", "gpneo_Butane" , "gpiso_Pentane", "gpneo_Pentane", "gpremarks" ]

