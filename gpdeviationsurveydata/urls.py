from django.urls import path
from .views import list_gpdeviationsurvey, create_gpdeviationsurvey, update_gpdeviationsurvey, delete_gpdeviationsurvey, Import_Deviation_SurveyData

app_name = 'gpdeviationsurveydata'

urlpatterns = [  
    path('gpdeviationsurvey/',list_gpdeviationsurvey, name='list_gpdeviationsurvey'),
    path('gpdeviationsurvey/create/', create_gpdeviationsurvey, name='create_gpdeviationsurvey'),
    path('gpdeviationsurvey/<int:id>/update/', update_gpdeviationsurvey, name='update_gpdeviationsurvey'),
    path('gpdeviationsurvey/<int:id>/delete/', delete_gpdeviationsurvey, name='delete_gpdeviationsurvey'), 
    path('Import_Deviation_SurveyData/', Import_Deviation_SurveyData,  name='Import_Deviation_SurveyData'), 
]
