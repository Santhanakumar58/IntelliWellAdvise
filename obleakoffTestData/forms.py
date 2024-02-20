from django import forms
from .models import OBLeakoffTestData


class OBLeakoffTestDataForm(forms.ModelForm):    
    class Meta:
        model = OBLeakoffTestData
        fields =[ 'obleakoffTest', 'obcasingSize', 'obtime', 'obvolume', 'obpressure']
