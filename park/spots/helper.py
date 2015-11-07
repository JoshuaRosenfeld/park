from .keys_secret import MAPS_KEY
from .models import Instance

def getInstances(address, date, time):
	instance_list = Instance.objects.all().values('id', 'start', 'end', 'rate', 'spot__residence__address')
	return instance_list

def getMapsUrl():
	return "https://maps.googleapis.com/maps/api/js?key=%s&libraries=places&callback=initAutocomplete" % MAPS_KEY