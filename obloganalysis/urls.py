from django.urls import path
from .views import list_obloganalysis, create_obloganalysis, update_obloganalysis,delete_obloganalysis
app_name = 'obloganalysis'

urlpatterns = [  
    path('', list_obloganalysis, name='list_obloganalysis'),
    path('create/', create_obloganalysis, name='create_obloganalysis'),
    path('<int:id>/update/', update_obloganalysis, name='update_obloganalysis'),    
    path('<int:id>/delete/',delete_obloganalysis, name='delete_obloganalysis')
]