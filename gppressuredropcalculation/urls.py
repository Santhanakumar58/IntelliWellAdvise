from django.urls import path
from .views import list_gppressure_drop, create_gppressure_drop, update_gppressure_drop,delete_gppressure_drop


app_name = 'gppressuredropcalculation'

urlpatterns = [  
    path('', list_gppressure_drop, name='list_gppressure_drop'),
    path('create/', create_gppressure_drop, name='create_gppressure_drop'),
    path('<int:id>/update/', update_gppressure_drop, name='update_gppressure_drop'),   
    path('<int:id>/delete/', delete_gppressure_drop, name='delete_gppressure_drop'),
    
   
]