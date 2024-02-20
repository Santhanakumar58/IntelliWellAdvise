from django.urls import path
from .views import  list_gileakoffTestData, create_gileakoffTestData, update_gileakoffTestData, delete_gileakoffTestData
 


app_name = 'gileakoffTestData'
urlpatterns = [    
    path('<int:id>', list_gileakoffTestData, name='list_gileakoffTestData'),
    path('<int:id>create/', create_gileakoffTestData, name='create_gileakoffTestData'),
    path('<int:id>/update/', update_gileakoffTestData, name='update_gileakoffTestData'),    
    path('<int:id>/delete/',delete_gileakoffTestData, name='delete_gileakoffTestData'),
]