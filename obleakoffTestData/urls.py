from django.urls import path
from .views import  list_obleakoffTestData, create_obleakoffTestData, update_obleakoffTestData, delete_obleakoffTestData
 


app_name = 'obleakoffTestData'
urlpatterns = [    
    path('<int:id>', list_obleakoffTestData, name='list_obleakoffTestData'),
    path('<int:id>create/', create_obleakoffTestData, name='create_obleakoffTestData'),
    path('<int:id>/update/', update_obleakoffTestData, name='update_obleakoffTestData'),    
    path('<int:id>/delete/',delete_obleakoffTestData, name='delete_obleakoffTestData'),
]