from django.urls import path
from .views import list_gideviationsurvey, create_gideviationsurvey, update_gideviationsurvey, delete_gideviationsurvey, Import_Deviation_SurveyData

app_name = 'gideviationsurveydata'

urlpatterns = [  
    path('gideviationsurvey/',list_gideviationsurvey, name='list_gideviationsurvey'),
    path('gideviationsurvey/create/', create_gideviationsurvey, name='create_gideviationsurvey'),
    path('gideviationsurvey/<int:id>/update/', update_gideviationsurvey, name='update_gideviationsurvey'),
    path('gideviationsurvey/<int:id>/delete/', delete_gideviationsurvey, name='delete_gideviationsurvey'), 
    path('Import_Deviation_SurveyData/', Import_Deviation_SurveyData,  name='Import_Deviation_SurveyData'), 
]
