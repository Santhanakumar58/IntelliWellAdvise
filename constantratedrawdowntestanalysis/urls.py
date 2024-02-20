from django.urls import path
from .views import  list_const_rate_drawdown_test_data, create_const_rate_drawdown_test_data,update_const_rate_drawdown_test_data, delete_const_rate_drawdown_test_data, update_const_rate_drawdown_test_data, upload_Conatant_Rate_test_data 


app_name = 'constantratedrawdowntestanalysis'

urlpatterns = [ 
    path('', list_const_rate_drawdown_test_data, name='list_const_rate_drawdown_test_data'),    
    path('create/', create_const_rate_drawdown_test_data, name='create_const_rate_drawdown_test_data'),
    path('<int:id>/update/', update_const_rate_drawdown_test_data, name='update_const_rate_drawdown_test_data'),   
    path('<int:id>/delete/', delete_const_rate_drawdown_test_data, name='delete_const_rate_drawdown_test_data'),
    path('<int:id>/upload_Conatant_Rate_test_data/', upload_Conatant_Rate_test_data, name='upload_Conatant_Rate_test_data'),    
]