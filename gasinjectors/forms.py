from django import forms
from .models import GasInjector
from assets.models import Asset


class GasInjectorForm(forms.ModelForm):
    class Meta:        
        model = GasInjector        
        fields =['wellname','category' , 'asset', 'block', 'oilfield', 'layer',
        'sublayer', 'completiontype', 'deviationtype', 'inflowtype',
        'connectedgatheringstation', 'connectedheader', 'unitid' ]
   