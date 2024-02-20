from django import forms
from .models import LeakoffTestData


class LeakoffTestDataForm(forms.ModelForm):    
    class Meta:
        model = LeakoffTestData
        fields =[ 'leakoffTest', 'casingSize', 'time', 'volume', 'pressure']
