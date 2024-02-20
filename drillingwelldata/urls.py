from django.urls import path
from  .views import list_drillingwelldata, create_drillingwelldata, update_drillingwelldata, delete_drillingwelldata

app_name = 'drillingwelldata'

urlpatterns = [
    path('', list_drillingwelldata, name='list_drillingwelldata'),   
    path('drillingwelldata/create/', create_drillingwelldata, name='create_drillingwelldata'),
    path('drillingwelldata/<int:id>/update/', update_drillingwelldata, name='update_drillingwelldata'),
    path('drillingwelldata/<int:id>/delete/',delete_drillingwelldata, name='delete_drillingwelldata'),
 
]