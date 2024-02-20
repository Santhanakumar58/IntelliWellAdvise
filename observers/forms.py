from django import forms
from .models import Observer
from assets.models import Asset


class ObserverForm(forms.ModelForm):
    class Meta:        
        model = Observer        
        fields =['wellname','category' , 'asset', 'block', 'oilfield', 'layer',
        'sublayer', 'completiontype', 'deviationtype', 'artificiallifttype', 'inflowtype',
        'connectedgatheringstation', 'connectedheader', 'unitid' ]
   