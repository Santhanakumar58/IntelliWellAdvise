from django import forms
from .models import WaterInjector
from assets.models import Asset


class WaterInjectorForm(forms.ModelForm):
    class Meta:        
        model = WaterInjector        
        fields =['wellname','category' , 'asset', 'block', 'oilfield', 'layer',
        'sublayer', 'completiontype', 'deviationtype', 'inflowtype',
        'connectedgatheringstation', 'connectedheader', 'unitid' ]
   