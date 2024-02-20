from django.contrib import admin
from .models import GradientSurveyData
from opgradientsurveys.models import GradientSurvey
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(GradientSurveyData)
class ViewAdmin(ImportExportModelAdmin):
   pass
    