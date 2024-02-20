from django import forms
from .models import GasProducer
from assets.models import Asset


class GasproducerForm(forms.ModelForm):
    class Meta:        
        model = GasProducer        
        fields =['wellname','category' , 'asset', 'block', 'oilfield', 'layer',
        'sublayer', 'completiontype', 'deviationtype', 'inflowtype',
        'connectedgatheringstation', 'connectedheader', 'unitid' ]
   