from django import views
from django.urls import path
from .views import  list_opwellobjectivedata,create_opwellobjectivedata,update_opwellobjectivedata,delete_opwellobjectivedata,Import_Excel_pandas

app_name = 'opwellobjectivedata'

urlpatterns = [ 

   
    path('<int:objid>', list_opwellobjectivedata, name='list_opwellobjectivedata'),    
    path('<int:objid>/create/', create_opwellobjectivedata, name='create_opwellobjectivedata'),
    path('<int:id>/update/', update_opwellobjectivedata, name='update_opwellobjectivedata'),   
    path('<int:id>/delete/', delete_opwellobjectivedata, name='delete_opwellobjectivedata'),
    path('<int:objid>/Import_Excel_pandas/', Import_Excel_pandas,  name='Import_Excel_pandas'),
   
   ]