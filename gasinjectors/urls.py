from django.urls import path
from .views import list_gasinjector, create_gasinjector, update_gasinjector,delete_gasinjector

app_name = 'gasinjectors'

urlpatterns = [  
    path('', list_gasinjector, name='list_gasinjector'),
    path('create/', create_gasinjector, name='create_gasinjector'),
    path('<int:id>/update/', update_gasinjector, name='update_gasinjector'),   
    path('<int:id>/delete/', delete_gasinjector, name='delete_gasinjector'),
]