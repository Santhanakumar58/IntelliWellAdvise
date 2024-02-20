from django.urls import path
from .views import list_gptestresult, create_gptestresult, update_gptestresult, delete_gptestresult

app_name = 'gptestresults'

urlpatterns = [  
    path('',list_gptestresult, name='list_gptestresult'),
    path('create/', create_gptestresult, name='create_gptestresult'),
    path('<int:id>/update/', update_gptestresult, name='update_gptestresult'),
    path('<int:id>/delete/', delete_gptestresult, name='delete_gptestresult'), 

]