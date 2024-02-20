from django.urls import path
from .views import  list_esp_design_data, create_esp_design_data, update_esp_design_data, delete_esp_design_data, esp_design


app_name = 'espdesign'

urlpatterns = [ 
    path('', list_esp_design_data, name='list_esp_design_data'),    
    path('create/', create_esp_design_data, name='create_esp_design_data'),
    path('<int:id>/update/', update_esp_design_data, name='update_esp_design_data'),   
    path('<int:id>/delete/', delete_esp_design_data, name='delete_esp_design_data'),
    path('<int:id>/design/', esp_design, name='esp_design'),
   
   
]