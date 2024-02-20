from django import forms
from .models import WILeakoffTest

class WILeakoffTestForm(forms.ModelForm):
    wirecorded_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = WILeakoffTest
        fields =['wicasingSize', 'wianalyst', 'wirecorded_Date', 'wimudWeight', 'wiopenholeLength', 'id']
     