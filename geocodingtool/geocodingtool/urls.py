from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geocodingtool.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # Geocodingtool App URLs
    url(r'^geocodingtool/',include('geocodingapp.urls')),
    
    # settings_local
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR+'/core/static/', 'show_indexes': True}),  
)
