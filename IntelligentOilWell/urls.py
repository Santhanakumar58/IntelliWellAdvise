"""
URL configuration for IntelligentOilWell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Home.urls")), 
    # Fieldwide Applications
    path("assets", include("assets.urls")),
    path("blocks", include("blocks.urls")),
    path("oilfields", include("oilfields.urls")),
    path("layers", include("layers.urls")),
    path("sublayers", include("sublayers.urls")),
    path("fgis", include("fgis.urls")),
    path("selectedfgi", include("selectedfgi.urls")),
    path("oilproducers", include("oilproducers.urls")),
    path("selectedOilProducer", include("selectedOilProducer.urls")),
    path("blackoilpvt", include("blackoilpvt.urls")),
    path("reservoirfluidcomposition", include("reservoirfluidcomposition.urls")),
    path("reservoirfluidcompositiondata", include("reservoirfluidcompositiondata.urls")),
    path("constantcompositionexpansion", include("constantcompositionexpansion.urls")),
    path("constantcompositionexpansiondata", include("constantcompositionexpansiondata.urls")),
    path("differentialliberation", include("differentialliberation.urls")),
    path("differentialliberationdata", include("differentialliberationdata.urls")),
    path("opwellobjectives", include("opwellobjectives.urls")),
    path("opwellobjectivedata", include("opwellobjectivedata.urls")),
    path("wateranalysis", include("wateranalysis.urls")),
    #---------------------------------------------------------------------------------------------------
    # Oil Producer Applications
    #---------------------------------------------------------------------------------------------------

    # Geology
    path("cuttingdescription", include ("cuttingdescription.urls")),
    path("formationtops", include ("formationtops.urls")),
    path("formationpressure", include ("formationpressure.urls")),
    path("gasshows", include ("gasshows.urls")),
    path("oilshows", include ("oilshows.urls")),
    path("testresults", include ("testresults.urls")),


    # Geophysics
    path("recordedlogs", include ("recordedlogs.urls")),
    path("loganalysis", include ("loganalysis.urls")),


    # drilling
    path("deviationsurveydata", include("deviationsurveydata.urls")),    
    path("drillingwelldata", include("drillingwelldata.urls")),
    path("casings", include("casings.urls")),
    path("cementbondlogs", include("cementbondlogs.urls")),
    path("leakoffTests", include("leakoffTests.urls")),
    path("leakoffTestData", include("leakoffTestData.urls")),
    path("wellhead", include ("wellhead.urls")),
    path("wellcompletion", include ("wellcompletion.urls")),
    path("fish", include ("fish.urls")),
    path("cementplugs", include ("cementplugs.urls")),
    path("drillingsummary", include ("drillingsummary.urls")),
    path("drillingoperations", include ("drillingoperations.urls")),
    path("drillingproblems", include ("drillingproblems.urls")),
    path("drillingplanvsactual", include ("drillingplanvsactual.urls")),
    path("perforations", include ("perforations.urls")),
    path("bridgeplugs", include ("bridgeplugs.urls")),
    
    
    # Reservoir models
    path("opreservoirpressure", include("opreservoirpressure.urls")),
    path("respresestimation", include ("respresestimation.urls")),
    path("opinflow", include("opinflow.urls")),
    path("opgradientsurveys", include("opgradientsurveys.urls")),
    path("opgradientsurveydata", include("opgradientsurveydata.urls")),
    path("pressurebuildupanalysis", include("pressurebuildupanalysis.urls")),
    path("drawdowntestanalysis", include ("drawdowntestanalysis.urls")),
    path("constantratedrawdowntestanalysis", include ("constantratedrawdowntestanalysis.urls")),
    path("multiratedrawdowntestanalysis", include ("multiratedrawdowntestanalysis.urls")),
    path("constantpressuredrawdowntestanalysis", include ("constantpressuredrawdowntestanalysis.urls")),
    path("builduptestdesign", include ("builduptestdesign.urls")),
    path("pressuredropcalculation", include ("pressuredropcalculation.urls")),


    # Production
    path("flowtest", include ("flowtest.urls")),
    path("gaslift", include ("gaslift.urls")),
    path("espdesign", include ("espdesign.urls")),
    path("jetpumpdesign", include ("jetpumpdesign.urls")),
    path("srpdesign", include ("srpdesign.urls")),

    #Interventions

    path("rigworkover", include("rigworkover.urls")),
    path("rigworkoveroperations", include("rigworkoveroperations.urls")),
    path("coiltubing", include("coiltubing.urls")),
    path("coiltubingoperations", include("coiltubingoperations.urls")),
    path("rigless", include("rigless.urls")),
    path("riglessoperations", include ("riglessoperations.urls")),
    path("stimulation", include("stimulation.urls", namespace='stimulation')),  
    path("stimulationoperations", include("stimulationoperations.urls", namespace='stimulationoperations')),   
    path("wireline", include("wireline.urls")),
    path("wirelineoperations", include("wirelineoperations.urls")),
    path("slickline", include("slickline.urls")),    
    path("slicklineoperations", include ("slicklineoperations.urls")),


    # GAS PRODUCERS

    # common
    path("gasproducers", include("gasproducers.urls")),
    path("selectedGasProducer", include("selectedGasProducer.urls")),
    path("gpwellobjectives", include("gpwellobjectives.urls")),
    path("gpwellobjectivedata", include("gpwellobjectivedata.urls")),

    # Geology
    path("gpcuttingdescription", include ("gpcuttingdescription.urls")),
    path("gpformationtops", include ("gpformationtops.urls")),
    path("gpformationpressure", include ("gpformationpressure.urls")),
    path("gpgasshows", include ("gpgasshows.urls")),
    path("gpoilshows", include ("gpoilshows.urls")),
    path("gptestresults", include ("gptestresults.urls")),

    path("gprecordedlogs", include ("gprecordedlogs.urls")),
    path("gploganalysis", include ("gploganalysis.urls")),

    #Gas Producer drilling

    path("gpdeviationsurveydata", include("gpdeviationsurveydata.urls")),    
    path("gpdrillingwelldata", include("gpdrillingwelldata.urls")),
    path("gpcasings", include("gpcasings.urls")),
    path("gpcementbondlogs", include("gpcementbondlogs.urls")),
    path("gpleakoffTests", include("gpleakoffTests.urls")),
    path("gpleakoffTestData", include("gpleakoffTestData.urls")),
    path("gpwellhead", include ("gpwellhead.urls")),
    path("gpwellcompletion", include ("gpwellcompletion.urls")),
    path("gpfish", include ("gpfish.urls")),
    path("gpcementplugs", include ("gpcementplugs.urls")),
    path("gpdrillingsummaary", include ("gpdrillingsummaary.urls")),
    path("gpdrillingoperations", include ("gpdrillingoperations.urls")),
    path("gpdrillingproblems", include ("gpdrillingproblems.urls")),
    path("gpdrillingplanvsactual", include ("gpdrillingplanvsactual.urls")),
    path("gpperforations", include ("gpperforations.urls")),
    path("gpbridgeplugs", include ("gpbridgeplugs.urls")),

    # Reservoir models
    path("gpreservoirpressure", include("gpreservoirpressure.urls")),
    path("gprespresestimation", include ("gprespresestimation.urls")),
    path("gpinflow", include("gpinflow.urls")),
    path("gpgradientsurveys", include("gpgradientsurveys.urls")),
    path("gpgradientsurveydata", include("gpgradientsurveydata.urls")),
    path("gppressurebuildupanalysis", include("gppressurebuildupanalysis.urls")),
    path("gpdrawdowntestanalysis", include ("gpdrawdowntestanalysis.urls")),
    path("gpconstantratedrawdowntestanalysis", include ("gpconstantratedrawdowntestanalysis.urls")),
    path("gpmultiratedrawdowntestanalysis", include ("gpmultiratedrawdowntestanalysis.urls")),
    path("gpconstantpressuredrawdowntestanalysis", include ("gpconstantpressuredrawdowntestanalysis.urls")),
    path("gpbuilduptestdesign", include ("gpbuilduptestdesign.urls")),
    path("gppressuredropcalculation", include ("gppressuredropcalculation.urls")),

    #Interventions

    path("gprigworkover1", include("gprigworkover1.urls")),
    path("gprigworkover1operations", include("gprigworkover1operations.urls")),
    path("gpcoiltubing", include("gpcoiltubing.urls")),
    path("gpcoiltubingoperations", include("gpcoiltubingoperations.urls")),
    path("gprigless", include("gprigless.urls")),
    path("gpriglessoperations", include ("gpriglessoperations.urls")),
    path("gpstimulation", include("gpstimulation.urls", namespace='gpstimulation')),  
    path("gpstimulationoperations", include("gpstimulationoperations.urls", namespace='gpstimulationoperations')),   
    path("gpwireline", include("gpwireline.urls")),
    path("gpwirelineoperations", include("gpwirelineoperations.urls")),
    path("gpslickline", include("gpslickline.urls")),    
    path("gpslicklineoperations", include ("gpslicklineoperations.urls")),


    # WATER INJECTORS
    path("waterinjectors", include("waterinjectors.urls")),
    path("selectedWaterInjector", include("selectedWaterInjector.urls")),
    path("wiwellobjectives", include("wiwellobjectives.urls")),
    path("wiwellobjectivedata", include("wiwellobjectivedata.urls")),

    #Water Injector drilling

    path("wideviationsurveydata", include("wideviationsurveydata.urls")),    
    path("widrillingwelldata", include("widrillingwelldata.urls")),
    path("wicasings", include("wicasings.urls")),
    path("wicementbondlogs", include("wicementbondlogs.urls")),
    path("wileakoffTests", include("wileakoffTests.urls")),
    path("wileakoffTestData", include("wileakoffTestData.urls")),
    path("wiwellhead", include ("wiwellhead.urls")),
    path("wiwellcompletion", include ("wiwellcompletion.urls")),
    path("wifish", include ("wifish.urls")),
    path("wicementplugs", include ("wicementplugs.urls")),
    path("widrillingsummary", include ("widrillingsummary.urls")),
    path("widrillingoperations", include ("widrillingoperations.urls")),
    path("widrillingproblems", include ("widrillingproblems.urls")),
    path("widrillingplanvsactual", include ("widrillingplanvsactual.urls")),
    path("wiperforations", include ("wiperforations.urls")),
    path("wibridgeplugs", include ("wibridgeplugs.urls")),

    # Geology
    path("wicuttingdescription", include ("wicuttingdescription.urls")),
    path("wiformationtops", include ("wiformationtops.urls")),
    path("wiformationpressure", include ("wiformationpressure.urls")),
    path("wigasshows", include ("wigasshows.urls")),
    path("wioilshows", include ("wioilshows.urls")),
    path("witestresults", include ("witestresults.urls")),

    #petrophysics
    path("wirecordedlogs", include ("wirecordedlogs.urls")),
    path("wiloganalysis", include ("wiloganalysis.urls")),

    # Reservoir models
    path("wireservoirpressure", include("wireservoirpressure.urls")),
    path("wirespresestimation", include ("wirespresestimation.urls")),
    path("wiinflow", include("wiinflow.urls")),
    path("wigradientsurveys", include("wigradientsurveys.urls")),
    #path("opgradientsurveydata", include("opgradientsurveydata.urls")),
    #path("pressurebuildupanalysis", include("pressurebuildupanalysis.urls")),
    #path("drawdowntestanalysis", include ("drawdowntestanalysis.urls")),
    #path("constantratedrawdowntestanalysis", include ("constantratedrawdowntestanalysis.urls")),
    #path("multiratedrawdowntestanalysis", include ("multiratedrawdowntestanalysis.urls")),
    #path("constantpressuredrawdowntestanalysis", include ("constantpressuredrawdowntestanalysis.urls")),
    #path("builduptestdesign", include ("builduptestdesign.urls")),
    #path("pressuredropcalculation", include ("pressuredropcalculation.urls")),


    #Interventions

    path("wirigworkover", include("wirigworkover.urls")),
    path("wirigworkoveroperations", include("wirigworkoveroperations.urls")),
    path("wicoiltubing", include("wicoiltubing.urls")),
    path("wicoiltubingoperations", include("wicoiltubingoperations.urls")),
    path("wirigless", include("wirigless.urls")),
    path("wiriglessoperations", include ("wiriglessoperations.urls")),
    path("wistimulation", include("wistimulation.urls", namespace='wistimulation')),  
    path("wistimulationoperations", include("wistimulationoperations.urls", namespace='wistimulationoperations')),   
    path("wiwireline", include("wiwireline.urls")),
    path("wiwirelineoperations", include("wiwirelineoperations.urls")),
    path("wislickline", include("wislickline.urls")),    
    path("wislicklineoperations", include ("wislicklineoperations.urls")),


    # GAS INJECTORS
    path("gasinjectors", include("gasinjectors.urls")),
    path("selectedGasInjector", include("selectedGasInjector.urls")),
    path("giwellobjectives", include("giwellobjectives.urls")),
    path("giwellobjectivedata", include("giwellobjectivedata.urls")),

    # Gas Injector Drilling
    path("gideviationsurveydata", include("gideviationsurveydata.urls")),    
    path("gidrillingwelldata", include("gidrillingwelldata.urls")),
    path("gicasings", include("gicasings.urls")),
    path("gicementbondlogs", include("gicementbondlogs.urls")),
    path("gileakoffTests", include("gileakoffTests.urls")),
    path("gileakoffTestData", include("gileakoffTestData.urls")),
    path("giwellhead", include ("giwellhead.urls")),
    path("giwellcompletion", include ("giwellcompletion.urls")),
    path("gifish", include ("gifish.urls")),
    path("gicementplugs", include ("gicementplugs.urls")),
    path("gidrillingsummary", include ("gidrillingsummary.urls")),
    path("gidrillingoperations", include ("gidrillingoperations.urls")),
    path("gidrillingproblems", include ("gidrillingproblems.urls")),
    path("gidrillingplanvsactual", include ("gidrillingplanvsactual.urls")),
    path("giperforations", include ("giperforations.urls")),
    path("gibridgeplugs", include ("gibridgeplugs.urls")),

    # Geology
    path("gicuttingdescription", include ("gicuttingdescription.urls")),
    path("giformationtops", include ("giformationtops.urls")),
    path("giformationpressure", include ("giformationpressure.urls")),
    path("gigasshows", include ("gigasshows.urls")),
    path("gioilshows", include ("gioilshows.urls")),
    path("gitestresults", include ("gitestresults.urls")),

    # Petrophysics

    path("girecordedlogs", include ("girecordedlogs.urls")),
    path("giloganalysis", include ("giloganalysis.urls")),

    # Reservoir models
    path("gireservoirpressure", include("gireservoirpressure.urls")),
    path("girespresestimation", include ("girespresestimation.urls")),
    path("giinflow", include("giinflow.urls")),
    path("gigradientsurveys", include("gigradientsurveys.urls")),
    #path("opgradientsurveydata", include("opgradientsurveydata.urls")),
    #path("pressurebuildupanalysis", include("pressurebuildupanalysis.urls")),
    #path("drawdowntestanalysis", include ("drawdowntestanalysis.urls")),
    #path("constantratedrawdowntestanalysis", include ("constantratedrawdowntestanalysis.urls")),
    #path("multiratedrawdowntestanalysis", include ("multiratedrawdowntestanalysis.urls")),
    #path("constantpressuredrawdowntestanalysis", include ("constantpressuredrawdowntestanalysis.urls")),
    #path("builduptestdesign", include ("builduptestdesign.urls")),
    #path("pressuredropcalculation", include ("pressuredropcalculation.urls")),

    # Interventions

    path("girigworkover", include("girigworkover.urls")),
    path("girigworkoveroperations", include("girigworkoveroperations.urls")),
    path("gicoiltubing", include("gicoiltubing.urls")),
    path("gicoiltubingoperations", include("gicoiltubingoperations.urls")),
    path("girigless", include("girigless.urls")),
    path("giriglessoperations", include ("giriglessoperations.urls")),
    path("gistimulation", include("gistimulation.urls", namespace='gistimulation')),  
    path("gistimulationoperations", include("gistimulationoperations.urls", namespace='gistimulationoperations')),   
    path("giwireline", include("giwireline.urls")),
    path("giwirelineoperations", include("giwirelineoperations.urls")),
    path("gislickline", include("gislickline.urls")),    
    path("gislicklineoperations", include ("gislicklineoperations.urls")),


    # OBSERVERS
    path("observers", include("observers.urls")),
    path("selectedObserver", include("selectedObserver.urls")),
    path("obwellobjectives", include("obwellobjectives.urls")),
    path("obwellobjectivedata", include("obwellobjectivedata.urls")),

    # Observer Drilling
    path("obdeviationsurveydata", include("obdeviationsurveydata.urls")),    
    path("obdrillingwelldata", include("obdrillingwelldata.urls")),
    path("obcasings", include("obcasings.urls")),
    path("obcementbondlogs", include("obcementbondlogs.urls")),
    path("obleakoffTests", include("obleakoffTests.urls")),
    path("obleakoffTestData", include("obleakoffTestData.urls")),
    path("obwellhead", include ("obwellhead.urls")),
    path("obwellcompletion", include ("obwellcompletion.urls")),
    path("obfish", include ("obfish.urls")),
    path("obcementplugs", include ("obcementplugs.urls")),
    path("obdrillingsummary", include ("obdrillingsummary.urls")),
    path("obdrillingoperations", include ("obdrillingoperations.urls")),
    path("obdrillingproblems", include ("obdrillingproblems.urls")),
    path("obdrillingplanvsactual", include ("obdrillingplanvsactual.urls")),
    path("obperforations", include ("obperforations.urls")),
    path("obbridgeplugs", include ("obbridgeplugs.urls")),

        # Geology
    path("obcuttingdescription", include ("obcuttingdescription.urls")),
    path("obformationtops", include ("obformationtops.urls")),
    path("obformationpressure", include ("obformationpressure.urls")),
    path("obgasshows", include ("obgasshows.urls")),
    path("oboilshows", include ("oboilshows.urls")),
    path("obtestresults", include ("obtestresults.urls")),

    #petrophysics/geophysics models

    path("obrecordedlogs", include ("obrecordedlogs.urls")),
    path("obloganalysis", include ("obloganalysis.urls")),

    # Reservoir models
    path("obreservoirpressure", include("obreservoirpressure.urls")),
    path("obrespresestimation", include ("obrespresestimation.urls")),
    path("obinflow", include("obinflow.urls")),
    path("obgradientsurveys", include("obgradientsurveys.urls")),
    #path("opgradientsurveydata", include("opgradientsurveydata.urls")),
    #path("pressurebuildupanalysis", include("pressurebuildupanalysis.urls")),
    #path("drawdowntestanalysis", include ("drawdowntestanalysis.urls")),
    #path("constantratedrawdowntestanalysis", include ("constantratedrawdowntestanalysis.urls")),
    #path("multiratedrawdowntestanalysis", include ("multiratedrawdowntestanalysis.urls")),
    #path("constantpressuredrawdowntestanalysis", include ("constantpressuredrawdowntestanalysis.urls")),
    #path("builduptestdesign", include ("builduptestdesign.urls")),
    #path("pressuredropcalculation", include ("pressuredropcalculation.urls")),

    # Interventions
    path("obrigworkover", include("obrigworkover.urls")),
    path("obrigworkoveroperations", include("obrigworkoveroperations.urls")),
    path("obcoiltubing", include("obcoiltubing.urls")),
    path("obcoiltubingoperations", include("obcoiltubingoperations.urls")),
    path("obrigless", include("obrigless.urls")),
    path("obriglessoperations", include ("obriglessoperations.urls")),
    path("obstimulation", include("obstimulation.urls", namespace='obstimulation')),  
    path("obstimulationoperations", include("obstimulationoperations.urls", namespace='obstimulationoperations')),   
    path("obwireline", include("obwireline.urls")),
    path("obwirelineoperations", include("obwirelineoperations.urls")),
    path("obslickline", include("obslickline.urls")),    
    path("obslicklineoperations", include ("obslicklineoperations.urls")),



]
