from django.urls import path
from gpbridgeplugs.views import list_gpbridgeplug, create_gpbridgeplug, update_gpbridgeplug,delete_gpbridgeplug

app_name = 'gpbridgeplugs'

urlpatterns = [  
    path('', list_gpbridgeplug, name='list_gpbridgeplug'),
    path('create/', create_gpbridgeplug, name='create_gpbridgeplug'),
    path('<int:id>/update/', update_gpbridgeplug, name='update_gpbridgeplug'),   
    path('<int:id>/delete/', delete_gpbridgeplug, name='delete_gpbridgeplug'),
]