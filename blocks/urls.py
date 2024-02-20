from django.urls import path
from . import views

app_name = 'blocks'

urlpatterns = [  
    path('', views.BlockListView.as_view(), name='all'),
    path('blocks/<int:pk>/detail', views.BlockDetailView.as_view(), name='block_detail'),
    path('blocks/create/', views.BlockCreateView.as_view(), name='block_create'),
    path('blocks/<int:pk>/update/', views.BlockUpdateView.as_view(), name='block_update'),
    path('blocks/<int:pk>/delete/', views.BlockDeleteView.as_view(), name='block_delete'),
]