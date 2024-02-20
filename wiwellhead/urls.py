from django.urls import path
from  .views import list_wiwellhead, create_wiwellhead, update_wiwellhead, delete_wiwellhead

app_name = 'wiwellhead'

urlpatterns = [
    path('', list_wiwellhead, name='list_wiwellhead'),   
    path('create/', create_wiwellhead, name='create_wiwellhead'),
    path('<int:id>/update/', update_wiwellhead, name='update_wiwellhead'),
    path('<int:id>/delete/',delete_wiwellhead, name='delete_wiwellhead'),  
]