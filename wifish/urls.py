from django.urls import path
from .views import list_wifish, create_wifish, update_wifish,delete_wifish

app_name = 'wifish'

urlpatterns = [  
    path('', list_wifish, name='list_wifish'),
    path('create/', create_wifish, name='create_wifish'),
    path('<int:id>/update/', update_wifish, name='update_wifish'),   
    path('<int:id>/delete/', delete_wifish, name='delete_wifish'),
]