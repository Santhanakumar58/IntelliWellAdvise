from django.urls import path
from  .views import list_selectedGasInjector, create_selectedGasInjector, update_selectedGasInjector, delete_selectedGasInjector,addselectedgi_ajax

app_name = 'selectedGasInjector'

urlpatterns = [
    path('', list_selectedGasInjector, name='list_selectedGasInjector'),   
    path('create/', create_selectedGasInjector, name='create_selectedGasInjector'),
    path('<int:id>/update/', update_selectedGasInjector, name='update_selectedGasInjector'),
    path('<int:id>/delete/',delete_selectedGasInjector, name='delete_selectedGasInjector'),
    path('addselectedgi_ajax/',addselectedgi_ajax, name='addselectedgi_ajax')  
]