from importlib import resources
from import_export import  resources
from constantcompositionexpansiondata.models import CCEPVTData

class CCEPVTdataResource(resources.ModelResource):
    class meta:
        model = CCEPVTData