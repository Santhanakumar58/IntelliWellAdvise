from django import forms
from .models import MultiRatePBUdesign
    
class MultiRatePBUdesignForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = MultiRatePBUdesign
        fields =['survey_Date', 'layer_Porosity_fraction', 'layer_Permeability_md', 'layer_Thickness_ft',  'wellbore_Radius_ft',
                 'drainage_radius_ft', 'total_Compressibility', 'initial_Res_Pres_psi', 'oil_Viscosity_cP', 'oil_FVF_Bo', 
                 'time1', 'rate1', 'time2', 'rate2', 'time3', 'rate3', 'time4', 'rate4', 'time5', 'rate5', 'time6', 'rate6' ]