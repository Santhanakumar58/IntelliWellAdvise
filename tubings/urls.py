from django.urls import path
from tubings.views import list_tubings, create_tubing, update_tubing,delete_tubing, ajax_load_tubingWeight, ajax_load_tubingGrade

app_name = 'tubings'

urlpatterns = [  
    path('', list_tubings, name='list_tubings'),
    path('create/', create_tubing, name='create_tubing'),
    path('<int:id>/update/', update_tubing, name='update_tubing'),    
    path('<int:id>/delete/',delete_tubing, name='delete_tubing'),
    path('ajax_load_tubingWeight/', ajax_load_tubingWeight, name='ajax_load_tubingWeight'),
    path('ajax_load_tubingGrade/', ajax_load_tubingGrade, name='ajax_load_tubingGrade'),

]