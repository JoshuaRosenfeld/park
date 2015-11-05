from .keys_secret import MAPS_KEY
from .models import Instance

def getInstances(address, date, time):
	return Instance.objects.all()

def getMapsUrl():
	return "https://maps.googleapis.com/maps/api/js?key=%s&libraries=places&callback=initAutocomplete" % MAPS_KEY