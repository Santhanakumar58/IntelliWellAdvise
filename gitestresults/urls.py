from django.urls import path
from .views import list_gitestresult, create_gitestresult, update_gitestresult, delete_gitestresult

app_name = 'gitestresults'

urlpatterns = [  
    path('',list_gitestresult, name='list_gitestresult'),
    path('create/', create_gitestresult, name='create_gitestresult'),
    path('<int:id>/update/', update_gitestresult, name='update_gitestresult'),
    path('<int:id>/delete/', delete_gitestresult, name='delete_gitestresult'), 

]