from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import User, Spot

class IndexView(generic.ListView):
	template_name = 'spots/index.html'
	context_object_name = 'spot_list'

	def get_queryset(self):
		""" Return all spots """
		return Spot.objects.all()

class SpotView(generic.DetailView):
	model = Spot