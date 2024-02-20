from django.contrib import admin
from .models import GPPressureBuildupModel, GPPressureBuildupDataUploadModel

# Register your models here.
admin.site.register(GPPressureBuildupModel)
admin.site.register(GPPressureBuildupDataUploadModel)
