from importlib import resources
from import_export import  resources
from .models import GIGradientSurveyData

class GIGradientSurveyDataResource(resources.ModelResource):
    class meta:
        model = GIGradientSurveyData