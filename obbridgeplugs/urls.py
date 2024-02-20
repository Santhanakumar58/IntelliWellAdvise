from django.urls import path
from obbridgeplugs.views import list_obbridgeplug, create_obbridgeplug, update_obbridgeplug,delete_obbridgeplug

app_name = 'obbridgeplugs'

urlpatterns = [  
    path('', list_obbridgeplug, name='list_obbridgeplug'),
    path('create/', create_obbridgeplug, name='create_obbridgeplug'),
    path('<int:id>/update/', update_obbridgeplug, name='update_obbridgeplug'),   
    path('<int:id>/delete/', delete_obbridgeplug, name='delete_obbridgeplug'),
]