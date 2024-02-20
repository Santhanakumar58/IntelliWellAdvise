from django.urls import path
from oilproducers.views import list_oilproducer, create_oilproducer, update_oilproducer,delete_oilproducer

app_name = 'oilproducers'

urlpatterns = [  
    path('', list_oilproducer, name='list_oilproducer'),
    path('create/', create_oilproducer, name='create_oilproducer'),
    path('<int:id>/update/', update_oilproducer, name='update_oilproducer'),   
    path('<int:id>/delete/', delete_oilproducer, name='delete_oilproducer'),
]