from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', auth_views.login),
	url(r'^accounts/logout/$', auth_views.logout,),
	url(r'^spots/', include('spots.urls', namespace='spots')),
]

