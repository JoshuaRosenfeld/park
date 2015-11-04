from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import User, Spot, Instance
from .forms import SearchForm
from .keys_secret import MAPS_KEY
import json

def index(request):
	form = SearchForm()
	script_url = "https://maps.googleapis.com/maps/api/js?key=%s&libraries=places&callback=initAutocomplete" % MAPS_KEY
	return render(request, 'spots/index.html', {'form': form, 'script_url': script_url})

def results(request):
	address = request.GET['address']
	date = request.GET['date']
	time = request.GET['time']
	instance_list = getInstances(address, date, time)
	return render(request, 'spots/spots.html', {'instance_list': instance_list})

def getInstances(address, date, time):
	return Instance.objects.all()

class SpotView(generic.DetailView):
	model = Spot
