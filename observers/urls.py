from django.urls import path
from .views import list_observer, create_observer, update_observer,delete_observer

app_name = 'observers'

urlpatterns = [  
    path('', list_observer, name='list_observer'),
    path('create/', create_observer, name='create_observer'),
    path('<int:id>/update/', update_observer, name='update_observer'),   
    path('<int:id>/delete/', delete_observer, name='delete_observer'),
]