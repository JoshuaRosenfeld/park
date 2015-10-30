from django.conf.urls import url
from . import views

urlpatterns = [
	# ex: /spots/
	url(r'^$', views.index, name='index'),
	# ex: /spots/5
	url(r'^(?P<spot_id>[0-9]+)/$', views.spot, name='spot'),
]