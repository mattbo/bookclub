from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'club.views.user_home'),
    (r'^(?P<club>\d)/$', 'club.views.club_home'),
    (r'^(?P<club>\d)/book/$', 'club.views.add_book'),
    (r'^(?P<club>\d)/book/(?P<book>\d)/comment/$', 'club.views.comment'),
)
