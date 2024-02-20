from .models import GPTestResultModel 
from django import forms

class GPTestResultForm(forms.ModelForm):  
    class Meta:        
        model = GPTestResultModel
        fields =["gpformation" , "gptop_MD" , "gpbottom_MD" , "gptest_Duration", "gpchoke_Size" ,"gpthp", "gpbhp", 
                 "gpliquid_Rate", "gpoil_Rate", "gpgas_Rate", "gpgas_Rate", "gpwater_Cut", "gpremarks"]

