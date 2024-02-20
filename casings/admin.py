from django.contrib import admin
from .models import CasingModel, CasingSizeModel, CasingWeightModel, CasingGradeModel
# Register your models here.
admin.site.register(CasingModel)
admin.site.register(CasingSizeModel)
admin.site.register(CasingWeightModel)
admin.site.register(CasingGradeModel)