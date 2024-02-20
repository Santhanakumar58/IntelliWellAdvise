from django.urls import path
from  .views import list_selectedObserver, create_selectedObserver, update_selectedObserver, delete_selectedObserver,addselectedob_ajax

app_name = 'selectedObserver'

urlpatterns = [
    path('', list_selectedObserver, name='list_selectedObserver'),   
    path('create/', create_selectedObserver, name='create_selectedObserver'),
    path('<int:id>/update/', update_selectedObserver, name='update_selectedObserver'),
    path('<int:id>/delete/',delete_selectedObserver, name='delete_selectedObserver'),
    path('addselectedob_ajax/',addselectedob_ajax, name='addselectedob_ajax')  
]