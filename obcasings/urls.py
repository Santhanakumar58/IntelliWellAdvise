from django.urls import path
from obcasings.views import list_obcasings, create_obcasing, update_obcasing,delete_obcasing, ajax_load_obcasingWeight, ajax_load_obcasingGrade

app_name = 'obcasings'

urlpatterns = [  
    path('', list_obcasings, name='list_obcasings'),
    path('create/', create_obcasing, name='create_obcasing'),
    path('<int:id>/update/', update_obcasing, name='update_obcasing'),    
    path('<int:id>/delete/',delete_obcasing, name='delete_obcasing'),
    path('ajax_load_obcasingWeight/', ajax_load_obcasingWeight, name='ajax_load_obcasingWeight'),
    path('ajax_load_obcasingGrade/', ajax_load_obcasingGrade, name='ajax_load_obcasingGrade'),

]