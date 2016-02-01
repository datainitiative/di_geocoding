from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.views import logout

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('geocodingapp.views',
	# Home page URL
	url(r'^home/$','home'),
	
	# Function URLs
	url(r'^api/geocoding/$','api_geocoding'),
	url(r'instant_geocoding/','instant_geocoding'),
	url(r'^geocoding/setup$','geocoding_setup'),
	url(r'^geocoding/start$','start_geocoding'),
	url(r'^geocoding/results$','geocoding_result'),
	url(r'^geocoding/download_results/(?P<task_id>\d+)/$','exportcsv_geocodingresults'),
	url(r'^geocoding/get_cf_link$','get_cf_link'),
	url(r'^geocoding/no_cf_link/(?P<task_id>\d+)/$','no_cf_link'),
	
	# Test geocoding URL
	url(r'^geocoding/test$','test_geocoding'),
	
	# URLs for importing geography
	url(r'^import/geo/county/$','import_geo_county'),
	url(r'^import/geo/city/$','import_geo_city'),

#	# Login,Logout,Register,User
#	url(r'^logout/$',logout,{'template_name': 'registration/logged_out.html'}),
#	url(r'^register/$','register'),
#	url(r'^user/profile/$','user_profile'),
#	url(r'^user/password/$','user_change_password'),
)