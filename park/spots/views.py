from django.shortcuts import render, HttpResponseRedirect
from django.utils.safestring import mark_safe
from . import helper 
from .forms import BookForm
from .models import Instance
import json, time, pytz, decimal
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


SERVICE_RATE = decimal.Decimal(0.1)

def index(request):
	form = BookForm(should_glue=True)
	has_user = request.user.is_authenticated()
	return render(request, 'spots/index.html', {'form': form, 'has_user': has_user,})

def indexSearch(request):
	form = BookForm(request.GET, should_glue=True)
	if form.is_valid():
		return results(request)
	else:
		has_user = request.user.is_authenticated()
		return render(request, 'spots/index.html', {'form': form,  'has_user': has_user,})

def results(request):
	form = BookForm(request.GET, should_glue=False)
	has_user = request.user.is_authenticated()

	if form.is_valid():
		address = request.GET['address']
		from_date = request.GET['from_date']
		from_time = request.GET['from_time']
		to_date = request.GET['to_date']
		to_time = request.GET['to_time']

		# get time zone of destination
		time_zone = helper.getTimeZone(address, from_date)

		# get instance list
		instances = helper.getInstances(address, from_date, from_time, to_date, to_time, time_zone)

		# format start and stop using destination's time zone
		tz = pytz.timezone(time_zone)
		for i in instances:
			loc_start = i['start'].astimezone(tz)
			loc_end = i['end'].astimezone(tz)
			i['start'] = loc_start.strftime('%I:%M %p on %m/%d')
			i['end'] = loc_end.strftime('%I:%M %p on %m/%d')

		instance_list = json.dumps(list(instances), cls=DjangoJSONEncoder)
	else:
		instance_list = []

	return render(request, 'spots/spots.html', {
		'instance_list': mark_safe(instance_list),
		'form': form,
		'has_user': has_user,},)

@login_required
def instance(request, instance_id):
	instance = Instance.objects.filter(id=instance_id)[0]
	from_date = request.GET['from_date']
	from_time = request.GET['from_time']
	to_date = request.GET['to_date']
	to_time = request.GET['to_time']

	num_hours = decimal.Decimal(helper.getDiff(from_date, from_time, to_date, to_time))
	spot_cost = round((instance.rate * num_hours), 2)
	service_fee = round((SERVICE_RATE * spot_cost), 2)
	total = round((spot_cost + service_fee), 2)

	has_user = request.user.is_authenticated()
	return render(request, 'spots/instance_detail.html', {
		'instance': instance,
		'from_date': from_date,
		'from_time': from_time,
		'to_date': to_date,
		'to_time': to_time,
		'num_hours': num_hours,
		'spot_cost': spot_cost,
		'service_fee': service_fee,
		'total': total,
	 	'has_user': has_user,
		},)

def success(request):
	return render(request, 'spots/success.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, new_user)
			return HttpResponseRedirect(request.GET['next'])
		else:
			return render(request, 'registration/register.html', {'form': form,})
	else:
		form = UserCreationForm()
		return render(request, 'registration/register.html', {'form': form,})
