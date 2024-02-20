from django.urls import path
from  .views import list_gidrillingwelldata, create_gidrillingwelldata, update_gidrillingwelldata, delete_gidrillingwelldata

app_name = 'gidrillingwelldata'

urlpatterns = [
    path('', list_gidrillingwelldata, name='list_gidrillingwelldata'),   
    path('gidrillingwelldata/create/', create_gidrillingwelldata, name='create_gidrillingwelldata'),
    path('gidrillingwelldata/<int:id>/update/', update_gidrillingwelldata, name='update_gidrillingwelldata'),
    path('gidrillingwelldata/<int:id>/delete/',delete_gidrillingwelldata, name='delete_gidrillingwelldata'),
 
]