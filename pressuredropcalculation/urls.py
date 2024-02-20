from django.urls import path
from .views import list_pressure_drop, create_pressure_drop, update_pressure_drop,delete_pressure_drop


app_name = 'pressuredropcalculation'

urlpatterns = [  
    path('', list_pressure_drop, name='list_pressure_drop'),
    path('create/', create_pressure_drop, name='create_pressure_drop'),
    path('<int:id>/update/', update_pressure_drop, name='update_pressure_drop'),   
    path('<int:id>/delete/', delete_pressure_drop, name='delete_pressure_drop'),
    
   
]