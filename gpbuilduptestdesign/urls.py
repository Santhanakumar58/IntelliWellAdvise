from django.urls import path
from .views import list_gppbu_test_design, create_gppbu_test_design, update_gppbu_test_design,delete_gppbu_test_design


app_name = 'gpbuilduptestdesign'

urlpatterns = [  
    path('', list_gppbu_test_design, name='list_gppbu_test_design'),
    path('create/', create_gppbu_test_design, name='create_gppbu_test_design'),
    path('<int:id>/update/', update_gppbu_test_design, name='update_gppbu_test_design'),   
    path('<int:id>/delete/', delete_gppbu_test_design, name='delete_gppbu_test_design'),
    
   
]