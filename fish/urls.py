from django.urls import path
from .views import list_fish, create_fish, update_fish,delete_fish

app_name = 'fish'

urlpatterns = [  
    path('', list_fish, name='list_fish'),
    path('create/', create_fish, name='create_fish'),
    path('<int:id>/update/', update_fish, name='update_fish'),   
    path('<int:id>/delete/', delete_fish, name='delete_fish'),
]