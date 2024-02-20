from django.urls import path
from .views import list_wiloganalysis, create_wiloganalysis, update_wiloganalysis,delete_wiloganalysis

app_name = 'wiloganalysis'

urlpatterns = [  
    path('', list_wiloganalysis, name='list_wiloganalysis'),
    path('create/', create_wiloganalysis, name='create_wiloganalysis'),
    path('<int:id>/update/', update_wiloganalysis, name='update_wiloganalysis'),    
    path('<int:id>/delete/',delete_wiloganalysis, name='delete_wiloganalysis')
]