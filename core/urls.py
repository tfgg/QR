from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
    url(r'^polls/(?P<id>\d)$', views.poll, name="poll"),
    url(r'^polls/(?P<id>\d)/print$', views.poll_print, name="poll_print"),
    url(r'^polls/(?P<poll_id>\d)/(?P<option_id>\d)$', views.poll_vote, name="poll_vote"),
    
    url(r'^c/(?P<campaign_id>\d)$', views.campaign, name="campaign"),
    url(r'^c/(?P<campaign_id>\d)/poster$', views.campaign_poster, name="poster"),
    url(r'^c/(?P<campaign_id>\d)/stickers$', views.campaign_stickers, name="stickers"),
)

