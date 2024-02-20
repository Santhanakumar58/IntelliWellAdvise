from django.urls import path
from .views import list_testresult, create_testresult, update_testresult, delete_testresult

app_name = 'testresults'

urlpatterns = [  
    path('',list_testresult, name='list_testresult'),
    path('create/', create_testresult, name='create_testresult'),
    path('<int:id>/update/', update_testresult, name='update_testresult'),
    path('<int:id>/delete/', delete_testresult, name='delete_testresult'), 

]