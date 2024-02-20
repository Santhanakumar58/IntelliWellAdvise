from django.urls import path
from .views import list_giloganalysis, create_giloganalysis, update_giloganalysis,delete_giloganalysis

app_name = 'giloganalysis'

urlpatterns = [  
    path('', list_giloganalysis, name='list_giloganalysis'),
    path('create/', create_giloganalysis, name='create_giloganalysis'),
    path('<int:id>/update/', update_giloganalysis, name='update_giloganalysis'),    
    path('<int:id>/delete/',delete_giloganalysis, name='delete_giloganalysis')
]