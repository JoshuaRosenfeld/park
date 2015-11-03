from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import User, Spot

class IndexView(TemplateView):
	template_name = 'spots/index.html'


class SpotView(generic.DetailView):
	model = Spot

class ResultsView(generic.DetailView):
	template_name = 'spots/spots.html'
	context_object_name = 'spot_list'

	def get_queryset(self):
		""" Return all spots """
		return Spot.objects.all()
