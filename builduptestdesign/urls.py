from django.urls import path
from .views import list_pbu_test_design, create_pbu_test_design, update_pbu_test_design,delete_pbu_test_design


app_name = 'builduptestdesign'

urlpatterns = [  
    path('', list_pbu_test_design, name='list_pbu_test_design'),
    path('create/', create_pbu_test_design, name='create_pbu_test_design'),
    path('<int:id>/update/', update_pbu_test_design, name='update_pbu_test_design'),   
    path('<int:id>/delete/', delete_pbu_test_design, name='delete_pbu_test_design'),
    
   
]