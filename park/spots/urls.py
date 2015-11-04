from django.conf.urls import url
from . import views

urlpatterns = [
	# ex: /spots/
	url(r'^$', views.index, name='index'),
	# ex: /spots/5
	url(r'^(?P<pk>[0-9]+)/$', views.SpotView.as_view(), name='spot'),
	# /spots/results
	url(r'^results/$', views.results, name='results'),
	# /spots/update
	url(r'^update/$', views.update, name='update'),
]