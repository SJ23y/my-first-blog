from django.conf.urls import url
from .  import views

urlpatterns = [
	url(r'^img/$', views.show_image, name='show_image'),
    url(r'^$', views.homepage, name='homepage'),
    ]
    
