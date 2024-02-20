from .models import WIReservoirPressureEstimationModel
from django import forms
    
class WIRespresEstimationForm(forms.ModelForm):
    wianalysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WIReservoirPressureEstimationModel
        fields =['wianalysis_Date', 'wilayer_Permeability', 'wilayer_Thickness', 'wilayer_Porosity', 'witotal_Compressibility', 
                 'wimu_oil','wioil_FVF' ,'wiwellbore_Radius', 'wioil_Prod_Rate', 'wiini_Res_Pres', 'widrainage_Radius' ]
