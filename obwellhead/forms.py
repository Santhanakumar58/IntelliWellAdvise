from .models import OBWellhead, OBTree
from django import forms
    
class OBWellheadForm(forms.ModelForm):   
    class Meta:        
        model = OBWellhead
        fields =['obwh_Make', 'obwh_Model', 'obwh_Type', 
        'obseal', 'obhanger_Type', 'obflange_Size',
         'obconnection', 'obvalve_Size', 'obtemperature_Rating',  
         'obmaterial', 'observice', 'obproduct_Service_Level',  
        ]
