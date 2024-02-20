from django.urls import path
from .views import  list_leakoffTestData, create_leakoffTestData, update_leakoffTestData, delete_leakoffTestData
 


app_name = 'leakoffTestData'
urlpatterns = [    
    path('<int:id>', list_leakoffTestData, name='list_leakoffTestData'),
    path('<int:id>create/', create_leakoffTestData, name='create_leakoffTestData'),
    path('<int:id>/update/', update_leakoffTestData, name='update_leakoffTestData'),    
    path('<int:id>/delete/',delete_leakoffTestData, name='delete_leakoffTestData'),
]