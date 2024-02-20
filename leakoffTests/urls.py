from django.urls import path
from leakoffTests.views import list_leakoffTest, create_leakoffTest, update_leakoffTest,delete_leakoffTest
  

app_name = 'leakoffTests'
urlpatterns = [  
    path('<int:id>', list_leakoffTest, name='list_leakoffTest'),
    path('<int:id>create/', create_leakoffTest, name='create_leakoffTest'),
    path('<int:id>/update/', update_leakoffTest, name='update_leakoffTest'),    
    path('<int:id>/delete/',delete_leakoffTest, name='delete_leakoffTest')
]