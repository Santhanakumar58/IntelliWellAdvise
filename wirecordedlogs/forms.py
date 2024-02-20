from .models import WIRecordedLogsModel
from django import forms


class WIRecordedLogsForm(forms.ModelForm):
    wisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    class Meta:        
        model = WIRecordedLogsModel
        fields =['wisurvey_Date', 'wihole_size', 'wilog_Type', 'witool_string', 
        'wifrom_MD', 'wito_MD', 'wiservice_Provider', 'wiunit_name','wianalyst' ,'wiinterpretation' ,"wilogImage",'wiremarks' , 'wifile_type', 'wifile_Name'
         ]
