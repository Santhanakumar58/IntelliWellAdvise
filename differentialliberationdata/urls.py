from django.urls import path
from .views import  list_difflibdata, create_difflibdata, update_difflibdata,delete_difflibdata, excel_upload_difflibdata

app_name = 'differentialliberationdata'

urlpatterns = [ 

    path('<int:diffid>/', list_difflibdata, name='list_difflibdata'),    
    path('<int:diffid>/create/', create_difflibdata, name='create_difflibdata'),
    path('<int:id>/update/', update_difflibdata, name='update_difflibdata'),   
    path('<int:id>/delete/', delete_difflibdata, name='delete_difflibdata'),
    path('<int:diffid>/upload', excel_upload_difflibdata, name='excel_upload_difflibdata'),
]