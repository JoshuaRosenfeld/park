from django.conf.urls import url
from . import views

urlpatterns = [
	# ex: /spots/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /spots/5
	url(r'^(?P<pk>[0-9]+)/$', views.SpotView.as_view(), name='spot'),
]