from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from . import helper 
from .models import User, Spot, Instance
from .forms import SearchForm

def index(request):
	form = SearchForm()
	maps_url = helper.getMapsUrl()
	return render(request, 'spots/index.html', {'form': form, 'script_url': maps_url})

def results(request):
	form = SearchForm(request.GET)
	maps_url = helper.getMapsUrl()
	if form.is_valid():
		address = request.GET['address']
		date = request.GET['date']
		time = request.GET['time']
		instance_list = helper.getInstances(address, date, time)
		return render(request, 'spots/spots.html', {
			'address': address,
			'from_date': date,
			'from_time': time,
			'instance_list': instance_list, 
			'script_url': maps_url})
	else:
		return render(request, 'spots/index.html', {'form': form, 'script_url': maps_url})

def update(request):
	return render(request, 'spots/spots.html')

class SpotView(generic.DetailView):
	model = Spot
