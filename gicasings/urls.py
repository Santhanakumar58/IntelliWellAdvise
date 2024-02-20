from django.urls import path
from gicasings.views import list_gicasings, create_gicasing, update_gicasing,delete_gicasing, ajax_load_gicasingWeight, ajax_load_gicasingGrade

app_name = 'gicasings'

urlpatterns = [  
    path('', list_gicasings, name='list_gicasings'),
    path('create/', create_gicasing, name='create_gicasing'),
    path('<int:id>/update/', update_gicasing, name='update_gicasing'),    
    path('<int:id>/delete/',delete_gicasing, name='delete_gicasing'),
    path('ajax_load_gicasingWeight/', ajax_load_gicasingWeight, name='ajax_load_gicasingWeight'),
    path('ajax_load_gicasingGrade/', ajax_load_gicasingGrade, name='ajax_load_gicasingGrade'),

]