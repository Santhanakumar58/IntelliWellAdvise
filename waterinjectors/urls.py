from django.urls import path
from .views import list_waterinjector, create_waterinjector, update_waterinjector,delete_waterinjector

app_name = 'waterinjectors'

urlpatterns = [  
    path('', list_waterinjector, name='list_waterinjector'),
    path('create/', create_waterinjector, name='create_waterinjector'),
    path('<int:id>/update/', update_waterinjector, name='update_waterinjector'),   
    path('<int:id>/delete/', delete_waterinjector, name='delete_waterinjector'),
]