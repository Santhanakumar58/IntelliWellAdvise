from .models import GIReservoirPressureEstimationModel
from django import forms
    
class GIRespresEstimationForm(forms.ModelForm):
    gianalysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = GIReservoirPressureEstimationModel
        fields =['gianalysis_Date', 'gilayer_Permeability', 'gilayer_Thickness', 'gilayer_Porosity', 'gitotal_Compressibility', 
                 'gimu_oil','gioil_FVF' ,'giwellbore_Radius', 'gioil_Prod_Rate', 'giini_Res_Pres', 'gidrainage_Radius' ]
