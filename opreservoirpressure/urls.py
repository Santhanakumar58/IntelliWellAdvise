from django.urls import path
from opreservoirpressure.views import list_reservoirPressure, create_reservoirPressure, update_reservoirPressure,delete_reservoirPressure

app_name = 'opreservoirpressure'

urlpatterns = [  
    path('', list_reservoirPressure, name='list_reservoirPressure'),
    path('create/', create_reservoirPressure, name='create_reservoirPressure'),
    path('<int:id>/update/', update_reservoirPressure, name='update_reservoirPressure'),   
    path('<int:id>/delete/', delete_reservoirPressure, name='delete_reservoirPressure'),
]