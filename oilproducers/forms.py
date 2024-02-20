from django import forms
from .models import OilProducer
from assets.models import Asset


class OilproducerForm(forms.ModelForm):
    class Meta:        
        model = OilProducer        
        fields =['wellname','category' , 'asset', 'block', 'oilfield', 'layer',
        'sublayer', 'completiontype', 'deviationtype', 'artificiallifttype', 'inflowtype',
        'connectedgatheringstation', 'connectedheader', 'unitid' ]
   