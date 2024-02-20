from django.urls import path
from .views import  list_jetpump_design_data, create_jetpump_design_data, update_jetpump_design_data, delete_jetpump_design_data, jetpump_design


app_name = 'jetpumpdesign'

urlpatterns = [ 
    path('', list_jetpump_design_data, name='list_jetpump_design_data'),    
    path('create/', create_jetpump_design_data, name='create_jetpump_design_data'),
    path('<int:id>/update/', update_jetpump_design_data, name='update_jetpump_design_data'),   
    path('<int:id>/delete/', delete_jetpump_design_data, name='delete_jetpump_design_data'),
    path('<int:id>/design/', jetpump_design, name='jetpump_design'),
   
   
]