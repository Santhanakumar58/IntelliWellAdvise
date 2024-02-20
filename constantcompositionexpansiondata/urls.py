from django.urls import path
from .views import  list_ccepvtdata, create_ccepvtdata, update_ccepvtdata,delete_ccepvtdata, upload

app_name = 'constantcompositionexpansiondata'

urlpatterns = [ 

    path('<int:ccepvt>/', list_ccepvtdata, name='list_ccepvtdata'),    
    path('<int:ccepvt>/create/', create_ccepvtdata, name='create_ccepvtdata'),
    path('<int:id>/update/', update_ccepvtdata, name='update_ccepvtdata'),   
    path('<int:id>/delete/', delete_ccepvtdata, name='delete_ccepvtdata'),
    path('<int:ccepvt>/upload', upload, name='upload'),
]