from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from .models import User

def index(request):
	user_list = User.objects.all()
	template = loader.get_template('spots/index.html')
	context = {'user_list': user_list}
	return render(request, 'spots/index.html', context)

def spot(request, spot_id):
	response = "You're looking at spot %s"
	return HttpResponse(response % spot_id)
