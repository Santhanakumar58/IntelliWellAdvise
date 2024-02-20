from django.urls import path
from .views import  list_gpleakoffTestData, create_gpleakoffTestData, update_gpleakoffTestData, delete_gpleakoffTestData
 


app_name = 'gpleakoffTestData'
urlpatterns = [    
    path('<int:id>', list_gpleakoffTestData, name='list_gpleakoffTestData'),
    path('<int:id>create/', create_gpleakoffTestData, name='create_gpleakoffTestData'),
    path('<int:id>/update/', update_gpleakoffTestData, name='update_gpleakoffTestData'),    
    path('<int:id>/delete/',delete_gpleakoffTestData, name='delete_gpleakoffTestData'),
]