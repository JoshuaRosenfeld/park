from .keys_secret import MAPS_KEY
from .models import Instance
import requests, time, datetime

def getInstances(address, date, time, time_zone): 
	# convert date and time to UTC

	instance_list = Instance.objects.all().values('id', 'start', 'end', 'rate', 'spot__residence__address')
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
	time_obj = datetime.datetime.strptime(date, "%m/%d/%Y")
	time_tuple = time_obj.timetuple()
	base_time = time.mktime(time_tuple)
	return base_time


