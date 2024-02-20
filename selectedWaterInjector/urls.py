from django.urls import path
from  .views import list_selectedWaterInjector, create_selectedWaterInjector, update_selectedWaterInjector, delete_selectedWaterInjector,addselectedwi_ajax

app_name = 'selectedWaterInjector'

urlpatterns = [
    path('', list_selectedWaterInjector, name='list_selectedWaterInjector'),   
    path('create/', create_selectedWaterInjector, name='create_selectedWaterInjector'),
    path('<int:id>/update/', update_selectedWaterInjector, name='update_selectedWaterInjector'),
    path('<int:id>/delete/',delete_selectedWaterInjector, name='delete_selectedWaterInjector'),
    path('addselectedwi_ajax/',addselectedwi_ajax, name='addselectedwi_ajax')  
]