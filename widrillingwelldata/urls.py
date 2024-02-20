from django.urls import path
from  .views import list_widrillingwelldata, create_widrillingwelldata, update_widrillingwelldata, delete_widrillingwelldata

app_name = 'widrillingwelldata'

urlpatterns = [
    path('', list_widrillingwelldata, name='list_widrillingwelldata'),   
    path('widrillingwelldata/create/', create_widrillingwelldata, name='create_widrillingwelldata'),
    path('widrillingwelldata/<int:id>/update/', update_widrillingwelldata, name='update_widrillingwelldata'),
    path('widrillingwelldata/<int:id>/delete/',delete_widrillingwelldata, name='delete_widrillingwelldata'),
 
]