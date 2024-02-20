from django import forms
from .models import OBLeakoffTest

class OBLeakoffTestForm(forms.ModelForm):
    obrecorded_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = OBLeakoffTest
        fields =['obcasingSize', 'obanalyst', 'obrecorded_Date', 'obmudWeight', 'obopenholeLength', 'id']
     