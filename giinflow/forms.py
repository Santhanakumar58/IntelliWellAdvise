from django import forms
from .models import GIProductivityIndexModel, GIVogelModel,GIWigginsModel,GIMultirateModel,GIStandingsModel,GIDarcyModel

class GIProductivityIndexForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIProductivityIndexModel
        fields =['analysis_Date', 'productivity_index', 'reservoir_Pressure', 'layer_Name', 'pvt_Well']
    

class GIVogelForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIVogelModel
        fields =['analysis_Date', 'vogel_Test_Rate', 'vogel_Test_Pressure', 'reservoir_Pressure', 'layer_Name', 'pvt_Well']
     

class GIStandingsForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIStandingsModel
        fields =['analysis_Date', 'current_Test_Rate', 'current_Test_Pressure', 'current_Reservoir_Pressure','future_Reservoir_Pressure', 'current_Relative_Permeability','future_Relative_Permeability','layer_Name','pvt_Well']
     
   

class GIWigginsForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIWigginsModel
        fields =['analysis_Date', 'wiggins_Test_Rate', 'wiggins_Test_Pressure', 'current_Reservoir_Pressure', 'future_Reservoir_Pressure','layer_Name','water_Cut', 'pvt_Well']
     
  

class GIMultiRateForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIMultirateModel
        fields =['analysis_Date', 'test_Rate1', 'test_Pressure1', 'test_Rate2', 'test_Pressure2','test_Rate3','test_Pressure3', 'current_Reservoir_Pressure', 'layer_Name', 'pvt_Well']
     


class GIDarcyModelForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GIDarcyModel
        fields =['analysis_Date', 'layer_Permeability', 'layer_Thickness', 'drainage_Radius', 'wellbore_Radius','layer_Skin', 'current_Reservoir_Pressure', 'layer_Name', 'pvt_Well']
     