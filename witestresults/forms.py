from .models import WITestResultModel 
from django import forms

class WITestResultForm(forms.ModelForm):  
    class Meta:        
        model = WITestResultModel     
        fields =["wiformation" , "witop_MD" , "wibottom_MD" , "witest_Duration", "wichoke_Size" ,"withp", "wibhp", 
                 "wiliquid_Rate", "wioil_Rate", "wigas_Rate", "wigas_Rate", "wiwater_Cut", "wiremarks"]

