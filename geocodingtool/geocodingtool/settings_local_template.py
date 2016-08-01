# Django generated secret key
SECRET_KEY = 'rkus!qn2dm2pq!^*sg)g%-olxc7gzd9ugx7_=n+myim1bf2k6='

DEBUG = True
TEMPLATE_DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "database_name",
        'USER': "database_user",
        'PASSWORD': "database_password",
        'HOST': "host", # put "localhost" if running locally
        'PORT': "port" # put "5432" if running on defautl postgresql port       
    }
}

# File path for storage of uploaded address excel/csv file
STORAGE_ROOTPATH = "project_path" + "di_geocoding/geocodingtool/geocodingapp/static/data/"

# Geocoder API Keys
## Google
GOOGLE_API_KEY = "Google API Key"

## OpenStreeMap
OSM_API_KEY = "OSM API Key" # not required

## ArcGIS
ARCGIS_API_KEY = "ArcGIS API Key" # not required

# Bing
BING_API_KEY = "Bing API Key"

# Mapbox
MAPBOX_API_KEY = "Mapbox API Key"

# MapQuest
MAPQUEST_API_KEY = "Mapquest API Key"

# what3words
WHAT3WORDS_API_KEY = "what3words API Key"