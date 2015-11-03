from django.conf.urls import url
from . import views

urlpatterns = [
	# ex: /spots/
	url(r'^$', views.index, name='index'),
	# ex: /spots/5
	url(r'^(?P<pk>[0-9]+)/$', views.SpotView.as_view(), name='spot'),
	# ex: /spots/results
	url(r'^results/$', views.results, name='results')
	# (?P<address>[\w]+)/(?P<date>[\w]+)/(?P<time>[\w]+)/$'
]