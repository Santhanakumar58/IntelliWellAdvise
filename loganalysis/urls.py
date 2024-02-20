from django.urls import path
from .views import list_loganalysis, create_loganalysis, update_loganalysis,delete_loganalysis
app_name = 'loganalysis'

urlpatterns = [  
    path('', list_loganalysis, name='list_loganalysis'),
    path('create/', create_loganalysis, name='create_loganalysis'),
    path('<int:id>/update/', update_loganalysis, name='update_loganalysis'),    
    path('<int:id>/delete/',delete_loganalysis, name='delete_loganalysis')
]