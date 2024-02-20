from django.urls import path
from gasproducers.views import list_gasproducer, create_gasproducer, update_gasproducer,delete_gasproducer

app_name = 'gasproducers'

urlpatterns = [  
    path('', list_gasproducer, name='list_gasproducer'),
    path('create/', create_gasproducer, name='create_gasproducer'),
    path('<int:id>/update/', update_gasproducer, name='update_gasproducer'),   
    path('<int:id>/delete/', delete_gasproducer, name='delete_gasproducer'),
]