from django.urls import path
from . import views

app_name = 'fgis'

urlpatterns = [  
    path('', views.FGIListView.as_view(), name='all'),
    path('fgis/<int:pk>/detail', views.FGIDetailView.as_view(), name='fgimodel_detail'),
    path('fgis/create/', views.FGICreateView.as_view(), name='fgimodel_create'),
    path('fgis/<int:pk>/update/', views.FGIUpdateView.as_view(), name='fgimodel_update'),
    path('fgis/<int:pk>/delete/', views.FGIDeleteView.as_view(), name='fgimodel_delete'),   
]