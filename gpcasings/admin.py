from django.contrib import admin
from .models import GPCasingModel, GPCasingSizeModel, GPCasingWeightModel, GPCasingGradeModel
# Register your models here.
admin.site.register(GPCasingModel)
admin.site.register(GPCasingSizeModel)
admin.site.register(GPCasingWeightModel)
admin.site.register(GPCasingGradeModel)
