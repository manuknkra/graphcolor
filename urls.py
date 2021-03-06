from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from graph_color.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	(r'^map_color/$',map_color),
	(r'^solve/$',solve),

	(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':'/home/manu/Django/django-projects/mysite/media' }),


    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
)
