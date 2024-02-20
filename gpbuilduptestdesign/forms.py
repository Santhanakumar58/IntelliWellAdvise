from django import forms
from .models import GPPressureBuildupTestDesignModel

class GPPBUTestDesignForm(forms.ModelForm):   
    design_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPPressureBuildupTestDesignModel
        fields =['gpdesign_Date','gpdesign_Rate', 'gplayer_Thickness', 'gplayer_Permeability', 'gpmu_oil','gptotal_Compressibility']