from django import forms
from .models import LeakoffTest

class LeakoffTestForm(forms.ModelForm):
    recorded_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = LeakoffTest
        fields =['casingSize', 'analyst', 'recorded_Date', 'mudWeight', 'openholeLength', 'id']
     