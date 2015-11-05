from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.http import QueryDict
from . import helper 
from .models import User, Spot, Instance
from .forms import SearchForm, SearchFormExtended

def index(request):
	form = SearchForm()
	maps_url = helper.getMapsUrl()
	return render(request, 'spots/index.html', {'form': form, 'script_url': maps_url})

def results(request):
	maps_url = helper.getMapsUrl()
	if 'to_date'in request.GET:
		return renderSpots(request)
	else:
		return requestFromIndex(request)

def requestFromIndex(request):
	form = SearchForm(request.GET)
	maps_url = helper.getMapsUrl()
	if form.is_valid():
		return renderSpots(request)
	else:
		return render(request, 'spots/index.html', {'form': form, 'script_url': maps_url})

def renderSpots(request):
	form = SearchFormExtended(request.GET)
	maps_url = helper.getMapsUrl()
	address = request.GET['address']
	from_date = request.GET['from_date']
	from_time = request.GET['from_time']
	instance_list = helper.getInstances(address, from_date, from_time)
	return render(request, 'spots/spots.html', {
		'instance_list': instance_list,
		'form': form,
		'script_url': maps_url})

class SpotView(generic.DetailView):
	model = Spot
