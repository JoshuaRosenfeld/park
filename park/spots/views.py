from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from django.core import serializers
from django.utils.safestring import mark_safe
from . import helper 
from .models import User, Spot, Instance
from .forms import BookForm
import json, time, pytz, decimal
from django.core.serializers.json import DjangoJSONEncoder

SERVICE_RATE = decimal.Decimal(0.1)

def index(request):
	form = BookForm(should_glue=True)
	maps_url = helper.getMapsUrl()
	return render(request, 'spots/index.html', {'form': form, 'script_url': maps_url})

def indexSearch(request):
	form = BookForm(request.GET, should_glue=True)
	maps_url = helper.getMapsUrl()
	if form.is_valid():
		return results(request)
	else:
		return render(request, 'spots/index.html', {'form': form, 'script_url': maps_url})

def results(request):
	form = BookForm(request.GET, should_glue=False)
	maps_url = helper.getMapsUrl()

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
		'script_url': maps_url,},)


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
		},)
