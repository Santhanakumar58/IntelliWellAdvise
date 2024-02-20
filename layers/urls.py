from django.urls import path
from . import views 
from .views import Layer_Volumetrics

app_name = 'layers'

urlpatterns = [  
    path('', views.LayerListView.as_view(), name='all'),
    path('layers/<int:pk>/detail', views.LayerDetailView.as_view(), name='layer_detail'),
    path('layers/create/', views.LayerCreateView.as_view(), name='layer_create'),
    path('layers/<int:pk>/update/', views.LayerUpdateView.as_view(), name='layer_update'),
    path('layers/<int:pk>/delete/', views.LayerDeleteView.as_view(), name='layer_delete'),  
    path('layers/<int:pk>/volumetrics/', Layer_Volumetrics, name='layer_volumetrics'),
]