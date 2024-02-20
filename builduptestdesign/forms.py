from django import forms
from .models import PressureBuildupTestDesignModel

class PBUTestDesignForm(forms.ModelForm):   
    design_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = PressureBuildupTestDesignModel
        fields =['design_Date','design_Rate', 'layer_Thickness', 'layer_Permeability', 'mu_oil','total_Compressibility']