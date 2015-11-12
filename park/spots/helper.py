from .keys_secret import MAPS_KEY
from .models import Instance
import requests, time, datetime, pytz

def getInstances(address, from_date, from_time, to_date, to_time, from_time_zone, to_time_zone): 
	utc_from = getUtcFromDateTime(from_date, from_time, from_time_zone)
	utc_to = getUtcFromDateTime(to_date, to_time, to_time_zone)

	instance_list = Instance.objects.filter(start__lte=utc_from, end__gte=utc_to, booked=False).values('id', 'start', 'end', 'rate', 'spot__residence__address', 'spot__residence__lat', 'spot__residence__lng')
	return instance_list

def getMapsUrl():
	return "https://maps.googleapis.com/maps/api/js?key=%s&libraries=places&callback=initAutocomplete" % MAPS_KEY

def getTimeZone(address, date, time):
	obj = makeDateTime(date, time)
	lat, lng = getLatLng(address)
	latlng = "%s, %s" % (lat, lng)
	time = getTimeStamp(obj)
	payload = {'location': latlng, 'key': MAPS_KEY, 'timestamp': time}
	r = requests.get('https://maps.googleapis.com/maps/api/timezone/json', params=payload)
	return r.json()['timeZoneId']

def getLatLng(address):
	payload = {'address': address, 'key': MAPS_KEY}
	r = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload)
	results = r.json()['results'][0]['geometry']['location']
	lat = results['lat']
	lng = results['lng']
	return (lat, lng)

def getTimeStamp(obj):
	time_tuple = obj.timetuple()
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

def getUtcFromDateTime(date, time, time_zone):
	# combine dates and times
	obj = makeDateTime(date, time)

	# localize and convert to UTC
	tz = pytz.timezone(time_zone)
	loc_obj = tz.localize(obj)
	utc_obj = loc_obj.astimezone(pytz.utc)
	return utc_obj

def makeDateTime(date, time):
	date_obj = getDate(date)
	time_obj = getTime(time)
	obj = datetime.datetime.combine(date_obj, time_obj)
	return obj
