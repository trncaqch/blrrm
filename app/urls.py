from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	
)

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)