from django.urls import path
from  .views import list_obdrillingwelldata, create_obdrillingwelldata, update_obdrillingwelldata, delete_obdrillingwelldata

app_name = 'obdrillingwelldata'

urlpatterns = [
    path('', list_obdrillingwelldata, name='list_obdrillingwelldata'),   
    path('obdrillingwelldata/create/', create_obdrillingwelldata, name='create_obdrillingwelldata'),
    path('obdrillingwelldata/<int:id>/update/', update_obdrillingwelldata, name='update_obdrillingwelldata'),
    path('obdrillingwelldata/<int:id>/delete/',delete_obdrillingwelldata, name='delete_obdrillingwelldata'),
 
]