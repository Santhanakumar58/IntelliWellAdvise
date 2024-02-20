from .models import GPRecordedLogsModel
from django import forms


class GPRecordedLogsForm(forms.ModelForm):
    gpsurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    class Meta:        
        model = GPRecordedLogsModel
        fields =['gpsurvey_Date', 'gphole_size', 'gplog_Type', 'gptool_string', 
        'gpfrom_MD', 'gpto_MD', 'gpservice_Provider', 'gpunit_name','gpanalyst' ,'gpinterpretation' ,"gplogImage",'gpremarks' , 'gpfile_type', 'gpfile_Name'
         ]
