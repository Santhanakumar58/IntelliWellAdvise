from django.urls import path
from .views import list_obfish, create_obfish, update_obfish,delete_obfish

app_name = 'obfish'

urlpatterns = [  
    path('', list_obfish, name='list_obfish'),
    path('create/', create_obfish, name='create_obfish'),
    path('<int:id>/update/', update_obfish, name='update_obfish'),   
    path('<int:id>/delete/', delete_obfish, name='delete_obfish'),
]