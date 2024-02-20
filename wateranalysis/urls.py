from django.urls import path
from  .views import list_wateranalysis, create_wateranalysis, update_wateranalysis, delete_wateranalysis

app_name = 'wateranalysis'

urlpatterns = [
    path('', list_wateranalysis, name='list_wateranalysis'),   
    path('create/', create_wateranalysis, name='create_wateranalysis'),
    path('<int:id>/update/', update_wateranalysis, name='update_wateranalysis'),
    path('<int:id>/delete/',delete_wateranalysis, name='delete_wateranalysis'),
     
]