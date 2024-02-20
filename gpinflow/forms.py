from django import forms
from .models import GPProductivityIndexModel, GPVogelModel,GPWigginsModel,GPMultirateModel,GPStandingsModel,GPDarcyModel

class GPProductivityIndexForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPProductivityIndexModel
        fields =['analysis_Date', 'productivity_index', 'reservoir_Pressure', 'layer_Name', 'pvt_Well']
    

class GPVogelForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPVogelModel
        fields =['analysis_Date', 'vogel_Test_Rate', 'vogel_Test_Pressure', 'reservoir_Pressure', 'layer_Name', 'pvt_Well']
     

class GPStandingsForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPStandingsModel
        fields =['analysis_Date', 'current_Test_Rate', 'current_Test_Pressure', 'current_Reservoir_Pressure','future_Reservoir_Pressure', 'current_Relative_Permeability','future_Relative_Permeability','layer_Name','pvt_Well']
     
   

class GPWigginsForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPWigginsModel
        fields =['analysis_Date', 'wiggins_Test_Rate', 'wiggins_Test_Pressure', 'current_Reservoir_Pressure', 'future_Reservoir_Pressure','layer_Name','water_Cut', 'pvt_Well']
     
  

class GPMultiRateForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPMultirateModel
        fields =['analysis_Date', 'test_Rate1', 'test_Pressure1', 'test_Rate2', 'test_Pressure2','test_Rate3','test_Pressure3', 'current_Reservoir_Pressure', 'layer_Name', 'pvt_Well']
     


class GPDarcyModelForm(forms.ModelForm):
    analysis_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPDarcyModel
        fields =['analysis_Date', 'layer_Permeability', 'layer_Thickness', 'drainage_Radius', 'wellbore_Radius','layer_Skin', 'current_Reservoir_Pressure', 'layer_Name', 'pvt_Well']
     