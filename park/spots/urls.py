from django.conf.urls import url
from . import views

urlpatterns = [
	# /spots/
	url(r'^$', views.index, name='index'),
	# /spots/s/
	url(r'^s/$', views.indexSearch, name='index-search'),
	# /spots/results/
	url(r'^results/$', views.results, name='results'),
	# ex: /spots/book/5/
	url(r'^book/(?P<instance_id>[0-9]+)', views.instance, name='instance'),
	# /success/
	url(r'^success/$', views.success, name='success'),
	# /error/
	url(r'^error/$', views.error, name='error'),
	# /register/
	url(r'^register/$', views.register, name='register'),
]