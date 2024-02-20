from django.urls import path
from .views import  list_constantpressure_test_data, create_constantpressure_test_data,update_constantpressure_test_data, delete_constantpressure_test_data, upload_Constant_Pressure_test_data


app_name = 'constantpressuredrawdowntestanalysis'

urlpatterns = [ 
    path('', list_constantpressure_test_data, name='list_constantpressure_test_data'),    
    path('create/', create_constantpressure_test_data, name='create_constantpressure_test_data'),
    path('<int:id>/update/', update_constantpressure_test_data, name='update_constantpressure_test_data'),   
    path('<int:id>/delete/', delete_constantpressure_test_data, name='delete_constantpressure_test_data'),
    path('<int:id>/cons_Pres/', upload_Constant_Pressure_test_data, name='upload_Constant_Pressure_test_data'), 
]