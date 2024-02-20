from django.urls import path
from .views import  list_wileakoffTestData, create_wileakoffTestData, update_wileakoffTestData, delete_wileakoffTestData
 


app_name = 'wileakoffTestData'
urlpatterns = [    
    path('<int:id>', list_wileakoffTestData, name='list_wileakoffTestData'),
    path('<int:id>create/', create_wileakoffTestData, name='create_wileakoffTestData'),
    path('<int:id>/update/', update_wileakoffTestData, name='update_wileakoffTestData'),    
    path('<int:id>/delete/',delete_wileakoffTestData, name='delete_wileakoffTestData'),
]