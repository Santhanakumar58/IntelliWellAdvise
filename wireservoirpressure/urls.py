from django.urls import path
from wireservoirpressure.views import list_wireservoirPressure, create_wireservoirPressure, update_wireservoirPressure,delete_wireservoirPressure

app_name = 'wireservoirpressure'

urlpatterns = [  
    path('', list_wireservoirPressure, name='list_wireservoirPressure'),
    path('create/', create_wireservoirPressure, name='create_wireservoirPressure'),
    path('<int:id>/update/', update_wireservoirPressure, name='update_wireservoirPressure'),   
    path('<int:id>/delete/', delete_wireservoirPressure, name='delete_wireservoirPressure'),
]