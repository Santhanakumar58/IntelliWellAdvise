from django.urls import path
from . import views

app_name = 'oilfields'

urlpatterns = [  
    path('', views.OilfieldListView.as_view(), name='all'),
    path('oilfields/<int:pk>/detail', views.OilfieldDetailView.as_view(), name='oilfield_detail'),
    path('oilfields/create/', views.OilfieldCreateView.as_view(), name='oilfield_create'),
    path('oilfields/<int:pk>/update/', views.OilfieldUpdateView.as_view(), name='oilfield_update'),
    path('oilfields/<int:pk>/delete/', views.OilfieldDeleteView.as_view(), name='oilfield_delete'),
]