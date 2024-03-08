from django.shortcuts import render, redirect
from .models import Asset
from .forms import AssetForm

 
def list_assets(request):
    assets = Asset.objects.all()
    return render (request, 'assets/assets.html', {'assets': assets})
 
def create_asset(request):
   form = AssetForm(request.POST or None)
   if form.is_valid():
       form.save()
       return redirect ('assets:list_assets')
   return render (request, 'assets/assets_form.html', {'form': form})

def update_asset(request, id):
   asset = Asset.objects.get(id=id)
   form = AssetForm(request.POST or None, instance=asset)   
   if form.is_valid():
        form.save()
        return redirect ('assets:list_assets')
   return render (request, 'assets/assets_form.html', {'form': form, 'asset':asset})

def delete_asset(request, id):
   asset = Asset.objects.get(id=id)   
   if request.method == 'POST' :
       asset.delete()
       return redirect ('assets:list_assets')
   return render (request, 'assets/asset_confirm_delete.html', {'asset':asset})


