from .models import GPWellhead, GPTree
from django import forms
    
class GPWellheadForm(forms.ModelForm):   
    class Meta:        
        model = GPWellhead
        fields =['gpwh_Make', 'gpwh_Model', 'gpwh_Type', 
        'gpseal', 'gphanger_Type', 'gpflange_Size',
         'gpconnection', 'gpvalve_Size', 'gptemperature_Rating',  
         'gpmaterial', 'gpservice', 'gpproduct_Service_Level',  
        ]
