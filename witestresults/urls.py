from django.urls import path
from .views import list_witestresult, create_witestresult, update_witestresult, delete_witestresult

app_name = 'witestresults'

urlpatterns = [  
    path('',list_witestresult, name='list_witestresult'),
    path('create/', create_witestresult, name='create_witestresult'),
    path('<int:id>/update/', update_witestresult, name='update_witestresult'),
    path('<int:id>/delete/', delete_witestresult, name='delete_witestresult'), 

]