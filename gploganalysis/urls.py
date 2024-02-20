from django.urls import path
from .views import list_gploganalysis, create_gploganalysis, update_gploganalysis,delete_gploganalysis
app_name = 'gploganalysis'

urlpatterns = [  
    path('', list_gploganalysis, name='list_gploganalysis'),
    path('create/', create_gploganalysis, name='create_gploganalysis'),
    path('<int:id>/update/', update_gploganalysis, name='update_gploganalysis'),    
    path('<int:id>/delete/',delete_gploganalysis, name='delete_gploganalysis')
]