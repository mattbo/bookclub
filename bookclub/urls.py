from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookclub.views.home', name='home'),
    # url(r'^bookclub/', include('bookclub.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    (r'^club/', include('club.urls')),
    (r'^register/$', 'club.views.register'),
    (r'^logout/$', 'club.views.logout'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name':'login.html'}),
)

