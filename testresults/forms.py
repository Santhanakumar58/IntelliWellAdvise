from .models import TestResultModel 
from django import forms

class TestResultForm(forms.ModelForm):  
    class Meta:        
        model = TestResultModel
        fields =["formation" , "top_MD" , "bottom_MD" , "test_Duration", "choke_Size" ,"thp", "bhp", "liquid_Rate", "oil_Rate", "gas_Rate", "gas_Rate", "water_Cut", "remarks"]

