from django.urls import path
from .views import  list_srp_design_data, create_srp_design_data, update_srp_design_data, delete_srp_design_data, srp_design


app_name = 'srpdesign'

urlpatterns = [ 
    path('', list_srp_design_data, name='list_srp_design_data'),    
    path('create/', create_srp_design_data, name='create_srp_design_data'),
    path('<int:id>/update/', update_srp_design_data, name='update_srp_design_data'),   
    path('<int:id>/delete/', delete_srp_design_data, name='delete_srp_design_data'),
    path('<int:id>/design/', srp_design, name='srp_design'),
   
   
]