from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^app_shop/', include('app_shop.urls', namespace="app_shop")), #added namespaces, info from docs
    url(r'^app_shop', include('app_shop.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
