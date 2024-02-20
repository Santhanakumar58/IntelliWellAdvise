from django import forms
from .models import GPPressuredropCalculationModel

class GPPressureDropCalcForm(forms.ModelForm):   
    model_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPPressuredropCalculationModel
        fields =['gpmodel_Date','gpsource_Pressure', 'gpsource_Flowrate', 'gpsource_Temp', 'gppipe_Angle','gppipe_Length', 'gppipe_Diam',
        'gpfluid_API', 'gpfluid_WaterCut', 'gpfluid_GOR', 'gpfluid_gas_spgr']