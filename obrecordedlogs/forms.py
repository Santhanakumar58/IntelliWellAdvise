from .models import OBRecordedLogsModel
from django import forms


class OBRecordedLogsForm(forms.ModelForm):
    obsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    class Meta:        
        model = OBRecordedLogsModel
        fields =['obsurvey_Date', 'obhole_size', 'oblog_Type', 'obtool_string', 
        'obfrom_MD', 'obto_MD', 'observice_Provider', 'obunit_name','obanalyst' ,'obinterpretation' ,"oblogImage",'obremarks' , 'obfile_type', 'obfile_Name'
         ]
