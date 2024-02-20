from django.urls import path
from gpcasings.views import list_gpcasings, create_gpcasing, update_gpcasing,delete_gpcasing, ajax_load_gpcasingWeight, ajax_load_gpcasingGrade

app_name = 'gpcasings'

urlpatterns = [  
    path('', list_gpcasings, name='list_gpcasings'),
    path('create/', create_gpcasing, name='create_gpcasing'),
    path('<int:id>/update/', update_gpcasing, name='update_gpcasing'),    
    path('<int:id>/delete/',delete_gpcasing, name='delete_gpcasing'),
    path('ajax_load_gpcasingWeight/', ajax_load_gpcasingWeight, name='ajax_load_gpcasingWeight'),
    path('ajax_load_gpcasingGrade/', ajax_load_gpcasingGrade, name='ajax_load_gpcasingGrade'),

]