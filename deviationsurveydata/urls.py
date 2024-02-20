from django.urls import path
from .views import list_deviationsurvey, create_deviationsurvey, update_deviationsurvey, delete_deviationsurvey, Import_Deviation_SurveyData

app_name = 'deviationsurveydata'

urlpatterns = [  
    path('deviationsurvey/',list_deviationsurvey, name='list_deviationsurvey'),
    path('deviationsurvey/create/', create_deviationsurvey, name='create_deviationsurvey'),
    path('deviationsurvey/<int:id>/update/', update_deviationsurvey, name='update_deviationsurvey'),
    path('deviationsurvey/<int:id>/delete/', delete_deviationsurvey, name='delete_deviationsurvey'), 
    path('Import_Deviation_SurveyData/', Import_Deviation_SurveyData,  name='Import_Deviation_SurveyData'), 
]
