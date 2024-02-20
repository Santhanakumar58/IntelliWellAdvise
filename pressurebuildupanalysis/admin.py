from django.contrib import admin
from .models import PressureBuildupModel, PressureBuildupDataUploadModel

# Register your models here.
admin.site.register(PressureBuildupModel)
admin.site.register(PressureBuildupDataUploadModel)



