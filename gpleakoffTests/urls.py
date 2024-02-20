from django.urls import path
from gpleakoffTests.views import list_gpleakoffTest, create_gpleakoffTest, update_gpleakoffTest,delete_gpleakoffTest
  

app_name = 'gpleakoffTests'
urlpatterns = [  
    path('<int:id>', list_gpleakoffTest, name='list_gpleakoffTest'),
    path('<int:id>create/', create_gpleakoffTest, name='create_gpleakoffTest'),
    path('<int:id>/update/', update_gpleakoffTest, name='update_gpleakoffTest'),    
    path('<int:id>/delete/',delete_gpleakoffTest, name='delete_gpleakoffTest')
]