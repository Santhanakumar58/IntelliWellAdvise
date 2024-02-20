from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields =['id', 'assetname', 'description', 'area', 'year', 'score_out_of_10']

  

   