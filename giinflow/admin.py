from django.contrib import admin
from .models import GIProductivityIndexModel, GIVogelModel, GIStandingsModel, GIWigginsModel,GIMultirateModel, GIDarcyModel
# Register your models here.
admin.site.register(GIProductivityIndexModel)
admin.site.register(GIVogelModel)
admin.site.register(GIStandingsModel)
admin.site.register(GIWigginsModel)
admin.site.register(GIMultirateModel)
admin.site.register(GIDarcyModel)
