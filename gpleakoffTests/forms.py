from django import forms
from .models import GPLeakoffTest

class GPLeakoffTestForm(forms.ModelForm):
    gprecorded_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = GPLeakoffTest
        fields =['gpcasingSize', 'gpanalyst', 'gprecorded_Date', 'gpmudWeight', 'gpopenholeLength', 'id']
     