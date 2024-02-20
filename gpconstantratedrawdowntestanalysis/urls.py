from django.urls import path
from .views import  list_gpconst_rate_drawdown_test_data, create_gpconst_rate_drawdown_test_data,update_gpconst_rate_drawdown_test_data, delete_gpconst_rate_drawdown_test_data, update_gpconst_rate_drawdown_test_data, upload_Conatant_Rate_test_data 


app_name = 'gpconstantratedrawdowntestanalysis'

urlpatterns = [ 
    path('', list_gpconst_rate_drawdown_test_data, name='list_gpconst_rate_drawdown_test_data'),    
    path('create/', create_gpconst_rate_drawdown_test_data, name='create_gpconst_rate_drawdown_test_data'),
    path('<int:id>/update/', update_gpconst_rate_drawdown_test_data, name='update_gpconst_rate_drawdown_test_data'),   
    path('<int:id>/delete/', delete_gpconst_rate_drawdown_test_data, name='delete_gpconst_rate_drawdown_test_data'),
    path('<int:id>/upload_Conatant_Rate_test_data/', upload_Conatant_Rate_test_data, name='upload_Conatant_Rate_test_data'),    
]