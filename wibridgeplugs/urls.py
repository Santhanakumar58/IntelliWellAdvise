from django.urls import path
from wibridgeplugs.views import list_wibridgeplug, create_wibridgeplug, update_wibridgeplug,delete_wibridgeplug

app_name = 'wibridgeplugs'

urlpatterns = [  
    path('', list_wibridgeplug, name='list_wibridgeplug'),
    path('create/', create_wibridgeplug, name='create_wibridgeplug'),
    path('<int:id>/update/', update_wibridgeplug, name='update_wibridgeplug'),   
    path('<int:id>/delete/', delete_wibridgeplug, name='delete_wibridgeplug'),
]