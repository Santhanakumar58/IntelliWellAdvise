from .models import GIWellhead, GITree
from django import forms
    
class GIWellheadForm(forms.ModelForm):   
    class Meta:        
        model = GIWellhead
        fields =['giwh_Make', 'giwh_Model', 'giwh_Type', 
        'giseal', 'gihanger_Type', 'giflange_Size',
         'giconnection', 'givalve_Size', 'gitemperature_Rating',  
         'gimaterial', 'giservice', 'giproduct_Service_Level',  
        ]
