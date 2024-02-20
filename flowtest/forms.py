from django import forms
from .models import FlowTestModel


class FlowTestForm(forms.ModelForm):   
    test_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    class Meta:
        model = FlowTestModel
        fields =['test_Date','test_Duration', 'choke_Size', 'th_Pres', 'th_Temp',
                'liquid_Rate','oil_Rate', 'gas_Rate', 'fl_Pres', 'fl_Temp',
                'sep_Pres', 'sep_Temp', 'remarks'        
        ]
        