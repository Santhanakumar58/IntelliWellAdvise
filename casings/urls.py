from django.urls import path
from casings.views import list_casings, create_casing, update_casing,delete_casing, ajax_load_casingWeight, ajax_load_casingGrade

app_name = 'casings'

urlpatterns = [  
    path('', list_casings, name='list_casings'),
    path('create/', create_casing, name='create_casing'),
    path('<int:id>/update/', update_casing, name='update_casing'),    
    path('<int:id>/delete/',delete_casing, name='delete_casing'),
    path('ajax_load_casingWeight/', ajax_load_casingWeight, name='ajax_load_casingWeight'),
    path('ajax_load_casingGrade/', ajax_load_casingGrade, name='ajax_load_casingGrade'),

]