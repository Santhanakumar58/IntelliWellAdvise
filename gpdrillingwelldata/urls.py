from django.urls import path
from  .views import list_gpdrillingwelldata, create_gpdrillingwelldata, update_gpdrillingwelldata, delete_gpdrillingwelldata

app_name = 'gpdrillingwelldata'

urlpatterns = [
    path('', list_gpdrillingwelldata, name='list_gpdrillingwelldata'),   
    path('gpdrillingwelldata/create/', create_gpdrillingwelldata, name='create_gpdrillingwelldata'),
    path('gpdrillingwelldata/<int:id>/update/', update_gpdrillingwelldata, name='update_gpdrillingwelldata'),
    path('gpdrillingwelldata/<int:id>/delete/',delete_gpdrillingwelldata, name='delete_gpdrillingwelldata'),
 
]