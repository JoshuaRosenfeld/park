from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.core import serializers
from django.utils.safestring import mark_safe
from . import helper 
from .models import User, Spot, Instance
from .forms import SearchForm, SearchFormExtended
import json
from django.core.serializers.json import DjangoJSONEncoder

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

	instances = helper.getInstances(address, from_date, from_time)
	instance_list = json.dumps(list(instances), cls=DjangoJSONEncoder)

	return render(request, 'spots/spots.html', {
		'instance_list': mark_safe(instance_list),
		'form': form,
		'script_url': maps_url})

class InstanceView(generic.DetailView):
	model = Instance
