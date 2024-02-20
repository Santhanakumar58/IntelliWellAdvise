from django.urls import path
from .views import  list_drawdown_test_data, create_drawdown_test_data,update_drawdown_test_data, delete_drawdown_test_data, upload_Conatant_Rate_test_data, upload_Constant_Pressure_test_data, upload_Multi_Rate_test_data


app_name = 'drawdowntestanalysis'

urlpatterns = [ 
    path('', list_drawdown_test_data, name='list_drawdown_test_data'),    
    path('create/', create_drawdown_test_data, name='create_drawdown_test_data'),
    path('<int:id>/update/', update_drawdown_test_data, name='update_drawdown_test_data'),   
    path('<int:id>/delete/', delete_drawdown_test_data, name='delete_drawdown_test_data'),
    path('<int:id>/cons_Rate/', upload_Conatant_Rate_test_data, name='upload_Conatant_Rate_test_data'),    
    path('<int:id>/cons_Pres/', upload_Constant_Pressure_test_data, name='upload_Constant_Pressure_test_data'), 
    path('<int:id>/multi_Rate/', upload_Multi_Rate_test_data, name='upload_Multi_Rate_test_data') 
]