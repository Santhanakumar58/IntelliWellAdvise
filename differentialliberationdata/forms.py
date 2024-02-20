from django import forms
from .models import DifferentialLiberationdata 


class DiffLibDATAForm(forms.ModelForm):
    class Meta:        
        model = DifferentialLiberationdata
        fields=["pressure", "solution_gor", "relative_oil_volume", "relative_total_volume", "oil_density","deviation_factor", "gas_fvf", "incremental_gas_gravity"]

     