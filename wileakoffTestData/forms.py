from django import forms
from .models import WILeakoffTestData


class WILeakoffTestDataForm(forms.ModelForm):    
    class Meta:
        model = WILeakoffTestData
        fields =[ 'wileakoffTest', 'wicasingSize', 'witime', 'wivolume', 'wipressure']
