from django.conf.urls import url
from . import views

urlpatterns = [
	# ex: /spots/
	url(r'^$', views.index, name='index'),
	# /spots/results/
	url(r'^results/$', views.results, name='results'),
	# ex: /spots/book/5/
	url(r'^book/(?P<pk>[0-9]+)', views.InstanceView.as_view(), name='instance'),
]