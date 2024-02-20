from django.urls import path
from giwellobjectivedata.views import  list_giwellobjectivedata, create_giwellobjectivedata, update_giwellobjectivedata,delete_giwellobjectivedata, Import_Excel_pandas

app_name = 'giwellobjectivedata'

urlpatterns = [    
    path('<int:objid>', list_giwellobjectivedata, name='list_giwellobjectivedata'),    
    path('<int:objid>/create/', create_giwellobjectivedata, name='create_giwellobjectivedata'),
    path('<int:id>/update/', update_giwellobjectivedata, name='update_giwellobjectivedata'),   
    path('<int:id>/delete/', delete_giwellobjectivedata, name='delete_giwellobjectivedata'),
    path('<int:objid>/Import_Excel_pandas/', Import_Excel_pandas,  name='Import_Excel_pandas'),
   
   ]