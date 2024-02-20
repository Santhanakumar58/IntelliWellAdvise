from django.urls import path
from  .views import list_selectedfgi, create_selectedfgi, update_selectedfgi, delete_selectedfgi,addselectedfgi_ajax

app_name = 'selectedfgi'

urlpatterns = [
    path('', list_selectedfgi, name='list_selectedfgi'),   
    path('create/', create_selectedfgi, name='create_selectedfgi'),
    path('<int:id>/update/', update_selectedfgi, name='update_selectedfgi'),
    path('<int:id>/delete/',delete_selectedfgi, name='delete_selectedfgi'),
    path('addselectedfgi_ajax/', addselectedfgi_ajax, name='addselectedfgi_ajax'),   
]