from django.urls import path
from .views import  list_multirate_test_pbu_design, create_multirate_test_pbu_design,update_multirate_test_pbu_design, delete_multirate_test_pbu_design


app_name = 'multiratepbudesign'

urlpatterns = [ 
    path('', list_multirate_test_pbu_design, name='list_multirate_test_pbu_design'),    
    path('create/', create_multirate_test_pbu_design, name='create_multirate_test_pbu_design'),
    path('<int:id>/update/', update_multirate_test_pbu_design, name='update_multirate_test_pbu_design'),   
    path('<int:id>/delete/', delete_multirate_test_pbu_design, name='delete_multirate_test_pbu_design'),
    
]