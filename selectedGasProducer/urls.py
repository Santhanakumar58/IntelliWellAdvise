from django.urls import path
from  .views import list_selectedGasProducer, create_selectedGasProducer, update_selectedGasProducer, delete_selectedGasProducer,addselectedgp_ajax

app_name = 'selectedGasProducer'

urlpatterns = [
    path('', list_selectedGasProducer, name='list_selectedGasProducer'),   
    path('create/', create_selectedGasProducer, name='create_selectedGasProducer'),
    path('<int:id>/update/', update_selectedGasProducer, name='update_selectedGasProducer'),
    path('<int:id>/delete/',delete_selectedGasProducer, name='delete_selectedGasProducer'),
    path('addselectedgp_ajax/',addselectedgp_ajax, name='addselectedgp_ajax')  
]