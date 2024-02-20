from django import forms
from .models import GILeakoffTest

class GILeakoffTestForm(forms.ModelForm):
    girecorded_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GILeakoffTest
        fields =['gicasingSize', 'gianalyst', 'girecorded_Date', 'gimudWeight', 'giopenholeLength', 'id']
     