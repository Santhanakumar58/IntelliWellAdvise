from django.urls import path
from .views import  list_gpmultirate_test_data, create_gpmultirate_test_data,update_gpmultirate_test_data, delete_gpmultirate_test_data, upload_Multi_Rate_test_data


app_name = 'gpmultiratedrawdowntestanalysis'

urlpatterns = [ 
    path('', list_gpmultirate_test_data, name='list_gpmultirate_test_data'),    
    path('create/', create_gpmultirate_test_data, name='create_gpmultirate_test_data'),
    path('<int:id>/update/', update_gpmultirate_test_data, name='update_gpmultirate_test_data'),   
    path('<int:id>/delete/', delete_gpmultirate_test_data, name='delete_gpmultirate_test_data'),
    path('<int:id>/multi_Rate/', upload_Multi_Rate_test_data, name='upload_Multi_Rate_test_data') 
]