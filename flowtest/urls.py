from django.urls import path
from .views import *

app_name = 'flowtest'

urlpatterns = [  
    path('', list_flowtest, name='list_flowtest'),
    path('create/', create_flowtest, name='create_flowtest'),
    path('<int:id>/update/', update_flowtest, name='update_flowtest'),   
    path('<int:id>/delete/', delete_flowtest, name='delete_flowtest'),
    path('load_from_Excel/', load_from_Excel,  name='load_from_Excel'),
    path('production_home/', production_home,  name='production_home'),
    path('pressure_vs_depth/', pressure_vs_depth,  name='pressure_vs_depth'),
    path('inflow_outflow/', inflow_outflow,  name='inflow_outflow'),
    path('tubing_Sensitivity/', tubing_Sensitivity,  name='tubing_Sensitivity'),
    path('gor_Sensitivity/', gor_Sensitivity,  name='gor_Sensitivity'),
    path('gaslift_design/', gaslift_design,  name='gaslift_design'),
]
