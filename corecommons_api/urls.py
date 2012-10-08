from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from core.views import IndexView
from core.api import StandardResource, ComponentResource, GradeLevelResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(StandardResource())
v1_api.register(ComponentResource())
v1_api.register(GradeLevelResource())

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
