from django.urls import path
from .views import  list_multirate_test_data, create_multirate_test_data,update_multirate_test_data, delete_multirate_test_data, upload_Multi_Rate_test_data


app_name = 'multiratedrawdowntestanalysis'

urlpatterns = [ 
    path('', list_multirate_test_data, name='list_multirate_test_data'),    
    path('create/', create_multirate_test_data, name='create_multirate_test_data'),
    path('<int:id>/update/', update_multirate_test_data, name='update_multirate_test_data'),   
    path('<int:id>/delete/', delete_multirate_test_data, name='delete_multirate_test_data'),
    path('<int:id>/multi_Rate/', upload_Multi_Rate_test_data, name='upload_Multi_Rate_test_data') 
]