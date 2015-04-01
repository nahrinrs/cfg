from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'configServices.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', 'configServices.views.login'),
    url(r'^logout', 'configServices.views.logout'),
    url(r'^auth', 'configServices.views.auth_view'),
    url(r'^config/$', 'config.views.index'),
    url(r'^config/update/', 'config.views.update'),
    url(r'^config/delete/', 'config.views.delete'),
    url(r'^config/lock/', 'config.views.lock'),
    url(r'^config/copy/', 'config.views.copy'),
    url(r'^api/', include('api.urls')),
)
