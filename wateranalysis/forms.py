from django import forms
from .models import WaterAnalysisModel 
    
class WaterAnalysisForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:        
        model = WaterAnalysisModel 
        fields =[ "date", "wellName", "sampleId", "samplepoint", "lab","sodium", "calcium", "magnesium", "pottasium","ferric","bicarbonate", "carbonate", "sulphate", 'chloride',"nitrate", 'tds',  "temperature", "ph"]
