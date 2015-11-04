from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import User, Spot, Instance
from .forms import SearchForm
from .keys_secret import MAP_KEY

def index(request):
	form = SearchForm()
	return render(request, 'spots/index.html', {'form': form})

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
