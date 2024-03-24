from django import forms
from .models import MultiRateDrawdowntest
    
class MultiRateDrawdownTestForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = MultiRateDrawdowntest
        fields =['survey_Date', 'gauge_Depth_ft', 'layer_Porosity_fraction', 'layer_Thickness_ft',  'wellbore_Radius_ft',
                 'total_Compressibility', 'initial_Res_Pres_psi', 'oil_Viscosity_cP', 'oil_FVF_Bo', 
                 'time1', 'rate1', 'time2', 'rate2', 'time3', 'rate3', 'file_Name_csv' ]



class MultiRateDrawdownTestUploadForm(forms.ModelForm):    
    class Meta:        
        model = MultiRateDrawdowntest
        fields =['time1', 'rate1', 'time2', 'rate2',  'time3','rate3']


   