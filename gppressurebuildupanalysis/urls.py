from django.urls import path
from .views import  list_gpbuildup_test_data, create_gpbuildup_test_data,update_gpbuildup_test_data, delete_gpbuildup_test_data, pbu_Analysis

app_name = 'gppressurebuildupanalysis'

urlpatterns = [ 
    path('', list_gpbuildup_test_data, name='list_gpbuildup_test_data'),    
    path('create/', create_gpbuildup_test_data, name='create_gpbuildup_test_data'),
    path('<int:id>/update/', update_gpbuildup_test_data, name='update_gpbuildup_test_data'),   
    path('<int:id>/delete/', delete_gpbuildup_test_data, name='delete_gpbuildup_test_data'),
    path('<int:id>/analysis/', pbu_Analysis, name='pbu_Analysis')
   ]