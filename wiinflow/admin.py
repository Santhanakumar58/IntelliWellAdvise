from django.contrib import admin
from .models import WIProductivityIndexModel, WIVogelModel, WIStandingsModel, WIWigginsModel,WIMultirateModel, WIDarcyModel
# Register your models here.
admin.site.register(WIProductivityIndexModel)
admin.site.register(WIVogelModel)
admin.site.register(WIStandingsModel)
admin.site.register(WIWigginsModel)
admin.site.register(WIMultirateModel)
admin.site.register(WIDarcyModel)
