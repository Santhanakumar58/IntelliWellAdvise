from django.urls import path
from wileakoffTests.views import list_wileakoffTest, create_wileakoffTest, update_wileakoffTest,delete_wileakoffTest
  

app_name = 'wileakoffTests'
urlpatterns = [  
    path('<int:id>', list_wileakoffTest, name='list_wileakoffTest'),
    path('<int:id>create/', create_wileakoffTest, name='create_wileakoffTest'),
    path('<int:id>/update/', update_wileakoffTest, name='update_wileakoffTest'),    
    path('<int:id>/delete/',delete_wileakoffTest, name='delete_wileakoffTest')
]