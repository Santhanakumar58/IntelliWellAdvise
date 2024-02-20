from django.urls import path
from .views import list_obtestresult, create_obtestresult, update_obtestresult, delete_obtestresult

app_name = 'obtestresults'

urlpatterns = [  
    path('',list_obtestresult, name='list_obtestresult'),
    path('create/', create_obtestresult, name='create_obtestresult'),
    path('<int:id>/update/', update_obtestresult, name='update_obtestresult'),
    path('<int:id>/delete/', delete_obtestresult, name='delete_obtestresult'), 

]