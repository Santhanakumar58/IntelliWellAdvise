from .models import ReservoirPressureEstimationModel
from django import forms
    
class RespresEstimationForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = ReservoirPressureEstimationModel
        fields =['analysis_Date', 'layer_Permeability', 'layer_Thickness', 'layer_Porosity', 'total_Compressibility', 'mu_oil','oil_FVF' ,'wellbore_Radius', 'oil_Prod_Rate', 'ini_Res_Pres', 'drainage_Radius' ]
