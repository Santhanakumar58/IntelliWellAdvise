from django.urls import path
from .views import list_wideviationsurvey, create_wideviationsurvey, update_wideviationsurvey, delete_wideviationsurvey, Import_Deviation_SurveyData

app_name = 'wideviationsurveydata'

urlpatterns = [  
    path('wideviationsurvey/',list_wideviationsurvey, name='list_wideviationsurvey'),
    path('wideviationsurvey/create/', create_wideviationsurvey, name='create_wideviationsurvey'),
    path('wideviationsurvey/<int:id>/update/', update_wideviationsurvey, name='update_wideviationsurvey'),
    path('wideviationsurvey/<int:id>/delete/', delete_wideviationsurvey, name='delete_wideviationsurvey'), 
    path('Import_Deviation_SurveyData/', Import_Deviation_SurveyData,  name='Import_Deviation_SurveyData'), 
]
