from django.contrib import admin
from .models import ProductivityIndexModel, VogelModel, StandingsModel, WigginsModel,MultirateModel, DarcyModel
# Register your models here.
admin.site.register(ProductivityIndexModel)
admin.site.register(VogelModel)
admin.site.register(StandingsModel)
admin.site.register(WigginsModel)
admin.site.register(MultirateModel)
admin.site.register( DarcyModel)