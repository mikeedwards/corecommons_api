from django.conf.urls import patterns, include, url

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'corecommons_api.views.home', name='home'),
    # url(r'^corecommons_api/', include('corecommons_api.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
