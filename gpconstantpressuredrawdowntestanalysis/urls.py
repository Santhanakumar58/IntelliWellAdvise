from django.urls import path
from .views import  list_gpconstantpressure_test_data, create_gpconstantpressure_test_data,update_gpconstantpressure_test_data, delete_gpconstantpressure_test_data, upload_Constant_Pressure_test_data


app_name = 'gpconstantpressuredrawdowntestanalysis'

urlpatterns = [ 
    path('', list_gpconstantpressure_test_data, name='list_gpconstantpressure_test_data'),    
    path('create/', create_gpconstantpressure_test_data, name='create_gpconstantpressure_test_data'),
    path('<int:id>/update/', update_gpconstantpressure_test_data, name='update_gpconstantpressure_test_data'),   
    path('<int:id>/delete/', delete_gpconstantpressure_test_data, name='delete_gpconstantpressure_test_data'),
    path('<int:id>/cons_Pres/', upload_Constant_Pressure_test_data, name='upload_Constant_Pressure_test_data'), 
]