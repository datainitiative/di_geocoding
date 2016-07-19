"""
Django settings for geocodingtool project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.contrib import messages
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECURET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Template
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Application definition

INSTALLED_APPS = (
    'bootstrap3',
    'django_admin_bootstrapped',
    'smart_selects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'geocodingapp'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'geocodingtool.urls'

WSGI_APPLICATION = 'geocodingtool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DATABASE_NAME',
        'USER': 'DATABASE_USER',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOST',
        'PORT': 'PORT'        
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Template context processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

ROOT_APP_URL = '/geocodingtool' # use this for localhost
#ROOT_APP_URL = '/geocodingtool/geocodingtool' # use this for server

ADMIN_ROOT_URL = '' # use this for localhost
#ADMIN_ROOT_URL = '/geocodingtool' # use this for server

STATIC_ROOT_URL = '/geocodingtool'
STATIC_URL = '%s/static/' % STATIC_ROOT_URL

# use this for localhost
STORAGE_ROOTPATH = 'LOCAL_DATA_DIR'
# use this for server
#STORAGE_ROOTPATH = 'SERVER_DATA_DIR'

# Login URL
LOGIN_URL = '/admin/login/' # use this for localhost
#LOGIN_URL = '/geocodingtool/admin/login/'

# Use Bootstrap3 for Django
## Bootstrap3 config dict
BOOTSTRAP3 = {
    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.3.1/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': False,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-4',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers':{
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}


## Custom rendere for fields using Bootstrap3
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'
### Custom admin messages - Add Bootstrap3 tags for messages (tag:"alert-info")
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'
}

## File Extensions
EXCEL_FILE_EXTENSIONS = [".xlsx",".xlsm",".xltx",".xltm"]
CSV_FILE_EXTENSIONS = [".csv"]

## Community Facts Neighborhood Table
CF_GEOTABLE = {
    'db_table': "neighborhood_metro7county_geographyv3_2010",
    'srid': "2232",
    'col_id': "nhid",
    'col_name': "nhname",
    'cf_url_nbsummary': "http://denvermetrodata.org/neighborhood/"
}

## Geocoder API Keys
# Google: 2500 free requests per day; 10 requests per second.
# g = geocoder.google('address',[key=])
GOOGLE_API_KEY = "GOOGLE_API_KEY"
GOOGLE_API_LIMIT = 2500

# OpenStreeMap: max of 1 request per second. No key needed.
# g = geocoder.osm('address')
OSM_API_KEY = ""

# ArcGIS: Free per one request. Need a key from GISOnline account later.
# g = geocoder.arcgis('address',[key=])
ARCGIS_API_KEY = ""

# Bing: Public website: Max 125000 cumulative billable transactions within any 12-month period at no charge.
# g = geocoder.bing('address',key=)
BING_API_KEY = "BING_API_KEY"

# Mapbox: Free one geocode per request.
# g = geocoder.mapbox('address',key=)
MAPBOX_API_KEY = "MAPBOX_API_KEY"

# MapQuest: 15000 transactions per month. No bounding box, thus no confidence level.
# g = geocoder.mapquest('address',key=)
MAPQUEST_API_KEY = "MAPQUEST_API_KEY"

# what3words API Key for user qliu@garycommunity.org
WHAT3WORDS_API_KEY = "WHAT3WORDS_API_KEY"

# Project ID for one-time (single) geocoding task
# use this for server
#SINGLE_GEOCODINGTASK_ID = 12
# use this for localhost
SINGLE_GEOCODINGTASK_ID = 1

## Limit Max File Upload Size to 5MB = 5242880 bytes
#MAX_UPLOAD_SIZE = 5242880
MAX_UPLOAD_SIZE = 1048576 # 1MB
MAX_GEOCODING_LIMIT = 500