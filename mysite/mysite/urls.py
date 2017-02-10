from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views

admin.autodiscover()
urlpatterns = [
    url(r'', include('HomePage.urls')),
    url(r'^blog', include('blog.urls')),
    url(r'^qa', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
]
