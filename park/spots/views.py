from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import User, Spot

def index(request):
	spot_list = Spot.objects.all()
	template = loader.get_template('spots/index.html')
	context = {'spot_list': spot_list}
	return render(request, 'spots/index.html', context)

def spot(request, spot_id):
	spot = get_object_or_404(Spot, pk=spot_id)
	return render(request, 'spots/detail.html', {'spot': spot})