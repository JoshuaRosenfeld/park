from .keys_secret import MAPS_KEY
from .models import Instance
import requests, time, datetime, pytz

def getInstances(address, from_date, from_time, to_date, to_time, time_zone): 
	# combine dates and times
	from_date_obj = getDate(from_date)
	from_time_obj = getTime(from_time)
	to_date_obj = getDate(to_date)
	to_time_obj = getTime(to_time)
	from_obj = datetime.datetime.combine(from_date_obj, from_time_obj)
	to_obj = datetime.datetime.combine(to_date_obj, to_time_obj)

	# localize dates and times
	tz = pytz.timezone(time_zone)
	loc_from = tz.localize(from_obj)
	loc_to = tz.localize(to_obj)
	
	# convert to UTC
	utc_from = loc_from.astimezone(pytz.utc)
	utc_to = loc_to.astimezone(pytz.utc)

	instance_list = Instance.objects.filter(start__lte=utc_from, end__gte=utc_to).values('id', 'start', 'end', 'rate', 'spot__residence__address')
	return instance_list

def getMapsUrl():
	return "https://maps.googleapis.com/maps/api/js?key=%s&libraries=places&callback=initAutocomplete" % MAPS_KEY

def getTimeZone(address, date):
	latlng = getLatLng(address)
	time = getTimeStamp(date)
	payload = {'location': latlng, 'key': MAPS_KEY, 'timestamp': time}
	r = requests.get('https://maps.googleapis.com/maps/api/timezone/json', params=payload)
	return r.json()['timeZoneId']

def getLatLng(address):
	payload = {'address': address, 'key': MAPS_KEY}
	r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
	print(r.url)
	results = r.json()['results'][0]['geometry']['location']
	lat = results['lat']
	lng = results['lng']
	return "%s, %s" % (lat, lng)

def getTimeStamp(date):
	time_obj = getDate(date)
	time_tuple = time_obj.timetuple()
	base_time = time.mktime(time_tuple)
	return base_time

def getDiff(from_date, from_time, to_date, to_time):
	from_date_obj = getDate(from_date)
	from_time_obj = getTime(from_time)
	to_date_obj = getDate(to_date)
	to_time_obj = getTime(to_time)

	from_obj = datetime.datetime.combine(from_date_obj, from_time_obj)
	to_obj = datetime.datetime.combine(to_date_obj, to_time_obj)
	diff = (to_obj - from_obj).total_seconds() / 3600
	return diff

def getDate(date):
	return datetime.datetime.strptime(date, "%m/%d/%Y")

def getTime(time):
	return datetime.datetime.strptime(time, "%I:%M %p").time()
