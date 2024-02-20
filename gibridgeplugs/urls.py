from django.urls import path
from gibridgeplugs.views import list_gibridgeplug, create_gibridgeplug, update_gibridgeplug,delete_gibridgeplug

app_name = 'gibridgeplugs'

urlpatterns = [  
    path('', list_gibridgeplug, name='list_gibridgeplug'),
    path('create/', create_gibridgeplug, name='create_gibridgeplug'),
    path('<int:id>/update/', update_gibridgeplug, name='update_gibridgeplug'),   
    path('<int:id>/delete/', delete_gibridgeplug, name='delete_gibridgeplug'),
]