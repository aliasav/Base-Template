from django.conf.urls import patterns, include, url
from Base_Template.views import register, home

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Base_Template.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name = 'home'),
    url(r'^register$', register),
    url(r'^home$', home)
)
