from django import forms
from .models import GPLeakoffTestData


class GPLeakoffTestDataForm(forms.ModelForm):    
    class Meta:
        model = GPLeakoffTestData
        fields =[ 'gpleakoffTest', 'gpcasingSize', 'gptime', 'gpvolume', 'gppressure']
