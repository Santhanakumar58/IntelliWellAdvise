"""
Django settings for IntelligentOilWell project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intelligentOilWell.settings')
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*1g_sn-voh%7ne9$+3%*dm=llk_b)^u-@t)3l0$7e3zfg4lb!n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "Home.apps.HomeConfig", 
    "import_export",
    # Fieldwide Applications
    'assets.apps.AssetsConfig',
    'blocks.apps.BlocksConfig',
    'oilfields.apps.OilfieldsConfig',
    'layers.apps.LayersConfig',
    'sublayers.apps.SublayersConfig',
    "fgis.apps.FgisConfig",
    'selectedfgi.apps.SelectedfgiConfig',
    'oilproducers.apps.OilproducersConfig',
    'selectedOilProducer.apps.SelectedOilProducerConfig',
    'blackoilpvt.apps.BlackoilpvtConfig',
    "reservoirfluidcomposition.apps.ReservoirfluidcompositionConfig",
    "reservoirfluidcompositiondata.apps.ReservoirfluidcompositiondataConfig",
    "constantcompositionexpansion.apps.ConstantcompositionexpansionConfig",
    "constantcompositionexpansiondata.apps.ConstantcompositionexpansiondataConfig",
    "differentialliberation.apps.DifferentialliberationConfig",
    "differentialliberationdata.apps.DifferentialliberationdataConfig",
    'opwellobjectives.apps.OpwellobjectivesConfig',
    'opwellobjectivedata.apps.OpwellobjectivedataConfig',
    'wateranalysis.apps.WateranalysisConfig',
     
    #----------------------------------------------------------------------------------------------------------------------------------------
    # Oil Producer applications
    #---------------------------------------------------------------------------------------------------------------------------------------
    
    # Geology 
    'cuttingdescription.apps.CuttingdescriptionConfig', 
    'formationtops.apps.FormationtopsConfig', 
    'formationpressure.apps.FormationpressureConfig', 
    'gasshows.apps.GasshowsConfig', 
    'oilshows.apps.OilshowsConfig', 
    'testresults.apps.TestresultsConfig', 
    
    # Geophysics/Petrophysics
    'recordedlogs.apps.RecordedlogsConfig', 
    'loganalysis.apps.LoganalysisConfig', 



    # Drillig   
    'drillingwelldata.apps.DrillingwelldataConfig',
    'deviationsurveydata.apps.DeviationsurveydataConfig',
    'casings.apps.CasingsConfig',
    'cementbondlogs.apps.CementbondlogsConfig',
    'leakoffTests.apps.LeakofftestsConfig',
    'leakoffTestData.apps.LeakofftestdataConfig',
    'wellcompletion.apps.WellcompletionConfig', 
    'wellhead.apps.WellheadConfig', 
    'fish.apps.FishConfig', 
    'cementplugs.apps.CementplugsConfig', 
    'drillingsummary.apps.DrillingsummaryConfig', 
    'drillingoperations.apps.DrillingoperationsConfig', 
    'drillingproblems.apps.DrillingproblemsConfig', 
    'drillingplanvsactual.apps.DrillingplanvsactualConfig', 
    'perforations.apps.PerforationsConfig', 
    'bridgeplugs.apps.BridgeplugsConfig', 
    'tubings.apps.TubingsConfig', 


    # Reservoir
    'opreservoirpressure.apps.OpreservoirpressureConfig',
    'respresestimation.apps.RespresestimationConfig', 
    'opinflow.apps.OpinflowConfig',
    'opgradientsurveys.apps.OpgradientsurveysConfig',
    'opgradientsurveydata.apps.OpgradientsurveydataConfig',
    'pressurebuildupanalysis.apps.PressurebuildupanalysisConfig',
    'drawdowntestanalysis.apps.DrawdowntestanalysisConfig', 
    'constantratedrawdowntestanalysis.apps.ConstantratedrawdowntestanalysisConfig', 
    'constantpressuredrawdowntestanalysis.apps.ConstantpressuredrawdowntestanalysisConfig', 
    'multiratedrawdowntestanalysis.apps.MultiratedrawdowntestanalysisConfig', 
    'builduptestdesign.apps.BuilduptestdesignConfig', 
    'pressuredropcalculation.apps.PressuredropcalculationConfig', 

    # Production
    'flowtest.apps.FlowtestConfig',
    'gaslift.apps.GasliftConfig',
    'espdesign.apps.EspdesignConfig',
    'jetpumpdesign.apps.JetpumpdesignConfig',
    'srpdesign.apps.SrpdesignConfig',

    # Interventions
    'rigworkover.apps.RigworkoverConfig',
    'rigworkoveroperations.apps.RigworkoveroperationsConfig',
    'coiltubing.apps.CoiltubingConfig', 
    'coiltubingoperations.apps.CoiltubingoperationsConfig',
    'rigless.apps.RiglessConfig',
    'riglessoperations.apps.RiglessoperationsConfig',
    'stimulation.apps.StimulationConfig',
    'stimulationoperations.apps.StimulationoperationsConfig',
    'wireline.apps.WirelineConfig',
    'wirelineoperations.apps.WirelineoperationsConfig',
    'slickline.apps.SlicklineConfig',   
    'slicklineoperations.apps.SlicklineoperationsConfig',  

    #----------------------------------------------------------------------------------------------------
    # Gas Producer Applications
    #-------------------------------------------------------------------------------------------------------------------
    # Common Gas Producer
    'gasproducers.apps.GasproducersConfig',
    'selectedGasProducer.apps.SelectedgasproducerConfig',
    'gpwellobjectives.apps.GpwellobjectivesConfig',
    'gpwellobjectivedata.apps.GpwellobjectivedataConfig',

    
    # Geology Gas Producer 
    'gpcuttingdescription.apps.GpcuttingdescriptionConfig', 
    'gpformationtops.apps.GpformationtopsConfig', 
    'gpformationpressure.apps.GpformationpressureConfig', 
    'gpgasshows.apps.GpgasshowsConfig', 
    'gpoilshows.apps.GpoilshowsConfig', 
    'gptestresults.apps.GptestresultsConfig',

    # Geophysics/Petrophysics
    'gprecordedlogs.apps.GprecordedlogsConfig', 
    'gploganalysis.apps.GploganalysisConfig', 
    
    # Drilling Gas Producer
    'gpdrillingwelldata.apps.GpdrillingwelldataConfig',
    'gpdeviationsurveydata.apps.GpdeviationsurveydataConfig',
    'gpcasings.apps.GpcasingsConfig',
    'gpcementbondlogs.apps.GpcementbondlogsConfig',
    'gpleakoffTests.apps.GpleakofftestsConfig',
    'gpleakoffTestData.apps.GpleakofftestdataConfig',
    'gpwellcompletion.apps.GpwellcompletionConfig', 
    'gpwellhead.apps.GpwellheadConfig', 
    'gpfish.apps.GpfishConfig', 
    'gpcementplugs.apps.GpcementplugsConfig', 
    'gpdrillingsummaary.apps.GpdrillingsummaaryConfig', 
    'gpdrillingoperations.apps.GpdrillingoperationsConfig', 
    'gpdrillingproblems.apps.GpdrillingproblemsConfig', 
    'gpdrillingplanvsactual.apps.GpdrillingplanvsactualConfig', 
    'gpperforations.apps.GpperforationsConfig', 
    'gpbridgeplugs.apps.GpbridgeplugsConfig', 

    # Reservoir gas Producer
    'gpreservoirpressure.apps.GpreservoirpressureConfig',
    'gprespresestimation.apps.GprespresestimationConfig', 
    'gpinflow.apps.GpinflowConfig',
    'gpgradientsurveys.apps.GpgradientsurveysConfig',
    'gpgradientsurveydata.apps.GpgradientsurveydataConfig',
    'gppressurebuildupanalysis.apps.GppressurebuildupanalysisConfig',
    'gpdrawdowntestanalysis.apps.GpdrawdowntestanalysisConfig', 
    'gpconstantratedrawdowntestanalysis.apps.GpconstantratedrawdowntestanalysisConfig', 
    'gpconstantpressuredrawdowntestanalysis.apps.GpconstantpressuredrawdowntestanalysisConfig', 
    'gpmultiratedrawdowntestanalysis.apps.GpmultiratedrawdowntestanalysisConfig', 
    'gpbuilduptestdesign.apps.GpbuilduptestdesignConfig', 
    'gppressuredropcalculation.apps.GppressuredropcalculationConfig', 

    # Interventions
    'gprigworkover1.apps.Gprigworkover1Config',
    'gprigworkover1operations.apps.Gprigworkover1operationsConfig',
    'gpcoiltubing.apps.GpcoiltubingConfig', 
    'gpcoiltubingoperations.apps.GpcoiltubingoperationsConfig',
    'gprigless.apps.GpriglessConfig',
    'gpriglessoperations.apps.GpriglessoperationsConfig',
    'gpstimulation.apps.GpstimulationConfig',
    'gpstimulationoperations.apps.GpstimulationoperationsConfig',
    'gpwireline.apps.GpwirelineConfig',
    'gpwirelineoperations.apps.GpwirelineoperationsConfig',
    'gpslickline.apps.GpslicklineConfig',   
    'gpslicklineoperations.apps.GpslicklineoperationsConfig',  

    #---------------------------------------------------------------------------------------------------------------------------
    # WATER INJECTORS
    #---------------------------------------------------------------------------------------------------------------------------

    # Common Water Injector
    'waterinjectors.apps.WaterinjectorsConfig',
    'selectedWaterInjector.apps.SelectedwaterinjectorConfig',
    'wiwellobjectives.apps.WiwellobjectivesConfig',
    'wiwellobjectivedata.apps.WiwellobjectivedataConfig',

    # Geology water injector 
    'wicuttingdescription.apps.WicuttingdescriptionConfig', 
    'wiformationtops.apps.WiformationtopsConfig', 
    'wiformationpressure.apps.WiformationpressureConfig', 
    'wigasshows.apps.WigasshowsConfig', 
    'wioilshows.apps.WioilshowsConfig', 
    'witestresults.apps.WitestresultsConfig',

    # Geophysics/Petrophysics
    'wirecordedlogs.apps.WirecordedlogsConfig', 
    'wiloganalysis.apps.WiloganalysisConfig', 

    # drilling applications
    'widrillingwelldata.apps.WidrillingwelldataConfig',
    'wideviationsurveydata.apps.WideviationsurveydataConfig',
    'wicasings.apps.WicasingsConfig',
    'wicementbondlogs.apps.WicementbondlogsConfig',
    'wileakoffTests.apps.WileakofftestsConfig',
    'wileakoffTestData.apps.WileakofftestdataConfig',
    'wiwellcompletion.apps.WiwellcompletionConfig', 
    'wiwellhead.apps.WiwellheadConfig', 
    'wifish.apps.WifishConfig', 
    'wicementplugs.apps.WicementplugsConfig', 
    'widrillingsummary.apps.WidrillingsummaryConfig', 
    'widrillingoperations.apps.WidrillingoperationsConfig', 
    'widrillingproblems.apps.WidrillingproblemsConfig', 
    'widrillingplanvsactual.apps.WidrillingplanvsactualConfig', 
    'wiperforations.apps.WiperforationsConfig', 
    'wibridgeplugs.apps.WibridgeplugsConfig', 

    # Reservoir Water Injector
    'wireservoirpressure.apps.WireservoirpressureConfig',
    'wirespresestimation.apps.WirespresestimationConfig', 
    'wiinflow.apps.WiinflowConfig',
    'wigradientsurveys.apps.WigradientsurveysConfig',
    'wigradientsurveydata.apps.WigradientsurveydataConfig',
    #'wipressurebuildupanalysis.apps.WipressurebuildupanalysisConfig',
    #'widrawdowntestanalysis.apps.WidrawdowntestanalysisConfig', 
    #'wiconstantratedrawdowntestanalysis.apps.WiconstantratedrawdowntestanalysisConfig', 
    #'wiconstantpressuredrawdowntestanalysis.apps.WiconstantpressuredrawdowntestanalysisConfig', 
    #'wimultiratedrawdowntestanalysis.apps.WimultiratedrawdowntestanalysisConfig', 
    #'wibuilduptestdesign.apps.WibuilduptestdesignConfig', 
    #'wipressuredropcalculation.apps.WipressuredropcalculationConfig', 

    # Interventions
    'wirigworkover.apps.WirigworkoverConfig',
    'wirigworkoveroperations.apps.WirigworkoveroperationsConfig',
    'wicoiltubing.apps.WicoiltubingConfig', 
    'wicoiltubingoperations.apps.WicoiltubingoperationsConfig',
    'wirigless.apps.WiriglessConfig',
    'wiriglessoperations.apps.WiriglessoperationsConfig',
    'wistimulation.apps.WistimulationConfig',
    'wistimulationoperations.apps.WistimulationoperationsConfig',
    'wiwireline.apps.WiwirelineConfig',
    'wiwirelineoperations.apps.WiwirelineoperationsConfig',
    'wislickline.apps.WislicklineConfig',   
    'wislicklineoperations.apps.WislicklineoperationsConfig',  

    # ----------------------------------------------------------------------------------------------------------------
    # GAS INJECTORS
    # ----------------------------------------------------------------------------------------------------------------
    'gasinjectors.apps.GasinjectorsConfig',
    'selectedGasInjector.apps.SelectedgasinjectorConfig',
    'giwellobjectives.apps.GiwellobjectivesConfig',
    'giwellobjectivedata.apps.GiwellobjectivedataConfig',

    # Geology Gas injector 
    'gicuttingdescription.apps.GicuttingdescriptionConfig', 
    'giformationtops.apps.GiformationtopsConfig', 
    'giformationpressure.apps.GiformationpressureConfig', 
    'gigasshows.apps.GigasshowsConfig', 
    'gioilshows.apps.GioilshowsConfig', 
    'gitestresults.apps.GitestresultsConfig',

    # Geophysics/Petrophysics
    'girecordedlogs.apps.GirecordedlogsConfig', 
    'giloganalysis.apps.GiloganalysisConfig', 

    # Drilling applications 
    'gidrillingwelldata.apps.GidrillingwelldataConfig',
    'gideviationsurveydata.apps.GideviationsurveydataConfig',
    'gicasings.apps.GicasingsConfig',
    'gicementbondlogs.apps.GicementbondlogsConfig',
    'gileakoffTests.apps.GileakofftestsConfig',
    'gileakoffTestData.apps.GileakofftestdataConfig',
    'giwellcompletion.apps.GiwellcompletionConfig', 
    'giwellhead.apps.GiwellheadConfig', 
    'gifish.apps.GifishConfig', 
    'gicementplugs.apps.GicementplugsConfig', 
    'gidrillingsummary.apps.GidrillingsummaryConfig', 
    'gidrillingoperations.apps.GidrillingoperationsConfig', 
    'gidrillingproblems.apps.GidrillingproblemsConfig', 
    'gidrillingplanvsactual.apps.GidrillingplanvsactualConfig', 
    'giperforations.apps.GiperforationsConfig', 
    'gibridgeplugs.apps.GibridgeplugsConfig', 

    # Reservoir gas Injector
    'gireservoirpressure.apps.GireservoirpressureConfig',
    'girespresestimation.apps.GirespresestimationConfig', 
    'giinflow.apps.GiinflowConfig',
    'gigradientsurveys.apps.GigradientsurveysConfig',
    'gigradientsurveydata.apps.GigradientsurveydataConfig',
    #'gipressurebuildupanalysis.apps.GipressurebuildupanalysisConfig',
    #'gidrawdowntestanalysis.apps.GidrawdowntestanalysisConfig', 
    #'giconstantratedrawdowntestanalysis.apps.GiconstantratedrawdowntestanalysisConfig', 
    #'giconstantpressuredrawdowntestanalysis.apps.GiconstantpressuredrawdowntestanalysisConfig', 
    #'gimultiratedrawdowntestanalysis.apps.GimultiratedrawdowntestanalysisConfig', 
    #'gibuilduptestdesign.apps.GibuilduptestdesignConfig', 
    #'gipressuredropcalculation.apps.GipressuredropcalculationConfig', 

    # Interventions
    'girigworkover.apps.GirigworkoverConfig',
    'girigworkoveroperations.apps.GirigworkoveroperationsConfig',
    'gicoiltubing.apps.GicoiltubingConfig', 
    'gicoiltubingoperations.apps.GicoiltubingoperationsConfig',
    'girigless.apps.GiriglessConfig',
    'giriglessoperations.apps.GiriglessoperationsConfig',
    'gistimulation.apps.GistimulationConfig',
    'gistimulationoperations.apps.GistimulationoperationsConfig',
    'giwireline.apps.GiwirelineConfig',
    'giwirelineoperations.apps.GiwirelineoperationsConfig',
    'gislickline.apps.GislicklineConfig',   
    'gislicklineoperations.apps.GislicklineoperationsConfig',  


    # OBSERVERS

    # Observer Common
    'observers.apps.ObserversConfig',
    'selectedObserver.apps.SelectedobserverConfig',
    'obwellobjectives.apps.ObwellobjectivesConfig',
    'obwellobjectivedata.apps.ObwellobjectivedataConfig',

    # Geology Observer
    'obcuttingdescription.apps.ObcuttingdescriptionConfig', 
    'obformationtops.apps.ObformationtopsConfig', 
    'obformationpressure.apps.ObformationpressureConfig', 
    'obgasshows.apps.ObgasshowsConfig', 
    'oboilshows.apps.OboilshowsConfig', 
    'obtestresults.apps.ObtestresultsConfig',

    # Geophysics/Petrophysics
    'obrecordedlogs.apps.ObrecordedlogsConfig', 
    'obloganalysis.apps.ObloganalysisConfig', 

    # Observer Drilling
    'obdrillingwelldata.apps.ObdrillingwelldataConfig',
    'obdeviationsurveydata.apps.ObdeviationsurveydataConfig',
    'obcasings.apps.ObcasingsConfig',
    'obcementbondlogs.apps.ObcementbondlogsConfig',
    'obleakoffTests.apps.ObleakofftestsConfig',
    'obleakoffTestData.apps.ObleakofftestdataConfig',
    'obwellcompletion.apps.ObwellcompletionConfig', 
    'obwellhead.apps.ObwellheadConfig', 
    'obfish.apps.ObfishConfig', 
    'obcementplugs.apps.ObcementplugsConfig', 
    'obdrillingsummary.apps.ObdrillingsummaryConfig', 
    'obdrillingoperations.apps.ObdrillingoperationsConfig', 
    'obdrillingproblems.apps.ObdrillingproblemsConfig', 
    'obdrillingplanvsactual.apps.ObdrillingplanvsactualConfig', 
    'obperforations.apps.ObperforationsConfig', 
    'obbridgeplugs.apps.ObbridgeplugsConfig', 

    # Reservoir Observer
    'obreservoirpressure.apps.ObreservoirpressureConfig',
    'obrespresestimation.apps.ObrespresestimationConfig', 
    'obinflow.apps.ObinflowConfig',
    'obgradientsurveys.apps.ObgradientsurveysConfig',
    'obgradientsurveydata.apps.ObgradientsurveydataConfig',
    #'obpressurebuildupanalysis.apps.ObpressurebuildupanalysisConfig',
    #'obdrawdowntestanalysis.apps.ObdrawdowntestanalysisConfig', 
    #'obconstantratedrawdowntestanalysis.apps.ObconstantratedrawdowntestanalysisConfig', 
    #'obconstantpressuredrawdowntestanalysis.apps.ObconstantpressuredrawdowntestanalysisConfig', 
    #'obmultiratedrawdowntestanalysis.apps.ObmultiratedrawdowntestanalysisConfig', 
    #'obbuilduptestdesign.apps.ObbuilduptestdesignConfig', 
    #'obpressuredropcalculation.apps.ObpressuredropcalculationConfig', 

    # Interventions
    'obrigworkover.apps.ObrigworkoverConfig',
    'obrigworkoveroperations.apps.ObrigworkoveroperationsConfig',
    'obcoiltubing.apps.ObcoiltubingConfig', 
    'obcoiltubingoperations.apps.ObcoiltubingoperationsConfig',
    'obrigless.apps.ObriglessConfig',
    'obriglessoperations.apps.ObriglessoperationsConfig',
    'obstimulation.apps.ObstimulationConfig',
    'obstimulationoperations.apps.ObstimulationoperationsConfig',
    'obwireline.apps.ObwirelineConfig',
    'obwirelineoperations.apps.ObwirelineoperationsConfig',
    'obslickline.apps.ObslicklineConfig',   
    'obslicklineoperations.apps.ObslicklineoperationsConfig',  

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IntelligentOilWell.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'IntelligentOilWell.custom_context_processors.selectedfgi',
                'IntelligentOilWell.custom_context_processors.selectedwell',
                'IntelligentOilWell.custom_context_processors.selectedgpwell',
                'IntelligentOilWell.custom_context_processors.selectedwiwell',  
                'IntelligentOilWell.custom_context_processors.selectedgiwell',
                'IntelligentOilWell.custom_context_processors.selectedobwell',         
            ],
        },
    },
]

WSGI_APPLICATION = 'IntelligentOilWell.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'Home/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'Home/static'),]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

