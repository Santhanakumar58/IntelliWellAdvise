from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Deviationsurveydata)
class ViewAdmin(ImportExportModelAdmin):
   pass