from django.urls import path
from  .views import list_selectedOilProducer, create_selectedOilProducer, update_selectedOilProducer, delete_selectedOilProducer,addselectedop_ajax

app_name = 'selectedOilProducer'

urlpatterns = [
    path('', list_selectedOilProducer, name='list_selectedOilProducer'),   
    path('create/', create_selectedOilProducer, name='create_selectedOilProducer'),
    path('<int:id>/update/', update_selectedOilProducer, name='update_selectedOilProducer'),
    path('<int:id>/delete/',delete_selectedOilProducer, name='delete_selectedOilProducer'),
    path('addselectedop_ajax/',addselectedop_ajax, name='addselectedop_ajax')  
]