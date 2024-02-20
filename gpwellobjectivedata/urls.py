from django import views
from django.urls import path
from .views import  list_gpwellobjectivedata,create_gpwellobjectivedata,update_gpwellobjectivedata,delete_gpwellobjectivedata,Import_Excel_pandas

app_name = 'gpwellobjectivedata'

urlpatterns = [    
    path('<int:objid>', list_gpwellobjectivedata, name='list_gpwellobjectivedata'),    
    path('<int:objid>/create/', create_gpwellobjectivedata, name='create_gpwellobjectivedata'),
    path('<int:id>/update/', update_gpwellobjectivedata, name='update_gpwellobjectivedata'),   
    path('<int:id>/delete/', delete_gpwellobjectivedata, name='delete_gpwellobjectivedata'),
    path('<int:objid>/Import_Excel_pandas/', Import_Excel_pandas,  name='Import_Excel_pandas'),
   
   ]