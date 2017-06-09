from django.conf.urls import url
from . import views
import django.contrib.auth 

urlpatterns = [
    url(r'^$', views.show_popular),
    url(r'^new/$', views.show_new),
    url(r'^question/(?P<pk>[0-9]+)/$', views.show_question),
	url(r'^/login/$', django.contrib.auth.views.login),
	url(r'^logout/$', django.contrib.auth.views.logout),
	url(r'^signup/$', views.ask_question),
	url(r'^/ask/$', views.ask_question),
    ]
    
