from importlib import resources
from import_export import  resources
from .models import GradientSurveyData

class GradientSurveyDataResource(resources.ModelResource):
    class meta:
        model = GradientSurveyData