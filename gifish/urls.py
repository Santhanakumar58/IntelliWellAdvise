from django.urls import path
from .views import list_gifish, create_gifish, update_gifish,delete_gifish

app_name = 'gifish'

urlpatterns = [  
    path('', list_gifish, name='list_gifish'),
    path('create/', create_gifish, name='create_gifish'),
    path('<int:id>/update/', update_gifish, name='update_gifish'),   
    path('<int:id>/delete/', delete_gifish, name='delete_gifish'),
]