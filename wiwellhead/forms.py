from .models import WIWellhead, WITree
from django import forms
    
class WIWellheadForm(forms.ModelForm):   
    class Meta:        
        model = WIWellhead
        fields =['wiwh_Make', 'wiwh_Model', 'wiwh_Type', 
        'wiseal', 'wihanger_Type', 'wiflange_Size',
         'wiconnection', 'wivalve_Size', 'witemperature_Rating',  
         'wimaterial', 'wiservice', 'wiproduct_Service_Level',  
        ]
