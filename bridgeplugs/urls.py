from django.urls import path
from bridgeplugs.views import list_bridgeplug, create_bridgeplug, update_bridgeplug,delete_bridgeplug

app_name = 'bridgeplugs'

urlpatterns = [  
    path('', list_bridgeplug, name='list_bridgeplug'),
    path('create/', create_bridgeplug, name='create_bridgeplug'),
    path('<int:id>/update/', update_bridgeplug, name='update_bridgeplug'),    
    path('<int:id>/delete/',delete_bridgeplug, name='delete_bridgeplug'),

]