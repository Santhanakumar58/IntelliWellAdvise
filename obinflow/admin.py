from django.contrib import admin
from .models import OBProductivityIndexModel, OBVogelModel, OBStandingsModel, OBWigginsModel,OBMultirateModel, OBDarcyModel
# Register your models here.
admin.site.register(OBProductivityIndexModel)
admin.site.register(OBVogelModel)
admin.site.register(OBStandingsModel)
admin.site.register(OBWigginsModel)
admin.site.register(OBMultirateModel)
admin.site.register(OBDarcyModel)
