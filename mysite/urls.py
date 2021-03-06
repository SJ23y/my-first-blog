from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls.static import static
from django.contrib.staticfiles import views as dj_views 
from . import settings

admin.autodiscover()
urlpatterns = [
    url(r'', include('HomePage.urls')),
    url(r'^blog', include('blog.urls')),
    url(r'^qa', include('qa.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/blog'}),]
    


if settings.DEBUG:
	urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)