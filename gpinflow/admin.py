from django.contrib import admin
from .models import GPProductivityIndexModel, GPVogelModel, GPStandingsModel, GPWigginsModel,GPMultirateModel, GPDarcyModel
# Register your models here.
admin.site.register(GPProductivityIndexModel)
admin.site.register(GPVogelModel)
admin.site.register(GPStandingsModel)
admin.site.register(GPWigginsModel)
admin.site.register(GPMultirateModel)
admin.site.register(GPDarcyModel)
