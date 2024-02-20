from django import forms
from .models import GILeakoffTestData


class GILeakoffTestDataForm(forms.ModelForm):    
    class Meta:
        model = GILeakoffTestData
        fields =[ 'gileakoffTest', 'gicasingSize', 'gitime', 'givolume', 'gipressure']
