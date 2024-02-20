from django.urls import path
from .views import  list_obwellobjectivedata, create_obwellobjectivedata, update_obwellobjectivedata,delete_obwellobjectivedata, Import_Excel_pandas

app_name = 'obwellobjectivedata'

urlpatterns = [    
    path('<int:objid>', list_obwellobjectivedata, name='list_obwellobjectivedata'),    
    path('<int:objid>/create/', create_obwellobjectivedata, name='create_obwellobjectivedata'),
    path('<int:id>/update/', update_obwellobjectivedata, name='update_obwellobjectivedata'),   
    path('<int:id>/delete/', delete_obwellobjectivedata, name='delete_obwellobjectivedata'),
    path('<int:objid>/Import_Excel_pandas/', Import_Excel_pandas,  name='Import_Excel_pandas'),
   
   ]