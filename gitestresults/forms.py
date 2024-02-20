from .models import GITestResultModel 
from django import forms

class GITestResultForm(forms.ModelForm):  
    class Meta:        
        model = GITestResultModel
        fields =["giformation" , "gitop_MD" , "gibottom_MD" , "gitest_Duration", "gichoke_Size" ,"githp", "gibhp", 
                 "giliquid_Rate", "gioil_Rate", "gigas_Rate", "gigas_Rate", "giwater_Cut", "giremarks"]

