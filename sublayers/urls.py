from django.urls import path
from . import views

app_name = 'sublayers'

urlpatterns = [  
    path('', views.SublayerListView.as_view(), name='all'),
    path('sublayers/<int:pk>/detail', views.SublayerDetailView.as_view(), name='sublayer_detail'),
    path('sublayers/create/', views.SublayerCreateView.as_view(), name='sublayer_create'),
    path('sublayers/<int:pk>/update/', views.SublayerUpdateView.as_view(), name='sublayer_update'),
    path('sublayers/<int:pk>/delete/', views.SublayerDeleteView.as_view(), name='sublayer_delete'),
]