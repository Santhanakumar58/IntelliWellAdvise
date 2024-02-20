from django.urls import path
from wiwellobjectivedata.views import  list_wiwellobjectivedata, create_wiwellobjectivedata, update_wiwellobjectivedata,delete_wiwellobjectivedata, Import_Excel_pandas

app_name = 'wiwellobjectivedata'

urlpatterns = [    
    path('<int:objid>', list_wiwellobjectivedata, name='list_wiwellobjectivedata'),    
    path('<int:objid>/create/', create_wiwellobjectivedata, name='create_wiwellobjectivedata'),
    path('<int:id>/update/', update_wiwellobjectivedata, name='update_wiwellobjectivedata'),   
    path('<int:id>/delete/', delete_wiwellobjectivedata, name='delete_wiwellobjectivedata'),
    path('<int:objid>/Import_Excel_pandas/', Import_Excel_pandas,  name='Import_Excel_pandas'),
   
   ]