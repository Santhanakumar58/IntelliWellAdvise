from .models import Wellhead, Tree
from django import forms
    
class WellheadForm(forms.ModelForm):   
    class Meta:        
        model = Wellhead
        fields =['wh_Make', 'wh_Model', 'wh_Type', 
        'seal', 'hanger_Type', 'flange_Size',
         'connection', 'valve_Size', 'temperature_Rating',  
         'material', 'service', 'product_Service_Level',  
        ]
