from django.urls import path
from obleakoffTests.views import list_obleakoffTest, create_obleakoffTest, update_obleakoffTest,delete_obleakoffTest
  

app_name = 'obleakoffTests'
urlpatterns = [  
    path('<int:id>', list_obleakoffTest, name='list_obleakoffTest'),
    path('<int:id>create/', create_obleakoffTest, name='create_obleakoffTest'),
    path('<int:id>/update/', update_obleakoffTest, name='update_obleakoffTest'),    
    path('<int:id>/delete/',delete_obleakoffTest, name='delete_obleakoffTest')
]