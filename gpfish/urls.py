from django.urls import path
from .views import list_gpfish, create_gpfish, update_gpfish,delete_gpfish

app_name = 'gpfish'

urlpatterns = [  
    path('', list_gpfish, name='list_gpfish'),
    path('create/', create_gpfish, name='create_gpfish'),
    path('<int:id>/update/', update_gpfish, name='update_gpfish'),   
    path('<int:id>/delete/', delete_gpfish, name='delete_gpfish'),
]