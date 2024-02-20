from .models import OBTestResultModel 
from django import forms

class OBTestResultForm(forms.ModelForm):  
    class Meta:        
        model = OBTestResultModel
        fields =["obformation" , "obtop_MD" , "obbottom_MD" , "obtest_Duration", "obchoke_Size" ,"obthp", "obbhp", 
                 "obliquid_Rate", "oboil_Rate", "obgas_Rate", "obgas_Rate", "obwater_Cut", "obremarks"]

