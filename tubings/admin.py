from django.contrib import admin
from .models import TubingModel, TubingSizeModel, TubingWeightModel, TubingGradeModel
# Register your models here.
admin.site.register(TubingModel)
admin.site.register(TubingSizeModel)
admin.site.register(TubingWeightModel)
admin.site.register(TubingGradeModel)
