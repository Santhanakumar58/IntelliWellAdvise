from django.urls import path
from gpreservoirpressure.views import list_gpreservoirPressure, create_gpreservoirPressure, update_gpreservoirPressure,delete_gpreservoirPressure

app_name = 'gpreservoirpressure'

urlpatterns = [  
    path('', list_gpreservoirPressure, name='list_gpreservoirPressure'),
    path('create/', create_gpreservoirPressure, name='create_gpreservoirPressure'),
    path('<int:id>/update/', update_gpreservoirPressure, name='update_gpreservoirPressure'),   
    path('<int:id>/delete/', delete_gpreservoirPressure, name='delete_gpreservoirPressure'),
]