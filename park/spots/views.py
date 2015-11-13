from django.shortcuts import render, HttpResponseRedirect
from django.utils.safestring import mark_safe
from . import helper 
from .forms import BookForm, MyUserCreationForm
from .models import Instance, Transaction
import json, time, pytz, decimal, urllib
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
		address = request.GET.get('address', None)
		from_date = request.GET.get('from_date', None)
		from_time = request.GET.get('from_time', None)
		to_date = request.GET.get('to_date', None)
		to_time = request.GET.get('to_time', None)

		# get time zones
		from_time_zone = helper.getTimeZone(address, from_date, from_time)
		to_time_zone = helper.getTimeZone(address, to_date, to_time)

		# get instance list
		instances = helper.getInstances(address, from_date, from_time, to_date, to_time, from_time_zone, to_time_zone)

		# format start and stop using destination's time zone
		from_tz = pytz.timezone(from_time_zone)
		to_tz = pytz.timezone(to_time_zone)

		for i in instances:
			loc_start = i['start'].astimezone(from_tz)
			loc_end = i['end'].astimezone(to_tz)
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
	instances = Instance.objects.filter(id=instance_id)
	if not instances:
		return HttpResponseRedirect('/spots/error/')
	else:
		instance = instances[0]

	print(request.GET)
	from_date = request.GET.get('from_date', None)
	from_time = request.GET.get('from_time', None)
	to_date = request.GET.get('to_date', None)
	to_time = request.GET.get('to_time', None)

	if not from_date or not from_time or not to_date or not to_time:
		return HttpResponseRedirect('/spots/error/')

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
	# Retrieve parameters
	instance_id = request.POST.get('instance_id')
	user_id = request.POST.get('user_id')
	from_date = request.POST.get('from_date', None)
	from_time = request.POST.get('from_time', None)
	to_date = request.POST.get('to_date', None)
	to_time = request.POST.get('to_time', None)
	total = request.POST.get('total', None)

	if not instance_id or not user_id or not from_date or not from_time or not to_date or not to_time or not total:
		return HttpResponseRedirect('/spots/error/')

	instances = Instance.objects.filter(id=instance_id)
	if not instances:
		return HttpResponseRedirect('/spots/error/')
	
	instance = instances[0]
	if instance.booked == True:
		return HttpResponseRedirect('/spots/error/')

	address = instance.spot.residence.address
	from_time_zone = helper.getTimeZone(address, from_date, from_time)
	to_time_zone = helper.getTimeZone(address, to_date, to_time)
	guest = User.objects.get(id=user_id)

	# Convert the original instance into 0, 1, or 2 new instances
	start_time = helper.getUtcFromDateTime(from_date, from_time, from_time_zone)
	end_time = helper.getUtcFromDateTime(to_date, to_time, to_time_zone)
	listed_start = instance.start
	listed_end = instance.end

	# Create an instance up until the booked start time
	if start_time != listed_start:
		pre_instance = Instance(start=listed_start, end=start_time, rate=instance.rate, spot=instance.spot)
		pre_instance.save()

	# Create an instance after the booked end time
	if end_time != listed_end:
		post_instance = Instance(start=end_time, end=listed_end, rate=instance.rate, spot=instance.spot)
		post_instance.save()

	# Create a new Transaction
	t = Transaction(start=start_time, end=end_time, cost=total, guest=guest, instance=instance)
	t.save()

	# Delete original instance
	instance.booked = True
	instance.save()

	return render(request, 'spots/success.html')

def register(request):
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
			login(request, new_user)
			url_with_get = urllib.parse.unquote(request.GET['next'])
			return HttpResponseRedirect(url_with_get)
		else:
			return render(request, 'registration/register.html', {'form': form,})
	else:
		form = MyUserCreationForm()
		return render(request, 'registration/register.html', {'form': form,})

def error(request):
	return render(request, 'spots/error.html')

