from django.urls import path
from .views import list_obdeviationsurvey, create_obdeviationsurvey, update_obdeviationsurvey, delete_obdeviationsurvey, Import_Deviation_SurveyData

app_name = 'obdeviationsurveydata'

urlpatterns = [  
    path('obdeviationsurvey/',list_obdeviationsurvey, name='list_obdeviationsurvey'),
    path('obdeviationsurvey/create/', create_obdeviationsurvey, name='create_obdeviationsurvey'),
    path('obdeviationsurvey/<int:id>/update/', update_obdeviationsurvey, name='update_obdeviationsurvey'),
    path('obdeviationsurvey/<int:id>/delete/', delete_obdeviationsurvey, name='delete_obdeviationsurvey'), 
    path('Import_Deviation_SurveyData/', Import_Deviation_SurveyData,  name='Import_Deviation_SurveyData'), 
]
