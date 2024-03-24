from django.urls import path
from .views import  list_buildup_test_data, create_buildup_test_data,update_buildup_test_data, delete_buildup_test_data, Calculate_Constant_Rate_Buildup_test

app_name = 'pressurebuildupanalysis'

urlpatterns = [ 
    path('', list_buildup_test_data, name='list_buildup_test_data'),    
    path('create/', create_buildup_test_data, name='create_buildup_test_data'),
    path('<int:id>/update/', update_buildup_test_data, name='update_buildup_test_data'),   
    path('<int:id>/delete/', delete_buildup_test_data, name='delete_buildup_test_data'),
    path('<int:id>/analysis/', Calculate_Constant_Rate_Buildup_test, name='Calculate_Constant_Rate_Buildup_test')
   ]