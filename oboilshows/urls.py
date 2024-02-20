from django.urls import path
from .views import list_oboilshow, create_oboilshow, update_oboilshow, delete_oboilshow

app_name = 'oboilshows'

urlpatterns = [  
    path('',list_oboilshow, name='list_oboilshow'),
    path('create/', create_oboilshow, name='create_oboilshow'),
    path('<int:id>/update/', update_oboilshow, name='update_oboilshow'),
    path('<int:id>/delete/', delete_oboilshow, name='delete_oboilshow'), 

]