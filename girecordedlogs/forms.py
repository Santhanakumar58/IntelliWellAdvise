from .models import GIRecordedLogsModel
from django import forms


class GIRecordedLogsForm(forms.ModelForm):
    gisurvey_Date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))    
    class Meta:        
        model = GIRecordedLogsModel
        fields =['gisurvey_Date', 'gihole_size', 'gilog_Type', 'gitool_string', 
        'gifrom_MD', 'gito_MD', 'giservice_Provider', 'giunit_name','gianalyst' ,'giinterpretation' ,"gilogImage",'giremarks' , 'gifile_type', 'gifile_Name'
         ]