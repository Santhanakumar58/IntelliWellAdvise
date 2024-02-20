from .models import RecordedLogsModel
from django import forms


class RecordedLogsForm(forms.ModelForm):
    survey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    class Meta:        
        model = RecordedLogsModel
        fields =['survey_Date', 'hole_size', 'log_Type', 'tool_string', 
        'from_MD', 'to_MD', 'service_Provider', 'unit_name','analyst' ,'interpretation' ,"logImage",'remarks' , 'file_type', 'file_Name'
         ]
