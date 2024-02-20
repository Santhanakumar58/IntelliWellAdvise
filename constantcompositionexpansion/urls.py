from django.urls import path
from .views import  list_ccepvt, create_ccepvt,update_ccepvt, delete_ccepvt


app_name = 'constantcompositionexpansion'

urlpatterns = [ 
    path('', list_ccepvt, name='list_ccepvt'),    
    path('create/', create_ccepvt, name='create_ccepvt'),
    path('<int:id>/update/', update_ccepvt, name='update_ccepvt'),   
    path('<int:id>/delete/', delete_ccepvt, name='delete_ccepvt'),
   ]