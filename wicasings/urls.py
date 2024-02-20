from django.urls import path
from wicasings.views import list_wicasings, create_wicasing, update_wicasing,delete_wicasing, ajax_load_wicasingWeight, ajax_load_wicasingGrade

app_name = 'wicasings'

urlpatterns = [  
    path('', list_wicasings, name='list_wicasings'),
    path('create/', create_wicasing, name='create_wicasing'),
    path('<int:id>/update/', update_wicasing, name='update_wicasing'),    
    path('<int:id>/delete/',delete_wicasing, name='delete_wicasing'),
    path('ajax_load_wicasingWeight/', ajax_load_wicasingWeight, name='ajax_load_wicasingWeight'),
    path('ajax_load_wicasingGrade/', ajax_load_wicasingGrade, name='ajax_load_wicasingGrade'),

]