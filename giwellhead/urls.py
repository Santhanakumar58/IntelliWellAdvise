from django.urls import path
from  .views import list_giwellhead, create_giwellhead, update_giwellhead, delete_giwellhead

app_name = 'giwellhead'

urlpatterns = [
    path('', list_giwellhead, name='list_giwellhead'),   
    path('create/', create_giwellhead, name='create_giwellhead'),
    path('<int:id>/update/', update_giwellhead, name='update_giwellhead'),
    path('<int:id>/delete/',delete_giwellhead, name='delete_giwellhead'),  
]