from django.urls import path
from obreservoirpressure.views import list_obreservoirPressure, create_obreservoirPressure, update_obreservoirPressure,delete_obreservoirPressure

app_name = 'obreservoirpressure'

urlpatterns = [  
    path('', list_obreservoirPressure, name='list_obreservoirPressure'),
    path('create/', create_obreservoirPressure, name='create_obreservoirPressure'),
    path('<int:id>/update/', update_obreservoirPressure, name='update_obreservoirPressure'),   
    path('<int:id>/delete/', delete_obreservoirPressure, name='delete_obreservoirPressure'),
]