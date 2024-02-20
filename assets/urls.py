from django.urls import path
from .views import list_assets, create_asset, update_asset,delete_asset

app_name = 'assets'

urlpatterns = [  
    path('', list_assets, name='list_assets'),
    path('create/', create_asset, name='create_asset'),
    path('<int:id>/update/', update_asset, name='update_asset'),   
    path('<int:id>/delete/', delete_asset, name='delete_asset'),
]