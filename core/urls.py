from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^polls/(?P<id>\d)$', views.poll, name="poll"),
    url(r'^polls/(?P<poll_id>\d)/(?P<option_id>\d)$', views.poll_vote, name="poll_vote"),
)

