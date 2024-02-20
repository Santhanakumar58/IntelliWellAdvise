from django.urls import path
from gireservoirpressure.views import list_gireservoirPressure, create_gireservoirPressure, update_gireservoirPressure,delete_gireservoirPressure

app_name = 'gireservoirpressure'

urlpatterns = [  
    path('', list_gireservoirPressure, name='list_gireservoirPressure'),
    path('create/', create_gireservoirPressure, name='create_gireservoirPressure'),
    path('<int:id>/update/', update_gireservoirPressure, name='update_gireservoirPressure'),   
    path('<int:id>/delete/', delete_gireservoirPressure, name='delete_gireservoirPressure'),
]