from django.urls import path
from gileakoffTests.views import list_gileakoffTest, create_gileakoffTest, update_gileakoffTest,delete_gileakoffTest
  

app_name = 'gileakoffTests'
urlpatterns = [  
    path('<int:id>', list_gileakoffTest, name='list_gileakoffTest'),
    path('<int:id>create/', create_gileakoffTest, name='create_gileakoffTest'),
    path('<int:id>/update/', update_gileakoffTest, name='update_gileakoffTest'),    
    path('<int:id>/delete/',delete_gileakoffTest, name='delete_gileakoffTest')
]